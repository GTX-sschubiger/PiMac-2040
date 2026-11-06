/* Composite Video output (CVBS) for Macintosh 128K/208K Emulator on RP2040
 *
 * Replaces VGA output with standard Baseband Monochrome Composite Video (CVBS).
 * Drives an RCA connector via a simple 2-resistor DAC:
 *
 *   GPIO_VID_SYNC (Pin 8)  ---[ 470R - 560R ]---+---> Center Pin (Video Signal)
 *                                               |
 *   GPIO_VID_DATA (Pin 9)  ---[ 240R - 270R ]---+
 *
 *   GND (RP2040 Ground)    -------------------------> Outer Ring (Ground Shield)
 *
 * Output Voltages into standard 75 Ohm TV load:
 *   - Sync Pulse:   0.0 V  (0 IRE)
 *   - Blank / Black: 0.3 V  (40 IRE)
 *   - 100% White:    1.0 V  (100 IRE)
 *
 * Timing:
 *   - Interlaced 480i NTSC (525 lines total, 60 Hz field rate)
 *   - Centered 512x342 Macintosh resolution:
 *       Even field displays scanlines 0, 2, 4, ... 340 (171 lines)
 *       Odd field displays scanlines 1, 3, 5, ... 341 (171 lines)
 *       Total visible height = 342 lines, perfectly fitting into 480i!
 *       Horizontal border: 64 dots left / right
 *       Vertical border: 37 lines top / 36 lines bottom
 *
 * Zero Framebuffer Copies:
 *   Direct DMA from the 1BPP Macintosh memory inside umac_ram!
 */

#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include "hardware/clocks.h"
#include "hardware/dma.h"
#include "hardware/gpio.h"
#include "hardware/structs/padsbank0.h"
#include "pio_composite.pio.h"

#include "hw.h"
#include "video.h"

////////////////////////////////////////////////////////////////////////////////
// Timing definitions for NTSC Composite Video (15,734 Hz / 60 Hz)

// System clock = 250 MHz. PIO clock = 20 MHz (clkdiv = 12.5).
// 2 PIO cycles = 100 ns = 1 pixel / timing unit.
#define COMPOSITE_CLK_DIV       12.5f

#define COMP_HSW                47      // 4.7 us HSYNC pulse
#define COMP_HBP                54      // 5.4 us Back Porch & Left Border
#define COMP_HRES               512     // 51.2 us Active Mac Display
#define COMP_HFP                23      // 2.3 us Front Porch & Right Border
#define COMP_H_TOTAL            (COMP_HSW + COMP_HBP + COMP_HRES + COMP_HFP) // 636 units = 63.60 us

// Field geometry (Interlaced 480i: 262 lines field 0, 263 lines field 1)
#define COMP_FIELD0_LINES       262
#define COMP_FIELD1_LINES       263

#define COMP_VSYNC_LINES        3       // Lines 0..2: Broad sync pulses
#define COMP_VBLANK_LINES       15      // Lines 3..17: Vertical blanking
#define COMP_TOP_BORDER_LINES   37      // Lines 18..54: Top black border
#define COMP_ACTIVE_LINES       171     // Lines 55..225: 171 active lines per field (171*2 = 342)

#define COMP_ACTIVE_START       (COMP_VSYNC_LINES + COMP_VBLANK_LINES + COMP_TOP_BORDER_LINES)
#define COMP_ACTIVE_END         (COMP_ACTIVE_START + COMP_ACTIVE_LINES)

#define VIDEO_FB_HRES           512
#define VIDEO_FB_VRES           342
#define VIDEO_VISIBLE_WPL       (VIDEO_FB_HRES / 32) // 16 32-bit words per line

////////////////////////////////////////////////////////////////////////////////
// Video DMA and Framebuffer Pointers

static uint32_t video_null[VIDEO_VISIBLE_WPL];
static uint32_t *video_framebuffer;

// Configuration words sent to PIO via DMA:
// [0, 1] for normal active/blanking lines
// [2, 3] for VSYNC broad pulse lines
static uint32_t video_dma_cfg[4];

static uint8_t video_dmach_tx;
static uint8_t video_dmach_descr_cfg;
static uint8_t video_dmach_descr_data;

typedef struct {
        const void *raddr;
        void *waddr;
        uint32_t count;
        uint32_t ctrl;
} dma_descr_t;

static dma_descr_t video_dmadescr_cfg;
static dma_descr_t video_dmadescr_data;

static volatile unsigned int video_current_line = 0;
static volatile unsigned int video_current_field = 0;

static inline const uint32_t *__not_in_flash_func(video_line_addr)(unsigned int line, unsigned int field)
{
        if (line >= COMP_ACTIVE_START && line < COMP_ACTIVE_END) {
                unsigned int active_idx = line - COMP_ACTIVE_START;
                // Interlace: field 0 maps to even lines, field 1 to odd lines
                unsigned int mac_y = (active_idx * 2) + (field & 1);
                if (mac_y < VIDEO_FB_VRES) {
                        return &video_framebuffer[mac_y * VIDEO_VISIBLE_WPL];
                }
        }
        return (const uint32_t *)video_null;
}

static inline const uint32_t *__not_in_flash_func(video_cfg_addr)(unsigned int line)
{
        // VSYNC broad pulses for first COMP_VSYNC_LINES lines
        return &video_dma_cfg[(line < COMP_VSYNC_LINES) ? 2 : 0];
}

static void __not_in_flash_func(video_dma_prep_new)(void)
{
        dma_hw->ch[video_dmach_descr_cfg].read_addr = (uintptr_t)&video_dmadescr_cfg;
        dma_hw->ch[video_dmach_descr_cfg].transfer_count = 4;
        dma_hw->ch[video_dmach_descr_data].read_addr = (uintptr_t)&video_dmadescr_data;
        dma_hw->ch[video_dmach_descr_data].transfer_count = 4;

        video_dmadescr_cfg.raddr = video_cfg_addr(video_current_line);
        video_dmadescr_data.raddr = video_line_addr(video_current_line, video_current_field);

        video_current_line++;
        unsigned int max_lines = (video_current_field == 0) ? COMP_FIELD0_LINES : COMP_FIELD1_LINES;
        if (video_current_line >= max_lines) {
                video_current_line = 0;
                video_current_field ^= 1;
        }
}

static void __not_in_flash_func(video_dma_irq)(void)
{
        if (dma_channel_get_irq0_status(video_dmach_descr_data)) {
                dma_channel_acknowledge_irq0(video_dmach_descr_data);
                video_dma_prep_new();
        }
}

static void video_prep_buffer(void)
{
        // In the Macintosh 1BPP framebuffer, 0 = White, 1 = Black.
        // Because the DATA GPIO is inverted, 0xff becomes 0 (0.3V Black) on the pin!
        memset(video_null, 0xff, VIDEO_VISIBLE_WPL * 4);

        // Word 0 layout:
        // [31] = vsync_flag (0 = normal, 1 = broad pulse)
        // [30:23] = HSW - 1
        // [22:15] = HBP - 3
        // [14:7]  = HFP - 4
        // [6:0]   = 0

        // Normal scanline timing
        uint32_t norm_timing = ((COMP_HSW - 1) << 23) |
                               ((COMP_HBP - 3) << 15) |
                               ((COMP_HFP - 4) << 7);
        video_dma_cfg[0] = norm_timing;
        video_dma_cfg[1] = VIDEO_FB_HRES - 1;

        // VSYNC scanline timing (vsync_flag = 1 in bit 31)
        uint32_t vsync_timing = 0x80000000 |
                                ((COMP_HSW - 1) << 23) |
                                ((COMP_HBP - 3) << 15) |
                                ((COMP_HFP - 4) << 7);
        video_dma_cfg[2] = vsync_timing;
        video_dma_cfg[3] = VIDEO_FB_HRES - 1;
}

static void video_init_dma(void)
{
        video_dmach_tx = dma_claim_unused_channel(true);
        video_dmach_descr_cfg = dma_claim_unused_channel(true);
        video_dmach_descr_data = dma_claim_unused_channel(true);

        // TX Channel Config descriptor
        dma_channel_config dc_tx_c = dma_channel_get_default_config(video_dmach_tx);
        channel_config_set_dreq(&dc_tx_c, DREQ_PIO0_TX0);
        channel_config_set_transfer_data_size(&dc_tx_c, DMA_SIZE_32);
        channel_config_set_read_increment(&dc_tx_c, true);
        channel_config_set_write_increment(&dc_tx_c, false);
        channel_config_set_bswap(&dc_tx_c, false);
        channel_config_set_chain_to(&dc_tx_c, video_dmach_descr_data);

        video_dmadescr_cfg.raddr = NULL;
        video_dmadescr_cfg.waddr = (void *)&pio0_hw->txf[0];
        video_dmadescr_cfg.count = 2; // 2 words config
        video_dmadescr_cfg.ctrl = dc_tx_c.ctrl;

        // TX Channel Data descriptor
        dma_channel_config dc_tx_d = dma_channel_get_default_config(video_dmach_tx);
        channel_config_set_dreq(&dc_tx_d, DREQ_PIO0_TX0);
        channel_config_set_transfer_data_size(&dc_tx_d, DMA_SIZE_32);
        channel_config_set_read_increment(&dc_tx_d, true);
        channel_config_set_write_increment(&dc_tx_d, false);
        channel_config_set_bswap(&dc_tx_d, true); // Byte swap for big-endian Mac FB
        channel_config_set_chain_to(&dc_tx_d, video_dmach_descr_cfg);

        video_dmadescr_data.raddr = NULL;
        video_dmadescr_data.waddr = (void *)&pio0_hw->txf[0];
        video_dmadescr_data.count = VIDEO_VISIBLE_WPL; // 16 words (512 bits)
        video_dmadescr_data.ctrl = dc_tx_d.ctrl;

        // Descr CFG channel
        dma_channel_config dcfg = dma_channel_get_default_config(video_dmach_descr_cfg);
        channel_config_set_transfer_data_size(&dcfg, DMA_SIZE_32);
        channel_config_set_read_increment(&dcfg, true);
        channel_config_set_write_increment(&dcfg, true);
        channel_config_set_ring(&dcfg, true, 4);
        dma_channel_configure(video_dmach_descr_cfg, &dcfg,
                              &dma_hw->ch[video_dmach_tx].read_addr,
                              &video_dmadescr_cfg,
                              4, false);

        // Descr DATA channel
        dma_channel_config ddata = dma_channel_get_default_config(video_dmach_descr_data);
        channel_config_set_transfer_data_size(&ddata, DMA_SIZE_32);
        channel_config_set_read_increment(&ddata, true);
        channel_config_set_write_increment(&ddata, true);
        channel_config_set_ring(&ddata, true, 4);
        dma_channel_set_irq0_enabled(video_dmach_descr_data, true);
        dma_channel_configure(video_dmach_descr_data, &ddata,
                              &dma_hw->ch[video_dmach_tx].read_addr,
                              &video_dmadescr_data,
                              4, false);
}

void video_composite_init(uint32_t *framebuffer)
{
        printf("Composite Video Init: SYNC=GP%d, DATA=GP%d (480i NTSC)\n",
               GPIO_COMP_SYNC, GPIO_COMP_DATA);

        uint offset = pio_add_program(pio0, &pio_composite_program);
        pio_composite_program_init(pio0, 0, offset,
                                  GPIO_COMP_SYNC, GPIO_COMP_DATA,
                                  COMPOSITE_CLK_DIV);

        // Invert data pin: Mac 0 = White (high), 1 = Black (low)
        gpio_set_outover(GPIO_COMP_DATA, GPIO_OVERRIDE_INVERT);

        // Maximum drive strength for 75 Ohm termination
        hw_write_masked(&padsbank0_hw->io[GPIO_COMP_SYNC],
                        PADS_BANK0_GPIO0_DRIVE_VALUE_12MA << PADS_BANK0_GPIO0_DRIVE_LSB,
                        PADS_BANK0_GPIO0_DRIVE_BITS);
        hw_write_masked(&padsbank0_hw->io[GPIO_COMP_DATA],
                        PADS_BANK0_GPIO0_DRIVE_VALUE_12MA << PADS_BANK0_GPIO0_DRIVE_LSB,
                        PADS_BANK0_GPIO0_DRIVE_BITS);

        irq_set_exclusive_handler(DMA_IRQ_0, video_dma_irq);
        irq_set_enabled(DMA_IRQ_0, true);

        video_init_dma();

        video_current_line = 0;
        video_current_field = 0;
        video_framebuffer = framebuffer;
        video_prep_buffer();

        video_dma_prep_new();
        dma_channel_start(video_dmach_descr_cfg);
}
