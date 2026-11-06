#!/usr/bin/env python3
"""
bin2h.py - Convert a binary file (such as a Macintosh disk image) into a C header.
Cross-platform replacement for `xxd -i`.
"""

import sys
import os

def bin_to_header(input_file, output_file, empty=False):
    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    if empty or not input_file or not os.path.exists(input_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("/* Empty disc image - booting from SD card */\n")
        print(f"Generated empty disc header at '{output_file}'")
        return

    with open(input_file, 'rb') as f:
        data = f.read()

    # If file has a DiskCopy 4.2 header (84 bytes, starts with 0x00 and volume name length), strip it
    if len(data) > 84 and data[0x40:0x42] == b'\x01\x00':
        print(f"Detected DiskCopy 4.2 84-byte header in '{input_file}', stripping header...")
        data = data[84:]

    lines = []
    for i in range(0, len(data), 12):
        chunk = data[i:i+12]
        lines.append("  " + ", ".join(f"0x{b:02x}" for b in chunk) + ",")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"Converted '{input_file}' ({len(data)} bytes) to '{output_file}'")

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <input_disc.img> [output_header=incbin/umac-disc.h]")
        print("Or for SD-only mode (empty internal disk): python tools/bin2h.py --empty")
        sys.exit(1)

    if sys.argv[1] == '--empty':
        output_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join("incbin", "umac-disc.h")
        bin_to_header(None, output_file, empty=True)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else os.path.join("incbin", "umac-disc.h")
        bin_to_header(input_file, output_file)

if __name__ == '__main__':
    main()
