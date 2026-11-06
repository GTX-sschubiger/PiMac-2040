#!/usr/bin/env python3
"""
Generador de Diagramas Reales de Conexión Hardware para PiMac 2040
Utiliza la fotografía física exacta del RP2040-Zero (Tenstar Robot / Waveshare)
Genera diagramas con conexiones milimétricas basadas en el pinout real.
Desarrollado para SCHUBIGER.CL (https://schubiger.cl)
"""

import os
import shutil
from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REF_IMAGE_PATH = os.path.join(PROJECT_DIR, "github", "assets", "rp2040_zero_reference.png")
OUTPUT_DIR_GITHUB = os.path.join(PROJECT_DIR, "github", "assets")
OUTPUT_DIR_ROOT = os.path.join(PROJECT_DIR, "assets")

def load_font(size, bold=False):
    # Try Windows fonts or default
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/consola.ttf"
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_resistor(draw, p1, p2, val_str, bands):
    """Dibuja una resistencia axial de orificio pasante con sus franjas de colores reales."""
    x1, y1 = p1
    x2, y2 = p2
    mx = (x1 + x2) // 2
    my = (y1 + y2) // 2
    
    # Lead wire
    draw.line([p1, p2], fill="#94a3b8", width=3)
    
    # Resistor body
    bw, bh = 56, 18
    body_box = [mx - bw//2, my - bh//2, mx + bw//2, my + bh//2]
    draw.rectangle(body_box, fill="#e2d9c8", outline="#78716c", width=2)
    
    # 4 Bands
    band_w = 6
    band_spacing = 10
    start_bx = mx - bw//2 + 8
    for i, color in enumerate(bands):
        bx = start_bx + i * band_spacing
        draw.rectangle([bx, my - bh//2 + 2, bx + band_w, my + bh//2 - 2], fill=color)
        
    # Value text
    f = load_font(13, bold=True)
    draw.text((mx - 25, my - bh//2 - 18), val_str, fill="#f8fafc", font=f)

def draw_rca_connector(draw, pos):
    """Dibuja un conector RCA hembra amarillo para chasis."""
    cx, cy = pos
    # Outer mounting hexagon/ring
    draw.ellipse([cx - 38, cy - 38, cx + 38, cy + 38], fill="#334155", outline="#cbd5e1", width=3)
    # Yellow insulator ring
    draw.ellipse([cx - 28, cy - 28, cx + 28, cy + 28], fill="#eab308", outline="#ca8a04", width=2)
    # Center gold socket
    draw.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill="#fef08a", outline="#a16207", width=3)
    draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill="#1e293b")

def draw_vga_connector(draw, pos):
    """Dibuja un conector D-Sub DE-15 (VGA DB-15 hembra) azul."""
    x, y, w, h = pos
    # Metal mounting flange
    draw.rounded_rectangle([x - 15, y - 10, x + w + 15, y + h + 10], radius=8, fill="#64748b", outline="#cbd5e1", width=2)
    # Screw posts
    draw.rectangle([x - 12, y + h//2 - 6, x - 2, y + h//2 + 6], fill="#cbd5e1")
    draw.rectangle([x + w + 2, y + h//2 - 6, x + w + 12, y + h//2 + 6], fill="#cbd5e1")
    # Blue plastic insert
    draw.rounded_rectangle([x, y, x + w, y + h], radius=6, fill="#0284c7", outline="#0369a1", width=2)
    
    # 3 rows of 5 pin holes
    pin_r = 3
    for row in range(3):
        row_y = y + 12 + row * 10
        offset_x = 4 if row == 1 else 0
        for col in range(5):
            col_x = x + 15 + offset_x + col * 14
            draw.ellipse([col_x - pin_r, row_y - pin_r, col_x + pin_r, row_y + pin_r], fill="#0f172a", outline="#fef08a", width=1)

def draw_sd_adapter(draw, pos):
    """Dibuja el adaptador plástico SD a MicroSD hackeado con sus 7 pistas doradas."""
    x, y, w, h = pos
    # Black plastic body with cut corner at top-right
    draw.polygon([
        (x, y), (x + w - 20, y), (x + w, y + 20),
        (x + w, y + h), (x, y + h)
    ], fill="#1e293b", outline="#475569")
    
    # Golden contact pads on back (pins 9, 1, 2, 3, 4, 5, 6, 7, 8)
    gold_color = "#eab308"
    pad_h = 24
    pad_w = 6
    for i in range(8):
        px = x + 12 + i * 11
        draw.rectangle([px, y + 8, px + pad_w, y + 8 + pad_h], fill=gold_color, outline="#a16207", width=1)
    
    # MicroSD slot cutout at bottom
    draw.rectangle([x + w//2 - 25, y + h - 8, x + w//2 + 25, y + h], fill="#0f172a")

def draw_usb_port(draw, pos, label):
    """Dibuja un conector USB-A hembra reciclado."""
    x, y, w, h = pos
    draw.rectangle([x, y, x + w, y + h], fill="#94a3b8", outline="#cbd5e1", width=2)
    # White/black plastic tongue inside
    draw.rectangle([x + 6, y + 6, x + w - 6, y + h//2], fill="#f8fafc")
    # 4 Pins
    for i in range(4):
        px = x + 12 + i * 12
        draw.rectangle([px, y + h//2 + 2, px + 4, y + h - 4], fill="#eab308")

def build_diagram(is_version2=False):
    canvas_w, canvas_h = 1600, 1020
    im = Image.new("RGBA", (canvas_w, canvas_h), "#0b0f19")
    draw = ImageDraw.Draw(im)

    # 1. Background Grid & Header
    for gx in range(0, canvas_w, 40):
        draw.line([(gx, 0), (gx, canvas_h)], fill="#111827", width=1)
    for gy in range(0, canvas_h, 40):
        draw.line([(0, gy), (canvas_w, gy)], fill="#111827", width=1)

    # Header Box
    f_title = load_font(26, bold=True)
    f_sub = load_font(15)
    f_badge = load_font(13, bold=True)
    f_note = load_font(12)
    f_pin = load_font(13, bold=True)

    header_title = "PiMac 2040 — Versión 2: Dual Video (VGA + Video Compuesto) y Opción OTG" if is_version2 else "PiMac 2040 — Versión 1: Solo Video Compuesto RCA (TV CRT / AV)"
    draw.text((40, 25), header_title, fill="#38bdf8", font=f_title)
    draw.text((40, 65), "Conexiones físicas reales sobre placa ultra-compacta Tenstar Robot / Waveshare RP2040-Zero — SCHUBIGER.CL", fill="#94a3b8", font=f_sub)

    # 2. Cargar y pegar la foto real de la RP2040-Zero
    ref_img = Image.open(REF_IMAGE_PATH)
    front_board = ref_img.crop((18, 175, 345, 635)) # 327 x 460
    # Escalar ligeramente para nitidez óptima
    board_w, board_h = 360, 506
    front_board = front_board.resize((board_w, board_h), Image.Resampling.LANCZOS)
    
    board_x = 620
    board_y = 220
    im.paste(front_board, (board_x, board_y), front_board if front_board.mode == 'RGBA' else None)
    
    # Outer border around board
    draw.rectangle([board_x - 4, board_y - 4, board_x + board_w + 4, board_y + board_h + 4], outline="#38bdf8", width=2)
    draw.text((board_x + 55, board_y - 28), "FOTOGRAFÍA REAL RP2040-ZERO", fill="#38bdf8", font=f_badge)

    # 3. Coordenadas de pines calculadas sobre la foto real
    # Left Pins (x = board_x + 12):
    p_5V  = (board_x + 12, board_y + 105)
    p_GND = (board_x + 12, board_y + 148)
    p_3V3 = (board_x + 12, board_y + 192)
    p_29  = (board_x + 12, board_y + 236)
    p_28  = (board_x + 12, board_y + 280)
    p_27  = (board_x + 12, board_y + 324)
    p_26  = (board_x + 12, board_y + 368)
    p_15  = (board_x + 12, board_y + 412)
    p_14  = (board_x + 12, board_y + 456)

    # Right Pins (x = board_x + board_w - 12):
    p_0 = (board_x + board_w - 12, board_y + 105)
    p_1 = (board_x + board_w - 12, board_y + 148)
    p_2 = (board_x + board_w - 12, board_y + 192)
    p_3 = (board_x + board_w - 12, board_y + 236)
    p_4 = (board_x + board_w - 12, board_y + 280)
    p_5 = (board_x + board_w - 12, board_y + 324)
    p_6 = (board_x + board_w - 12, board_y + 368)
    p_7 = (board_x + board_w - 12, board_y + 412)
    p_8 = (board_x + board_w - 12, board_y + 456)

    # Bottom Pins (y = board_y + board_h - 12):
    p_b14 = (board_x + 22,  board_y + board_h - 12)
    p_b13 = (board_x + 75,  board_y + board_h - 12)
    p_b12 = (board_x + 128, board_y + board_h - 12)
    p_b11 = (board_x + 181, board_y + board_h - 12)
    p_b10 = (board_x + 234, board_y + board_h - 12)
    p_b9  = (board_x + 287, board_y + board_h - 12)
    p_b8  = (board_x + 338, board_y + board_h - 12)

    # 4. Conexión de Alimentación Directa (Top-Left)
    pwr_box = [60, 160, 320, 250]
    draw.rounded_rectangle(pwr_box, radius=8, fill="#1e293b", outline="#ef4444", width=2)
    draw.text((pwr_box[0] + 15, pwr_box[1] + 12), "ALIMENTACIÓN DIRECTA 5V", fill="#ef4444", font=f_badge)
    draw.text((pwr_box[0] + 15, pwr_box[1] + 35), "Batería Li-Ion 18650 con booster\nTP4056 a 5V o Fuente Regulada", fill="#94a3b8", font=f_note)
    # Wires to 5V and GND
    draw.line([(pwr_box[2], pwr_box[1] + 30), (board_x - 30, pwr_box[1] + 30), (board_x - 30, p_5V[1]), p_5V], fill="#ef4444", width=3) # +5V Red
    draw.line([(pwr_box[2], pwr_box[1] + 60), (board_x - 45, pwr_box[1] + 60), (board_x - 45, p_GND[1]), p_GND], fill="#0f172a", width=4) # GND Black
    draw.line([(pwr_box[2], pwr_box[1] + 60), (board_x - 45, pwr_box[1] + 60), (board_x - 45, p_GND[1]), p_GND], fill="#64748b", width=2)

    # 5. Conexión MicroSD Adapter DIY (Right Side)
    sd_x, sd_y = 1180, 240
    sd_w, sd_h = 130, 200
    draw_sd_adapter(draw, (sd_x, sd_y, sd_w, sd_h))
    
    # Title SD
    draw.text((sd_x - 30, sd_y - 30), "HACK ADAPTADOR SD PASIVO", fill="#fbbf24", font=f_badge)
    draw.text((sd_x - 50, sd_y + sd_h + 10), "Soldar 6 cables directos a pistas\ndoradas traseras del adaptador plástico", fill="#94a3b8", font=f_note)
    
    # Wires from RP2040-Zero Right Side to SD
    # Pin 2 (SCK) -> SD CLK (Pad 5)
    draw.line([p_2, (sd_x - 40, p_2[1]), (sd_x - 40, sd_y + 100), (sd_x + 55, sd_y + 100), (sd_x + 55, sd_y + 32)], fill="#f97316", width=3)
    # Pin 3 (MOSI) -> SD CMD (Pad 2)
    draw.line([p_3, (sd_x - 30, p_3[1]), (sd_x - 30, sd_y + 80), (sd_x + 23, sd_y + 80), (sd_x + 23, sd_y + 32)], fill="#22c55e", width=3)
    # Pin 4 (MISO) -> SD DAT0 (Pad 7)
    draw.line([p_4, (sd_x - 20, p_4[1]), (sd_x - 20, sd_y + 120), (sd_x + 78, sd_y + 120), (sd_x + 78, sd_y + 32)], fill="#eab308", width=3)
    # Pin 5 (CS) -> SD CD/DAT3 (Pad 1)
    draw.line([p_5, (sd_x - 10, p_5[1]), (sd_x - 10, sd_y + 60), (sd_x + 12, sd_y + 60), (sd_x + 12, sd_y + 32)], fill="#38bdf8", width=3)
    
    # 3.3V to SD VDD (Pad 4) - Routed from 3V3 on Left side around the top
    draw.line([p_3V3, (board_x - 60, p_3V3[1]), (board_x - 60, board_y - 20), (sd_x + 45, board_y - 20), (sd_x + 45, sd_y + 32)], fill="#ef4444", width=3)
    draw.text((board_x - 180, p_3V3[1] - 8), "Alimentación 3.3V (¡SOLO 3.3V!)", fill="#ef4444", font=f_note)

    # 6. Conector RCA de Video Compuesto (Bottom-Right)
    rca_pos = (1280, 780)
    draw_rca_connector(draw, rca_pos)
    draw.text((rca_pos[0] - 80, rca_pos[1] + 50), "CONECTOR RCA HEMBRA", fill="#eab308", font=f_badge)
    draw.text((rca_pos[0] - 90, rca_pos[1] + 70), "Entrada Video TV / Tubo CRT (75 Ω)", fill="#94a3b8", font=f_note)

    # Node point where 560Ω and 270Ω meet
    node_rca = (1120, 780)
    
    # Resistor 560Ω from GP8 (bottom right corner: p_b8 / p_8)
    draw_resistor(draw, p_b8, (node_rca[0], p_b8[1]), "560 Ω (GP8 Sync)", ["#22c55e", "#3b82f6", "#78350f", "#eab308"])
    draw.line([(node_rca[0], p_b8[1]), node_rca], fill="#94a3b8", width=3)

    # Resistor 270Ω from GP9 (bottom edge: p_b9)
    draw_resistor(draw, p_b9, (node_rca[0], p_b9[1] + 50), "270 Ω (GP9 Video)", ["#ef4444", "#a855f7", "#78350f", "#eab308"])
    draw.line([(node_rca[0], p_b9[1] + 50), node_rca], fill="#94a3b8", width=3)

    # Line from node to RCA center pin
    draw.line([node_rca, rca_pos], fill="#eab308", width=4)
    draw.ellipse([node_rca[0]-4, node_rca[1]-4, node_rca[0]+4, node_rca[1]+4], fill="#facc15")

    # Black wire for GND to RCA outer shell
    draw.line([(board_x + 12, board_y + 148), (board_x - 75, board_y + 148), (board_x - 75, 870), (rca_pos[0], 870), (rca_pos[0], rca_pos[1] + 35)], fill="#64748b", width=3)
    draw.text((rca_pos[0] - 30, 850), "Masa GND", fill="#64748b", font=f_note)

    # 7. Si es Versión 1: Puertos USB Reciclados (Bottom-Left)
    if not is_version2:
        usb_x, usb_y = 120, 680
        draw_usb_port(draw, (usb_x, usb_y, 140, 70), "USB Teclado")
        draw.text((usb_x, usb_y - 25), "PUERTO 1: TECLADO USB", fill="#38bdf8", font=f_badge)
        draw.text((usb_x, usb_y + 78), "Conector USB-A reciclado + 27 Ω / 15 kΩ", fill="#94a3b8", font=f_note)

        draw_usb_port(draw, (usb_x, usb_y + 130, 140, 70), "USB Mouse")
        draw.text((usb_x, usb_y + 105), "PUERTO 2: RATÓN USB", fill="#38bdf8", font=f_badge)

        # Lines from GP10 & GP11 to Port 1
        draw.line([p_b10, (p_b10[0], usb_y + 20), (usb_x + 140, usb_y + 20)], fill="#22c55e", width=2) # D+ Teclado
        draw.line([p_b11, (p_b11[0], usb_y + 40), (usb_x + 140, usb_y + 40)], fill="#f97316", width=2) # D- Teclado
        draw.text((p_b10[0] - 10, usb_y + 6), "GP10 (D+)", fill="#22c55e", font=f_note)
        draw.text((p_b11[0] - 10, usb_y + 26), "GP11 (D-)", fill="#f97316", font=f_note)

        # Lines from GP12 & GP13 to Port 2
        draw.line([p_b12, (p_b12[0], usb_y + 150), (usb_x + 140, usb_y + 150)], fill="#22c55e", width=2) # D+ Mouse
        draw.line([p_b13, (p_b13[0], usb_y + 170), (usb_x + 140, usb_y + 170)], fill="#f97316", width=2) # D- Mouse
        draw.text((p_b12[0] - 10, usb_y + 136), "GP12 (D+)", fill="#22c55e", font=f_note)
        draw.text((p_b13[0] - 10, usb_y + 156), "GP13 (D-)", fill="#f97316", font=f_note)

    # 8. Si es Versión 2: Conector VGA, Switch GP0 y Opción OTG
    if is_version2:
        # VGA DE-15 Blue Connector on Left
        vga_box = (100, 420, 140, 90)
        draw_vga_connector(draw, vga_box)
        draw.text((vga_box[0], vga_box[1] - 30), "CONECTOR VGA DE-15 (DB-15) HEMBRA", fill="#38bdf8", font=f_badge)
        draw.text((vga_box[0], vga_box[1] + vga_box[3] + 12), "Monitor PC CRT / LCD (640x480 @ 60Hz)", fill="#94a3b8", font=f_note)

        # Resistor 100Ω from GP26 (Pin 26 Left) to VGA pins 1, 2, 3 (RGB)
        rgb_join = (vga_box[0] + vga_box[2] + 40, vga_box[1] + 20)
        draw_resistor(draw, p_26, rgb_join, "100 Ω (GP26 Video)", ["#78350f", "#0f172a", "#78350f", "#eab308"])
        draw.line([rgb_join, (vga_box[0] + vga_box[2], vga_box[1] + 20)], fill="#94a3b8", width=3)
        draw.text((rgb_join[0] - 40, rgb_join[1] + 10), "Pines 1, 2, 3 (RGB Unidos)", fill="#f8fafc", font=f_note)

        # Pin 27 (VSync) to Pin 14 VGA
        draw.line([p_27, (p_27[0] - 150, p_27[1]), (p_27[0] - 150, vga_box[1] + 50), (vga_box[0] + vga_box[2], vga_box[1] + 50)], fill="#38bdf8", width=3)
        draw.text((p_27[0] - 270, p_27[1] - 12), "GP27 -> Pin 14 (VSync)", fill="#38bdf8", font=f_note)

        # Pin 29 (HSync) to Pin 13 VGA
        draw.line([p_29, (p_29[0] - 120, p_29[1]), (p_29[0] - 120, vga_box[1] + 70), (vga_box[0] + vga_box[2], vga_box[1] + 70)], fill="#eab308", width=3)
        draw.text((p_29[0] - 270, p_29[1] - 12), "GP29 -> Pin 13 (HSync)", fill="#eab308", font=f_note)

        # Ground wire to VGA GND pins (5, 6, 7, 8, 10)
        draw.line([p_GND, (vga_box[0] + vga_box[2] + 15, p_GND[1]), (vga_box[0] + vga_box[2] + 15, vga_box[1] + 85), (vga_box[0] + vga_box[2], vga_box[1] + 85)], fill="#64748b", width=3)
        draw.text((vga_box[0] + 150, vga_box[1] + 75), "Masa GND (Pines 5,6,7,8,10)", fill="#64748b", font=f_note)

        # Selector Switch GP0 to GND (Top-Right)
        sw_box = [1050, 100, 1260, 175]
        draw.rounded_rectangle(sw_box, radius=8, fill="#1e293b", outline="#a855f7", width=2)
        draw.text((sw_box[0] + 15, sw_box[1] + 12), "SELECTOR VGA / RCA (SWITCH)", fill="#a855f7", font=f_badge)
        draw.text((sw_box[0] + 15, sw_box[1] + 35), "• Abierto (Sin Jumper): Modo Video Compuesto RCA\n• Cerrado a GND: Modo Monitor VGA", fill="#94a3b8", font=f_note)
        # Wire from GP0 (top-right pin) to switch
        draw.line([p_0, (sw_box[0], p_0[1])], fill="#a855f7", width=3)

        # Opción Adaptador OTG USB-C
        otg_box = [board_x + 80, 50, board_x + 280, 140]
        draw.rounded_rectangle(otg_box, radius=8, fill="#1e293b", outline="#22c55e", width=2)
        draw.text((otg_box[0] + 15, otg_box[1] + 10), "OPCIÓN ADAPTADOR OTG", fill="#22c55e", font=f_badge)
        draw.text((otg_box[0] + 15, otg_box[1] + 32), "Conectar Adaptador USB-C a USB-A OTG\n+ Hub pasivo para Teclado/Mouse\n(¡Sin soldar resistencias USB!)", fill="#94a3b8", font=f_note)
        draw.line([(otg_box[0] + 100, otg_box[3]), (otg_box[0] + 100, board_y + 10)], fill="#22c55e", width=3)

        # USB Reciclados también indicados al pie
        draw.text((100, 720), "PUERTOS USB RECICLADOS:\nConectar a GP10 (D+ Kbd), GP11 (D- Kbd),\nGP12 (D+ Mouse) y GP13 (D- Mouse) con resistencias 27 Ω", fill="#94a3b8", font=f_note)

    # Footer note
    draw.text((40, canvas_h - 40), "PiMac 2040 Hardware Reference • Desarrollado por SCHUBIGER.CL (https://schubiger.cl) • Código y Hardware Abierto MIT", fill="#64748b", font=f_note)

    return im

print("Generating Version 1 diagram...")
im_v1 = build_diagram(is_version2=False)
v1_png = os.path.join(OUTPUT_DIR_GITHUB, "pimac2040_version1_composite.png")
v1_jpg = os.path.join(OUTPUT_DIR_GITHUB, "pimac2040_version1_composite.jpg")
im_v1.save(v1_png)
im_v1.convert("RGB").save(v1_jpg, quality=95)
shutil.copy(v1_png, os.path.join(OUTPUT_DIR_ROOT, "pimac2040_version1_composite.png"))
shutil.copy(v1_jpg, os.path.join(OUTPUT_DIR_ROOT, "pimac2040_version1_composite.jpg"))
print("Saved Version 1 diagram:", os.path.getsize(v1_jpg), "bytes")

print("Generating Version 2 diagram...")
im_v2 = build_diagram(is_version2=True)
v2_png = os.path.join(OUTPUT_DIR_GITHUB, "pimac2040_version2_dual_vga_composite.png")
v2_jpg = os.path.join(OUTPUT_DIR_GITHUB, "pimac2040_version2_dual_vga_composite.jpg")
im_v2.save(v2_png)
im_v2.convert("RGB").save(v2_jpg, quality=95)
shutil.copy(v2_png, os.path.join(OUTPUT_DIR_ROOT, "pimac2040_version2_dual_vga_composite.png"))
shutil.copy(v2_jpg, os.path.join(OUTPUT_DIR_ROOT, "pimac2040_version2_dual_vga_composite.jpg"))
print("Saved Version 2 diagram:", os.path.getsize(v2_jpg), "bytes")

print("Done generating exact physical diagrams!")
