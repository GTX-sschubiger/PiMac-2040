# Disk Images Collection for PiMac 2040 (Macintosh 208K)
### Curated and Developed by **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="README.md">🇪🇸 Español</a> |
  <a href="README_EN.md"><strong>🇬🇧 English</strong></a> |
  <a href="README_PT.md">🇵🇹 Português</a> |
  <a href="README_DE.md">🇩🇪 Deutsch</a> |
  <a href="README_ZH.md">🇨🇳 中文</a> |
  <a href="README_FR.md">🇫🇷 Français</a>
</p>


This directory contains a complete library of ready-to-boot disk images with persistent read/write support, running directly from a MicroSD card on the **RP2040-Zero**.

---

## 💽 Available Disk Images Catalog

| Filename | Size | Operating System | Type | Featured Software & Highlights |
| :--- | :---: | :---: | :---: | :--- |
| **`umac0_oficina_almacenamiento_20mb.img`** | **20 MB** | System 3.2 / Finder 5.3 | HFS Office & Storage | **Real Productivity & Work:**<br>• **Microsoft Office Suite:** Word 4.0a, Excel 2.2a, Works 3.0 (integrated word processing, spreadsheets, and databases).<br>• **Publishing & Design:** Aldus PageMaker 2.0a, MacPaint 2.0, MacDraw 1.9.<br>• **Text Editors:** TeachText, BBEdit Lite 3.5.1.<br>• **System Utilities:** Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm 1.0.1.<br>• **📁 My Documents:** Dedicated folder with **over 10 MB of permanent free space** to save your files on the MicroSD. |
| **`umac0_aventura_juegos_15mb.img`** | **15 MB** | System 3.2 / Finder 5.3 | HFS Adventure & Games | **Top Retro Adventure & Strategy:**<br>• **Prince of Persia:** Jordan Mechner's legendary action-platformer masterpiece with sword duels (optimized black & white build).<br>• **SimCity 1.11:** Will Wright's classic city-building simulation with scenarios and sound effects.<br>• **Tetris:** Official Spectrum HoloByte edition with classic music themes and sound effects.<br>• **Silicon Beach Classics:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter v1.x/2.0.<br>• **Arcade & Board Games:** Shufflepuck Café, Risk (World Strategy), Cannon Fodder, Lode Runner, Billiard Parlour.<br>• **📁 My Savegames:** Over 8 MB free to save Prince of Persia progress, SimCity cities, and high scores. |
| **`umac0_master_10mb.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS All-in-One | **Balanced All-Rounder:** Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA, MacPaint, MacDraw, TeachText, Disk Copy, Utilities. |
| **`umac0.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS/MFS Classic | **Original Classic Pack:** MacPaint 1.3, MacWrite 4.5, MacDraw, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma. |
| **`umac0_games_pack.img`** | 4 MB | System 3.2 / Finder 5.3 | HFS Arcade Pack | **Quick Gaming Disk:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA. |
| **`umac0_productivity.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Productivity | **Essential Work Tools:** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock. |
| **`umac0_dark_castle.img`** | 800 KB | Standalone System | HFS Standalone Game | **Dark Castle v1.2:** Bootable standalone version of the legendary platformer. |
| **`umac0_beyond_dark_castle.img`** | 800 KB | Standalone System | HFS Standalone Game | **Beyond Dark Castle:** Acclaimed sequel with jetpack, bombs, and secret chambers. |
| **`umac0_stunt_copter.img`** | 800 KB | Standalone System | HFS Standalone Game | **Stunt Copter:** Classic Duane Blehm physics skill game (v1.0 & v2.0). |
| **`umac0_system11_1984.img`** | 400 KB | System 1.1 / Finder 1.1g | MFS Historical 1984 | **Macintosh 128K Original:** The historical launch software shown by Steve Jobs on January 24, 1984. |
| **`umac0_system32_utilities.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Tools | **Apple Official Utilities:** Font/DA Mover, vintage fonts (Chicago, Geneva, Monaco, San Francisco), and disk tools. |

---

## 🚀 How to Use and Swap Disks on the MicroSD Card

The **PiMac 2040** firmware searches the root directory of your MicroSD card for the file named **`umac0.img`**.

### Usage Options:

### Option 1: All-in-One Master Disk (Recommended)
Copy `umac0_oficina_almacenamiento_20mb.img` or `umac0_master_10mb.img` to your MicroSD card and rename it to **`umac0.img`**:
* You will have plenty of storage with all office applications, creative tools, and games organized in folders with full read and write support.

### Option 2: Keep Multiple Disks on the Card and Select the Active One
You can store all image files on your MicroSD card:
* `umac0.img` (the active disk that boots by default)
* `office.img`
* `games.img`
* `darkcastle.img`
* `system1984.img`

Whenever you want to switch disks, plug the MicroSD into your computer or smartphone and simply rename the image you want to boot to **`umac0.img`**.

---

## 💾 Data Persistence (Read / Write Support)
Unlike static embedded ROMs in microcontrollers, running these disks from the MicroSD card on the RP2040-Zero provides real persistence:
* **Save documents** in MacWrite or illustrations in MacPaint.
* **Save game progress and high scores** in Prince of Persia, SimCity, Dark Castle, Stunt Copter, and Shufflepuck Café.
* **Configure Desk Accessories** and Control Panel settings; changes remain saved across reboots!
