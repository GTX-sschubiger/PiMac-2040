#!/usr/bin/env python3
"""
PiMac 2040 - GitHub Folder Synchronizer
Developed by SCHUBIGER.CL (https://schubiger.cl)

This script synchronizes the complete source code, disk images, tools,
documentation and build scripts into the github/ distribution folder.
"""

import os
import shutil

ROOT_DIR = r"c:\Antigravity\macos-rp2040"
GITHUB_DIR = os.path.join(ROOT_DIR, "github")

def copy_tree_clean(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    def ignore_patterns(dir, files):
        ignored = []
        for f in files:
            if f in [".git", "__pycache__", ".DS_Store", "Thumbs.db"] or f.endswith(".pyc"):
                ignored.append(f)
        return ignored

    shutil.copytree(src, dst, ignore=ignore_patterns)
    print(f"  Copied {src} -> {dst}")

def main():
    print("Synchronizing PiMac 2040 repository into github/ ...")
    os.makedirs(GITHUB_DIR, exist_ok=True)

    # 1. Source code & headers
    copy_tree_clean(os.path.join(ROOT_DIR, "src"), os.path.join(GITHUB_DIR, "src"))
    copy_tree_clean(os.path.join(ROOT_DIR, "include"), os.path.join(GITHUB_DIR, "include"))
    copy_tree_clean(os.path.join(ROOT_DIR, "incbin"), os.path.join(GITHUB_DIR, "incbin"))
    copy_tree_clean(os.path.join(ROOT_DIR, "rom"), os.path.join(GITHUB_DIR, "rom"))
    copy_tree_clean(os.path.join(ROOT_DIR, "tools"), os.path.join(GITHUB_DIR, "tools"))
    copy_tree_clean(os.path.join(ROOT_DIR, "external"), os.path.join(GITHUB_DIR, "external"))

    # 2. Disk images
    copy_tree_clean(os.path.join(ROOT_DIR, "disks"), os.path.join(GITHUB_DIR, "disks"))

    # 3. Build & config files
    for fname in ["CMakeLists.txt", "pico_sdk_import.cmake", "build.bat", ".gitignore"]:
        src_file = os.path.join(ROOT_DIR, fname)
        dst_file = os.path.join(GITHUB_DIR, fname)
        if os.path.exists(src_file):
            shutil.copy2(src_file, dst_file)
            print(f"  Copied {fname} -> github/{fname}")

    print("Synchronization finished successfully!")

if __name__ == "__main__":
    main()
