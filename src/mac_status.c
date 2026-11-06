/*
 * mac_status.c - System Status Indicator for RP2040-Zero
 * RGB LED WS2812 Visual Feedback for Macintosh 208K Emulator
 *
 * SCHUBIGER.CL - https://schubiger.cl
 */

#include "mac_status.h"
#include "hw.h"
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/sync.h"

// Track system status
static volatile mac_status_t current_status = MAC_STATUS_INIT;
static volatile uint32_t disk_read_flash_until_ms = 0;
static volatile uint32_t disk_write_flash_until_ms = 0;
static uint32_t boot_sector_count = 0;
static uint32_t last_boot_read_time_ms = 0;

// WS2812 GRB bitbang protocol for RP2040 at 250 MHz sys_clk (4ns/cycle)
static void ws2812_send_grb(uint8_t r, uint8_t g, uint8_t b)
{
#ifdef BOARD_RP2040_ZERO
    uint32_t grb = ((uint32_t)g << 16) | ((uint32_t)r << 8) | (uint32_t)b;
    uint32_t save = save_and_disable_interrupts();

    for (int i = 23; i >= 0; i--) {
        if (grb & (1u << i)) {
            // T1H: ~700ns (175 cycles), T1L: ~600ns (150 cycles)
            gpio_put(RP2040_ZERO_RGB_PIN, 1);
            busy_wait_at_least_cycles(175);
            gpio_put(RP2040_ZERO_RGB_PIN, 0);
            busy_wait_at_least_cycles(150);
        } else {
            // T0H: ~340ns (85 cycles), T0L: ~800ns (200 cycles)
            gpio_put(RP2040_ZERO_RGB_PIN, 1);
            busy_wait_at_least_cycles(85);
            gpio_put(RP2040_ZERO_RGB_PIN, 0);
            busy_wait_at_least_cycles(200);
        }
    }

    restore_interrupts(save);
#else
    // Fallback for standard Pico green LED on GP25
    gpio_put(GPIO_LED_PIN, (r || g || b));
#endif
}

void mac_status_init(void)
{
#ifdef BOARD_RP2040_ZERO
    gpio_init(RP2040_ZERO_RGB_PIN);
    gpio_set_dir(RP2040_ZERO_RGB_PIN, GPIO_OUT);
    gpio_put(RP2040_ZERO_RGB_PIN, 0);
#else
    gpio_init(GPIO_LED_PIN);
    gpio_set_dir(GPIO_LED_PIN, GPIO_OUT);
    gpio_put(GPIO_LED_PIN, 0);
#endif

    // Initial state: Cyan (Hardware init / POST)
    current_status = MAC_STATUS_INIT;
    ws2812_send_grb(0, 20, 30);
}

void mac_set_status(mac_status_t status)
{
    current_status = status;
}

void mac_notify_disk_read(void)
{
    uint32_t now = to_ms_since_boot(get_absolute_time());
    disk_read_flash_until_ms = now + 65; // Flash for 65ms

    // Boot tracking: if in INIT or WAIT_DISK, automatically promote to BOOTING
    if (current_status == MAC_STATUS_INIT || current_status == MAC_STATUS_WAIT_DISK) {
        current_status = MAC_STATUS_BOOTING;
        boot_sector_count = 0;
    }

    if (current_status == MAC_STATUS_BOOTING) {
        boot_sector_count++;
        last_boot_read_time_ms = now;
    }
}

void mac_notify_disk_write(void)
{
    uint32_t now = to_ms_since_boot(get_absolute_time());
    disk_write_flash_until_ms = now + 110; // Flash for 110ms
}

void mac_status_poll(void)
{
    static uint32_t last_poll_ms = 0;
    uint32_t now = to_ms_since_boot(get_absolute_time());

    // Update LED at ~40 Hz (every 25 ms)
    if (now - last_poll_ms < 25) {
        return;
    }
    last_poll_ms = now;

    // Auto-transition from BOOTING to RUNNING once initial boot read burst subsides
    // (Typically ~120 sectors read during boot, followed by > 1.2s of disk idle when Finder loads)
    if (current_status == MAC_STATUS_BOOTING) {
        if (boot_sector_count > 60 && (now - last_boot_read_time_ms > 1200)) {
            current_status = MAC_STATUS_RUNNING;
        }
    }

    // 1. Priority 1: Panic / Crash (Fast Red Strobe @ 6 Hz)
    if (current_status == MAC_STATUS_PANIC) {
        uint32_t phase = (now / 80) % 2;
        if (phase == 0) {
            ws2812_send_grb(50, 0, 0); // Bright Red
        } else {
            ws2812_send_grb(0, 0, 0);
        }
        return;
    }

    // 2. Priority 2: Disk Write Activity (Magenta / Pink Flash)
    if (now < disk_write_flash_until_ms) {
        ws2812_send_grb(45, 0, 25);
        return;
    }

    // 3. Priority 3: Disk Read Activity (Bright Warm Orange Flash)
    if (now < disk_read_flash_until_ms) {
        ws2812_send_grb(50, 18, 0);
        return;
    }

    // 4. Default Base Status Colors:
    switch (current_status) {
    case MAC_STATUS_INIT:
        // Soft Cyan
        ws2812_send_grb(0, 15, 25);
        break;

    case MAC_STATUS_WAIT_DISK: {
        // Pulsing Amber / Gold (Flashing Floppy '?' indicator at 1 Hz)
        uint32_t phase = (now / 500) % 2;
        if (phase == 0) {
            ws2812_send_grb(35, 18, 0); // Amber
        } else {
            ws2812_send_grb(3, 1, 0);   // Dim glow
        }
        break;
    }

    case MAC_STATUS_BOOTING: {
        // Orange breathing / pulse during OS load
        uint32_t step = (now / 20) % 50;
        int level = (step < 25) ? step : (50 - step); // 0..25
        uint8_t r = 15 + level;
        uint8_t g = 4 + (level / 3);
        ws2812_send_grb(r, g, 0);
        break;
    }

    case MAC_STATUS_RUNNING: {
        // Vintage Apple Green organic breathing pulse (2.5s cycle)
        // 0..100 steps
        uint32_t step = (now / 25) % 100;
        int level = (step < 50) ? step : (100 - step); // 0..50
        // Scale green from 6 (dim glow) to 32 (vibrant retro green)
        uint8_t g = 6 + (level * 26) / 50;
        uint8_t b = 1 + (level * 5) / 50;
        ws2812_send_grb(0, g, b);
        break;
    }

    default:
        ws2812_send_grb(0, 10, 0);
        break;
    }
}
