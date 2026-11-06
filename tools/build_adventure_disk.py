#!/usr/bin/env python3
"""
Generador de Disco de Aventura y Videojuegos Top para PiMac 2040
Desarrollado y mantenido por SCHUBIGER.CL (https://schubiger.cl)
Licencia MIT - Código y Hardware Abierto

Genera una imagen HFS booteable de 15 Megabytes que incluye:
- Sistema Operativo Mac OS 3.2 / Finder 5.3 con arranque booteable
- Prince of Persia (Jordan Mechner / Brøderbund, versión clásica completa con gráficos BW)
- SimCity 1.11 (Will Wright / Maxis, con escenarios y editor de ciudades)
- Tetris Oficial (Spectrum HoloByte, con versión Desk Accessory y efectos de sonido)
- Dark Castle y Beyond Dark Castle (Silicon Beach Software)
- Stunt Copter (Duane Blehm)
- Shufflepuck Café (Air Hockey arcade)
- Risk y Cannon Fodder
- Carpeta 'Mis Partidas Guardadas' con ~9 MB libres para salvar progresos y récords
"""

import os
import sys
import shutil
import machfs
from machfs.main import Resource, make_file, parse_file

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REA_DIR = "C:/Antigravity/rea/macplus-web-emulator"

POP_IMG_PATH = os.path.join(REA_DIR, "PrinceOfPersia.img")
SIMCITY_IMG_PATH = os.path.join(REA_DIR, "SimCity.img")
TETRIS_IMG_PATH = os.path.join(REA_DIR, "Tetris.img")
MASTER_IMG_PATH = os.path.join(PROJECT_DIR, "disks", "umac0_master_10mb.img")
SYSTEM_IMG_PATH = os.path.join(PROJECT_DIR, "disks", "umac0_system32_utilities.img")

DOWNLOADS_DIR = r"C:\Users\EME Chile\Downloads\PiMac2040_Disks"
OUTPUT_LOCAL = os.path.join(PROJECT_DIR, "disks", "umac0_aventura_juegos_15mb.img")
OUTPUT_GITHUB = os.path.join(PROJECT_DIR, "github", "disks", "umac0_aventura_juegos_15mb.img")
OUTPUT_DOWNLOADS = os.path.join(DOWNLOADS_DIR, "umac0_aventura_juegos_15mb.img")

VOLUME_NAME = "PiMac Aventura"
TOTAL_SIZE = 15 * 1024 * 1024  # 15 MB

def build_adventure_disk():
    print(f"[*] Iniciando ensamblaje de '{VOLUME_NAME}' ({TOTAL_SIZE // (1024*1024)} MB)...")

    for path, desc in [(SYSTEM_IMG_PATH, "Sistema"), (POP_IMG_PATH, "Prince of Persia"),
                       (SIMCITY_IMG_PATH, "SimCity"), (TETRIS_IMG_PATH, "Tetris"),
                       (MASTER_IMG_PATH, "Master Juegos")]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"No se encontro el archivo de {desc}: {path}")

    # 1. System Folder booteable
    print("[1/5] Extrayendo System Folder con bendicion de arranque...")
    with open(SYSTEM_IMG_PATH, "rb") as f:
        boot1024 = f.read(1024)
        f.seek(0)
        sys_data = f.read()

    v_sys = machfs.Volume()
    v_sys.read(sys_data)
    sys_fld = v_sys["System Folder"]

    sys_file = sys_fld["System"]
    rsrcs = list(parse_file(sys_file.rsrc))
    rsrcs.append(Resource(b"boot", 1, data=boot1024))
    sys_file.rsrc = make_file(rsrcs)

    # 2. Prince of Persia
    print("[2/5] Cargando Prince of Persia...")
    v_pop = machfs.Volume()
    with open(POP_IMG_PATH, "rb") as f:
        v_pop.read(f.read())

    # 3. SimCity & Tetris
    print("[3/5] Cargando SimCity y Tetris...")
    v_sc = machfs.Volume()
    with open(SIMCITY_IMG_PATH, "rb") as f:
        v_sc.read(f.read())
    fld_sc = machfs.Folder()
    fld_sc["SimCity 1.11"] = v_sc["SimCity1.11"]
    fld_sc["scenario"] = v_sc["scenario"]

    v_tet = machfs.Volume()
    with open(TETRIS_IMG_PATH, "rb") as f:
        v_tet.read(f.read())

    # 4. Master Arcade Games
    print("[4/5] Cargando clasicos de accion y arcade...")
    v_m = machfs.Volume()
    with open(MASTER_IMG_PATH, "rb") as f:
        v_m.read(f.read())

    fld_arcade = machfs.Folder()
    fld_arcade["Dark Castle"] = v_m["Dark Castle"]
    fld_arcade["Beyond Dark Castle"] = v_m["Beyond Dark Castle"]
    fld_arcade["StuntCopter"] = v_m["StuntCopter"]
    fld_arcade["Shufflepuck Cafe"] = v_m["Shufflepuck"]
    fld_arcade["Risk"] = v_m["Risk"]
    fld_arcade["Cannon Fodder"] = v_m["Cannon Fodder"]

    # 5. Estructurar volumen final
    v_out = machfs.Volume()
    v_out.name = VOLUME_NAME
    v_out["System Folder"] = sys_fld
    v_out["Prince of Persia"] = v_pop["Prince of Persia"]
    v_out["SimCity"] = fld_sc
    v_out["Tetris"] = v_tet["Tetris"]
    v_out["Clasicos de Accion"] = fld_arcade

    # Carpeta para guardar partidas
    fld_saves = machfs.Folder()
    readme = machfs.File()
    readme.type = b"TEXT"
    readme.creator = b"ttxt"
    readme.data = (
        "=================================================================\r"
        "PIMAC 2040 - DISCO DE AVENTURA, ACCION Y ESTRATEGIA\r"
        "Desarrollado y compartido con la comunidad por SCHUBIGER.CL\r"
        "Web oficial: https://schubiger.cl\r"
        "=================================================================\r\r"
        "Este disco cuenta con un volumen HFS de 15 Megabytes y dispone de\r"
        "mas de 8 Megabytes completamente libres para guardar tus avances.\r\r"
        "JUEGOS INCLUIDOS EN ESTE DISCO:\r"
        "--------------------------------\r"
        "1. Prince of Persia (Jordan Mechner / Broderbund):\r"
        "   - La aclamada odisea de plataformas, saltos de precision, trampas\r"
        "     mortales y duelos a espada contra los guardias del Visir Jaffar.\r"
        "   - Totalmente optimizado para pantalla monocroma (carga Persia(BW)).\r\r"
        "2. SimCity 1.11 (Will Wright / Maxis):\r"
        "   - Construye, zonifica y gestiona tu propia metropoli con carreteras,\r"
        "     red electrica, impuestos, policias, bomberos y desastres naturales.\r"
        "   - Incluye el paquete de escenarios historicos.\r\r"
        "3. Tetris (Spectrum HoloByte):\r"
        "   - El legendario puzzle ruso con musica, efectos de sonido oficiales\r"
        "     y version Desk Accessory para jugar desde cualquier aplicacion.\r\r"
        "4. Clasicos de Accion y Arcade:\r"
        "   - Dark Castle y Beyond Dark Castle (Plataformas y accion pura).\r"
        "   - Stunt Copter (Acrobacias y fisicas aereas de Duane Blehm).\r"
        "   - Shufflepuck Cafe (Air Hockey futurista de gran precision).\r"
        "   - Risk (Estrategia y conquista mundial).\r"
        "   - Cannon Fodder (Accion tactica militar clasica).\r\r"
        "PERSISTENCIA Y GUARDADO:\r"
        "------------------------\r"
        "Puedes guardar tus ciudades de SimCity ('Save City...'), tus avances\r"
        "en Prince of Persia y tus records en esta carpeta 'Mis Partidas Guardadas'.\r"
        "El PiMac 2040 escribe directamente en la tarjeta MicroSD fisica.\r"
    ).encode("mac_roman")
    fld_saves["LEEME - Partidas.txt"] = readme
    v_out["Mis Partidas Guardadas"] = fld_saves

    print(f"[*] Escribiendo disco HFS booteable ({TOTAL_SIZE // (1024*1024)} MB)...")
    disk_data = v_out.write(size=TOTAL_SIZE, bootable=True)

    print(f"[*] Tamano generado: {len(disk_data):,} bytes ({len(disk_data) / (1024*1024):.2f} MB)")
    print(f"[*] Magia de arranque (Boot block offset 0): {disk_data[:2]}")

    # Guardar en las rutas correspondientes
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

    print("\n[OK] Disco de Aventura y Videojuegos Top generado exitosamente.")

if __name__ == "__main__":
    build_adventure_disk()
