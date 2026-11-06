#!/usr/bin/env python3
"""
PiMac 2040 - Disk Image Collection Generator
Developed by SCHUBIGER.CL (https://schubiger.cl)

This script curates and builds bootable Macintosh disk images (.img / .dsk)
optimized for the RP2040-Zero Macintosh 208K emulator.
"""

import os
import shutil
import machfs
from machfs.main import Resource, make_file, parse_file

DISKS_DIR = r"c:\Antigravity\macos-rp2040\disks"
CYD_DIR = r"C:\Antigravity\CYD 2.8 MINI MP3, RADIO WEB WIFI, BLUETOOTH, SD, TOUCH\cydintosh"
REA_DIR = r"C:\Antigravity\rea\macplus-web-emulator"

def prepare_system_folder():
    """Extract and prepare a bootable System Folder from System 3.2"""
    v_sys = machfs.Volume()
    with open("System_3.2.dsk", "rb") as f:
        v_sys.read(f.read())
    with open("System_3.2.dsk", "rb") as f:
        boot1024 = f.read(1024)

    sys_fld = v_sys["System Folder"]
    sys_file = sys_fld["System"]
    rsrcs = list(parse_file(sys_file.rsrc))
    rsrcs.append(Resource(b"boot", 1, data=boot1024))
    sys_file.rsrc = make_file(rsrcs)
    return sys_fld

def build_games_pack(sys_fld):
    print("Building umac0_games_pack.img (4MB)...")
    v = machfs.Volume()
    v.name = "PiMac Games"
    v["System Folder"] = sys_fld

    # Load apps
    v_apps = machfs.Volume()
    with open(os.path.join(CYD_DIR, r"data\apps.img"), "rb") as f:
        v_apps.read(f.read())

    for app in ["Shufflepuck", "Risk", "Cannon Fodder", "Tetris DA"]:
        if app in v_apps:
            v[app] = v_apps[app]

    # Load Stunt Copter
    v_sc = machfs.Volume()
    with open("StuntCopter.dsk", "rb") as f:
        v_sc.read(f.read())
    v["StuntCopter"] = v_sc["StuntCopter--patched for any OS"]

    # Load Dark Castle
    v_dc = machfs.Volume()
    with open("DarkCastle_1_2.dsk", "rb") as f:
        v_dc.read(f.read())
    fld_dc = machfs.Folder()
    for k, item in v_dc.items():
        if k not in ["System", "Finder"]:
            fld_dc[k] = item
    v["Dark Castle"] = fld_dc

    # Load Beyond Dark Castle
    v_bdc = machfs.Volume()
    with open(os.path.join(REA_DIR, "BeyondDarkCastle.img"), "rb") as f:
        v_bdc.read(f.read())
    fld_bdc = machfs.Folder()
    for k, item in v_bdc.items():
        if k not in ["System", "Finder"]:
            fld_bdc[k] = item
    v["Beyond Dark Castle"] = fld_bdc

    data = v.write(size=4*1024*1024, bootable=True)
    out_path = os.path.join(DISKS_DIR, "umac0_games_pack.img")
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"  -> Generated {out_path} ({len(data)} bytes)")

def build_productivity_pack(sys_fld):
    print("Building umac0_productivity.img (800KB)...")
    v = machfs.Volume()
    v.name = "PiMac Office"
    v["System Folder"] = sys_fld

    # Load apps
    v_apps = machfs.Volume()
    with open(os.path.join(CYD_DIR, r"data\apps.img"), "rb") as f:
        v_apps.read(f.read())

    for app in ["MacPaint", "MacDraw", "TeachText", "Disk Copy", "Draw Tour", "woodblock"]:
        if app in v_apps:
            v[app] = v_apps[app]

    data = v.write(size=819200, bootable=True)
    out_path = os.path.join(DISKS_DIR, "umac0_productivity.img")
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"  -> Generated {out_path} ({len(data)} bytes)")

def copy_standalone_images():
    print("Copying standalone curated disks...")
    # Dark Castle
    dc_out = os.path.join(DISKS_DIR, "umac0_dark_castle.img")
    shutil.copy("DarkCastle_1_2.dsk", dc_out)
    print(f"  -> {dc_out}")

    # Beyond Dark Castle
    bdc_src = os.path.join(REA_DIR, "BeyondDarkCastle.img")
    bdc_out = os.path.join(DISKS_DIR, "umac0_beyond_dark_castle.img")
    shutil.copy(bdc_src, bdc_out)
    print(f"  -> {bdc_out}")

    # Stunt Copter
    sc_out = os.path.join(DISKS_DIR, "umac0_stunt_copter.img")
    shutil.copy("StuntCopter.dsk", sc_out)
    print(f"  -> {sc_out}")

    # System 1.1 (1984 original)
    s11_out = os.path.join(DISKS_DIR, "umac0_system11_1984.img")
    shutil.copy("System_1.1.dsk", s11_out)
    print(f"  -> {s11_out}")

    # System 3.2 Utilities
    s32_out = os.path.join(DISKS_DIR, "umac0_system32_utilities.img")
    shutil.copy("System_3.2.dsk", s32_out)
    print(f"  -> {s32_out}")

if __name__ == "__main__":
    os.makedirs(DISKS_DIR, exist_ok=True)
    sys_fld = prepare_system_folder()
    build_games_pack(sys_fld)
    build_productivity_pack(sys_fld)
    copy_standalone_images()
    print("All disk images assembled successfully!")
