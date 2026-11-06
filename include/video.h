/* PIO video output
 * Dual Mode: Composite Video (CVBS) & VGA Monitor
 *
 * SCHUBIGER.CL - PiMac 2040
 */

#ifndef VIDEO_H
#define VIDEO_H

#include <inttypes.h>

void    video_composite_init(uint32_t *framebuffer);
void    video_vga_init(uint32_t *framebuffer);
void    video_init(uint32_t *framebuffer);

#endif
