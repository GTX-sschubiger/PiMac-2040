/*
 * PiMac 2040 (SCHUBIGER.CL) pin definitions
 * Tailored for RP2040-Zero (Waveshare / AliExpress mini RP2040)
 * and standard Raspberry Pi Pico.
 */

#ifndef HW_H
#define HW_H

#include "pico/stdlib.h"

// Onboard WS2812 RGB LED on RP2040-Zero is on GP16
#define RP2040_ZERO_RGB_PIN     16

#ifdef BOARD_RP2040_ZERO
#define GPIO_LED_PIN            RP2040_ZERO_RGB_PIN
#else
#ifndef PICO_DEFAULT_LED_PIN
#define GPIO_LED_PIN            25
#else
#define GPIO_LED_PIN            PICO_DEFAULT_LED_PIN
#endif
#endif

// Video Mode Selection Pin (GP0 on RP2040-Zero pin 1)
// Jumper Open (Pull-up = 1): Composite Video (CVBS) on GP8/GP9 (15.7 kHz NTSC 480i)
// Jumper to GND (Pull-down = 0): VGA Monitor on GP26..GP29 (31.5 kHz 640x480)
#ifndef GPIO_VID_MODE_SELECT
#define GPIO_VID_MODE_SELECT    0
#endif

// Composite Video Pins (GP8 = Sync, GP9 = Data)
#define GPIO_COMP_SYNC          8
#define GPIO_COMP_DATA          9

// VGA Video Pins (GP26 = Data, GP27 = VS, GP28 = CLK, GP29 = HS)
#define GPIO_VGA_BASE           26
#define GPIO_VGA_DATA           (GPIO_VGA_BASE)       // GP26
#define GPIO_VGA_VS             (GPIO_VGA_BASE + 1)   // GP27
#define GPIO_VGA_CLK            (GPIO_VGA_BASE + 2)   // GP28
#define GPIO_VGA_HS             (GPIO_VGA_BASE + 3)   // GP29

// Legacy aliases for backward compatibility
#define GPIO_VID_SYNC           GPIO_COMP_SYNC
#define GPIO_VID_DATA           GPIO_COMP_DATA
#define GPIO_VID_BASE           GPIO_VGA_BASE
#define GPIO_VID_VS             GPIO_VGA_VS
#define GPIO_VID_CLK            GPIO_VGA_CLK
#define GPIO_VID_HS             GPIO_VGA_HS

#endif
