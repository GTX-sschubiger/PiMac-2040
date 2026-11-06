/*
 * mac_status.h - System Status Indicator for RP2040-Zero
 * RGB LED WS2812 Visual Feedback for Macintosh 208K Emulator
 *
 * SCHUBIGER.CL
 */

#ifndef MAC_STATUS_H
#define MAC_STATUS_H

#include <inttypes.h>

typedef enum {
    MAC_STATUS_INIT = 0,      // Cyan / Blue: Hardware init & POST
    MAC_STATUS_WAIT_DISK,     // Amber / Yellow blink: No disk inserted (Floppy ?)
    MAC_STATUS_BOOTING,       // Orange flicker: Loading boot sectors (Happy Mac)
    MAC_STATUS_RUNNING,       // Retro Apple Green Breathing: Desktop / Finder idle
    MAC_STATUS_PANIC          // Fast Red Strobe: System Crash / Sad Mac
} mac_status_t;

void mac_status_init(void);
void mac_set_status(mac_status_t status);
void mac_notify_disk_read(void);
void mac_notify_disk_write(void);
void mac_status_poll(void);

#endif
