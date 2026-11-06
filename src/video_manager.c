/*
 * video_manager.c - Dual Video Output Selector for PiMac 2040
 *
 * Checks GPIO_VID_MODE_SELECT (GP0 on RP2040-Zero pin 1):
 *   - Open / Floating (Pull-up = 1): Composite Video (CVBS) on GP8/GP9 (15.7 kHz NTSC 480i)
 *   - Jumper to GND   (Pull-down = 0): VGA Monitor on GP26..GP29 (31.5 kHz 640x480)
 *
 * SCHUBIGER.CL - https://schubiger.cl
 */

#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hw.h"
#include "video.h"

void video_init(uint32_t *framebuffer)
{
    // Configure GP0 with internal pull-up
    gpio_init(GPIO_VID_MODE_SELECT);
    gpio_set_dir(GPIO_VID_MODE_SELECT, GPIO_IN);
    gpio_pull_up(GPIO_VID_MODE_SELECT);
    sleep_ms(5); // Stabilization delay

    int is_vga = (gpio_get(GPIO_VID_MODE_SELECT) == 0);

    if (is_vga) {
        printf("=====================================================\n");
        printf("PiMac 2040: VGA Monitor Mode (640x480 @ 60Hz)\n");
        printf("  Pins: Video=GP26, VS=GP27, CLK=GP28, HS=GP29\n");
        printf("  Status: Jumper detected on GP0 (GND)\n");
        printf("=====================================================\n");
        video_vga_init(framebuffer);
    } else {
        printf("=====================================================\n");
        printf("PiMac 2040: Composite Video Mode (CVBS 480i NTSC)\n");
        printf("  Pins: SYNC=GP8, DATA=GP9 (RCA Output)\n");
        printf("  Status: GP0 Open (Default Mode)\n");
        printf("=====================================================\n");
        video_composite_init(framebuffer);
    }
}
