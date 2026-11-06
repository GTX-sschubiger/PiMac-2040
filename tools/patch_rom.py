#!/usr/bin/env python3
"""
patch_rom.py - Patch Macintosh Plus v3 ROM for umac / PiMac 2040 on RP2040.

Applies:
1. Checksum bypass patch
2. Paravirtualized .Sony disk driver patch
3. Custom memory size patch (Mac 208K)
4. Exports patched rom.bin and generates incbin/umac-rom.h
"""

import os
import sys
import struct
import zlib

ROM_PLUSv3_CHECKSUM = 0x4d1f8172
ROM_PLUSv3_SONYDRV  = 0x17d30
PV_SONY_ADDR        = 0x00580000
M68K_INST_NOP       = 0x4e71

def load_sony_driver():
    sonydrv_header = os.path.join(os.path.dirname(__file__), '..', 'external', 'umac', 'include', 'sonydrv.h')
    if not os.path.exists(sonydrv_header):
        raise FileNotFoundError(f"sonydrv.h not found at {sonydrv_header}")
    with open(sonydrv_header, 'r', encoding='utf-8') as f:
        text = f.read()
    # Parse hex bytes
    bytes_list = []
    for token in text.replace(',', ' ').split():
        token = token.strip()
        if token.startswith('0x') or token.startswith('0X'):
            bytes_list.append(int(token, 16))
    return bytearray(bytes_list)

def patch_rom(rom_data, memsize_kb=208):
    if len(rom_data) != 131072:
        print(f"Warning: ROM file size is {len(rom_data)} bytes (expected 131072 bytes). Proceeding anyway...")

    crc = zlib.crc32(rom_data) & 0xffffffff
    print(f"Input ROM CRC32: 0x{crc:08x}")
    if crc != ROM_PLUSv3_CHECKSUM:
        print(f"Note: Standard Mac Plus v3 checksum is 0x{ROM_PLUSv3_CHECKSUM:08x}. Checksum differs, but applying patches...")

    patched = bytearray(rom_data)

    def write16(offset, val):
        patched[offset] = (val >> 8) & 0xff
        patched[offset + 1] = val & 0xff

    def write32(offset, val):
        patched[offset] = (val >> 24) & 0xff
        patched[offset + 1] = (val >> 16) & 0xff
        patched[offset + 2] = (val >> 8) & 0xff
        patched[offset + 3] = val & 0xff

    # 1. Disable checksum check
    write16(0xd92, 0xb381)  # eor.l d1, d1
    print("  [+] Checksum verification bypassed at 0x0d92")

    # 2. Inject .Sony floppy driver
    sony_driver = load_sony_driver()
    patched[ROM_PLUSv3_SONYDRV:ROM_PLUSv3_SONYDRV + len(sony_driver)] = sony_driver
    write32(ROM_PLUSv3_SONYDRV + len(sony_driver) - 4, PV_SONY_ADDR)
    print(f"  [+] Injected paravirtualized .Sony driver ({len(sony_driver)} bytes) at 0x{ROM_PLUSv3_SONYDRV:x}")

    # 3. Patch memory size for Mac 208K
    ram_size = memsize_kb * 1024
    for i in range(0x376, 0x37e, 2):
        write16(i, M68K_INST_NOP)
    write16(0x376, 0x2a7c)  # moveal #RAM_SIZE, A5
    write16(0x378, (ram_size >> 16) & 0xffff)
    write16(0x37a, ram_size & 0xffff)
    write16(0x132, 0x6000)  # bra (was beq)
    print(f"  [+] Configured RAM probe override to {memsize_kb} KB (0x{ram_size:08x}) at 0x0376")

    return bytes(patched)

def bin_to_c_header(data, array_name="umac_rom"):
    lines = []
    for i in range(0, len(data), 12):
        chunk = data[i:i+12]
        lines.append("  " + ", ".join(f"0x{b:02x}" for b in chunk) + ",")
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <path_to_macplus_v3.rom> [memsize_kb=208] [output_bin=rom.bin]")
        print("Example: python tools/patch_rom.py '4D1F8172 - MacPlus v3.ROM' 208 rom.bin")
        sys.exit(1)

    rom_path = sys.argv[1]
    memsize = int(sys.argv[2]) if len(sys.argv) > 2 else 208
    out_bin = sys.argv[3] if len(sys.argv) > 3 else "rom.bin"

    if not os.path.exists(rom_path):
        print(f"Error: ROM file not found: {rom_path}")
        sys.exit(1)

    with open(rom_path, 'rb') as f:
        raw_rom = f.read()

    print(f"Patching '{rom_path}' for Mac {memsize}K...")
    patched = patch_rom(raw_rom, memsize)

    with open(out_bin, 'wb') as f:
        f.write(patched)
    print(f"Saved patched ROM to '{out_bin}' ({len(patched)} bytes)")

    # Ensure incbin folder exists
    incbin_dir = os.path.join(os.path.dirname(__file__), '..', 'incbin')
    os.makedirs(incbin_dir, exist_ok=True)
    header_path = os.path.join(incbin_dir, 'umac-rom.h')
    with open(header_path, 'w', encoding='utf-8') as f:
        f.write(bin_to_c_header(patched, "umac_rom"))
    print(f"Generated C header at '{header_path}'")

if __name__ == '__main__':
    main()
