#!/usr/bin/env python3
"""
Generador de Disco de Oficina y Almacenamiento para PiMac 2040
Desarrollado y mantenido por SCHUBIGER.CL (https://schubiger.cl)
Licencia MIT - Código y Hardware Abierto

Genera una imagen HFS de 20 Megabytes (Apple HD 20SC) que incluye:
- Sistema Operativo Mac OS 3.2 / Finder 5.3 con arranque booteable
- Microsoft Word 4.0a (Procesador de texto profesional)
- Microsoft Excel 2.2a (Hoja de cálculo, fórmulas, macros y gráficos)
- Microsoft Works 3.0 (Suite integrada: Texto, Base de Datos, Cálculo, Comunicaciones)
- Aldus PageMaker 2.0a (Autoedición y maquetación editorial)
- MacPaint 2.0 y MacDraw 1.9 (Dibujo artístico y vectorial/técnico)
- BBEdit Lite 3.5.1 y TeachText (Editores de texto y código)
- Herramientas: Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm
- Carpeta 'Mis Documentos' con ~10 MB de espacio libre permanente para guardar archivos
"""

import os
import sys
import shutil
import machfs
from machfs.main import Resource, make_file, parse_file

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REA_DIR = "C:/Antigravity/rea/macplus-web-emulator"
HD2_PATH = os.path.join(REA_DIR, "hd2.img")
SYSTEM_IMG_PATH = os.path.join(PROJECT_DIR, "disks", "umac0_system32_utilities.img")

DOWNLOADS_DIR = r"C:\Users\EME Chile\Downloads\PiMac2040_Disks"
OUTPUT_LOCAL = os.path.join(PROJECT_DIR, "disks", "umac0_oficina_almacenamiento_20mb.img")
OUTPUT_GITHUB = os.path.join(PROJECT_DIR, "github", "disks", "umac0_oficina_almacenamiento_20mb.img")
OUTPUT_DOWNLOADS = os.path.join(DOWNLOADS_DIR, "umac0_oficina_almacenamiento_20mb.img")

VOLUME_NAME = "PiMac Oficina"
TOTAL_SIZE = 20 * 1024 * 1024  # 20 MB

def build_office_disk():
    print(f"[*] Iniciando ensamblaje de '{VOLUME_NAME}' ({TOTAL_SIZE // (1024*1024)} MB)...")

    if not os.path.exists(SYSTEM_IMG_PATH):
        raise FileNotFoundError(f"No se encontro el archivo de sistema: {SYSTEM_IMG_PATH}")
    if not os.path.exists(HD2_PATH):
        raise FileNotFoundError(f"No se encontro el archivo de aplicaciones: {HD2_PATH}")

    # 1. Leer imagen base con System Folder
    print("[1/5] Extrayendo System Folder (System 3.2 / Finder 5.3)...")
    with open(SYSTEM_IMG_PATH, "rb") as f:
        boot1024 = f.read(1024)
        f.seek(0)
        sys_img_data = f.read()

    v_sys = machfs.Volume()
    v_sys.read(sys_img_data)
    sys_fld = v_sys["System Folder"]

    # Inyectar recurso boot 1 en System para bendicion automatica de machfs
    sys_file = sys_fld["System"]
    rsrcs = list(parse_file(sys_file.rsrc))
    rsrcs.append(Resource(b"boot", 1, data=boot1024))
    sys_file.rsrc = make_file(rsrcs)

    # 2. Leer HD2 con aplicaciones de oficina
    print("[2/5] Extrayendo aplicaciones clasicas de oficina...")
    v_hd2 = machfs.Volume()
    with open(HD2_PATH, "rb") as f:
        v_hd2.read(f.read())

    desk = v_hd2["Desktop Folder"]
    ofi = desk["Ofimatica y Aplicaciones"]
    dis = desk["Diseno y Utilidades"]
    arch = v_hd2["Archive"]

    # 3. Construir volumen HFS estructurado
    print("[3/5] Organizando carpetas del volumen HFS...")
    v_out = machfs.Volume()
    v_out.name = VOLUME_NAME
    v_out["System Folder"] = sys_fld

    # Microsoft Office
    fld_ms = machfs.Folder()
    fld_ms["Microsoft Word 4.0a"] = ofi["Microsoft Word 4.0a"]
    fld_ms["Microsoft Excel 2.2a"] = ofi["Microsoft Excel 2.2a"]
    fld_ms["Microsoft Works 3.0"] = ofi["Microsoft Works 3.0"]
    v_out["Microsoft Office"] = fld_ms

    # Autoedicion y Diseno
    fld_design = machfs.Folder()
    fld_design["Pagemaker 2.0a"] = ofi["Pagemaker 2.0a"]
    fld_design["MacPaint 2.0"] = ofi["MacPaint 2.0"]
    fld_design["MacDraw 1.9"] = ofi["MacDraw 1.9"]
    v_out["Autoedicion y Diseno"] = fld_design

    # Editores de Texto
    fld_text = machfs.Folder()
    fld_text["TeachText"] = dis["TeachText"]
    fld_text["BBEdit Lite 3.5.1"] = ofi["BBEdit Lite 3.5.1"]
    v_out["Editores de Texto"] = fld_text

    # Herramientas y Comunicacion
    fld_utils = machfs.Folder()
    fld_utils["Disk Copy 4.2"] = dis["Disk Copy 4.2"]
    fld_utils["ResEdit 2.1.3"] = dis["ResEdit 2.1.3"]
    fld_utils["Disinfectant 3.7.1"] = dis["Disinfectant 3.7.1"]
    fld_utils["StuffIt Expander"] = arch["StuffIt Expander 4.0.2"]
    fld_utils["Compact Pro"] = arch["Compact Pro 1.52"]
    fld_utils["ZTerm 1.0.1"] = ofi["ZTerm 1.0.1"]
    v_out["Herramientas y Utilidades"] = fld_utils

    # Carpeta 'Mis Documentos' con guia de uso
    fld_storage = machfs.Folder()
    readme_file = machfs.File()
    readme_file.type = b"TEXT"
    readme_file.creator = b"ttxt"
    readme_content = (
        "=================================================================\r"
        "BIENVENIDO A TU DISCO DE OFICINA Y ALMACENAMIENTO PIMAC 2040\r"
        "Desarrollado y compartido con afecto por SCHUBIGER.CL\r"
        "Web oficial: https://schubiger.cl\r"
        "=================================================================\r\r"
        "Este disco cuenta con un volumen HFS de 20 Megabytes y dispone de\r"
        "mas de 10 Megabytes completamente libres para guardar tus documentos,\r"
        "hojas de calculo, bases de datos, dibujos y notas personales.\r\r"
        "APLICACIONES DISPONIBLES EN ESTE DISCO:\r"
        "---------------------------------------\r"
        "1. Microsoft Office:\r"
        "   - Microsoft Word 4.0a: Redaccion de cartas, libros, contratos e informes.\r"
        "   - Microsoft Excel 2.2a: Hojas de calculo, balances financieros, macros y graficos.\r"
        "   - Microsoft Works 3.0: Suite integrada con procesador de textos, base de datos\r"
        "     relacional, hoja de calculo y comunicaciones.\r\r"
        "2. Autoedicion y Diseno Grafico:\r"
        "   - Aldus PageMaker 2.0a: Maquetacion editorial, boletines, folletos y revistas.\r"
        "   - MacPaint 2.0: Creacion y edicion de imagenes de mapa de bits (bitmaps).\r"
        "   - MacDraw 1.9: Planos tecnicos, diagramas vectoriales y esquemas.\r\r"
        "3. Editores de Texto y Notas:\r"
        "   - TeachText: Lector y editor rapido de textos y archivos ReadMe.\r"
        "   - BBEdit Lite 3.5.1: Potente editor para programacion y textos avanzados.\r\r"
        "4. Herramientas y Utilidades:\r"
        "   - Disk Copy 4.2: Gestion de imagenes de disquete.\r"
        "   - ResEdit 2.1.3: Editor profundo de recursos Macintosh.\r"
        "   - Disinfectant 3.7.1: Antivirus clasico para proteccion del sistema.\r"
        "   - StuffIt Expander y Compact Pro: Descompresion y compresion de archivos.\r"
        "   - ZTerm 1.0.1: Emulador de terminal y comunicaciones serie/modem.\r\r"
        "COMO GUARDAR TUS ARCHIVOS DE MANERA SEGURA:\r"
        "-------------------------------------------\r"
        "Cada vez que utilices 'Guardar como...' (Save As...) en cualquier programa,\r"
        "puedes guardar tus archivos dentro de esta carpeta 'Mis Documentos' o\r"
        "en cualquier parte del disco 'PiMac Oficina'.\r\r"
        "El emulador PiMac 2040 sincroniza de inmediato cada escritura en tu tarjeta\r"
        "MicroSD fisica, por lo que tus archivos permaneceran grabados aun cuando\r"
        "apagues o reinicies el dispositivo.\r\r"
        "Disfruta de la experiencia clasica de productividad Mac!\r"
    ).encode("mac_roman")
    readme_file.data = readme_content
    fld_storage["LEEME - Como Guardar.txt"] = readme_file
    v_out["Mis Documentos"] = fld_storage

    # 4. Generar imagen HFS binaria booteable
    print("[4/5] Escribiendo estructura HFS y bendiciendo bloques de arranque...")
    disk_data = v_out.write(size=TOTAL_SIZE, bootable=True)

    print(f"[*] Tamano generado: {len(disk_data):,} bytes ({len(disk_data) / (1024*1024):.2f} MB)")
    print(f"[*] Magia de arranque (Boot block offset 0): {disk_data[:2]}")

    # 5. Guardar copias
    print("[5/5] Distribuyendo imagen de disco...")
    os.makedirs(os.path.dirname(OUTPUT_LOCAL), exist_ok=True)
    with open(OUTPUT_LOCAL, "wb") as f:
        f.write(disk_data)
    print(f" -> Guardado: {OUTPUT_LOCAL}")

    os.makedirs(os.path.dirname(OUTPUT_GITHUB), exist_ok=True)
    with open(OUTPUT_GITHUB, "wb") as f:
        f.write(disk_data)
    print(f" -> Guardado: {OUTPUT_GITHUB}")

    if os.path.exists(DOWNLOADS_DIR):
        with open(OUTPUT_DOWNLOADS, "wb") as f:
            f.write(disk_data)
        print(f" -> Guardado: {OUTPUT_DOWNLOADS}")

    print("\n[OK] Disco de Oficina y Almacenamiento generado exitosamente.")

if __name__ == "__main__":
    build_office_disk()
