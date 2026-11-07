# PiMac 2040 (Macintosh 208K) – Official Installation & Hardware Guide
### Open Source Software & Hardware Project by [SCHUBIGER.CL](https://schubiger.cl)
### MIT License – Free to Use, Modify, and Share

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="RELEASE_README.md">🇪🇸 Español</a> |
  <a href="RELEASE_README_EN.md"><strong>🇬🇧 English</strong></a> |
  <a href="RELEASE_README_PT.md">🇵🇹 Português</a> |
  <a href="RELEASE_README_DE.md">🇩🇪 Deutsch</a> |
  <a href="RELEASE_README_ZH.md">🇨🇳 中文</a> |
  <a href="RELEASE_README_FR.md">🇫🇷 Français</a>
</p>


Welcome to **PiMac 2040**! This guide is written in clear, simple, and practical language so anyone — even with zero microcontroller background — can flash the system onto an **RP2040** board, wire the circuit in minutes, and relive the complete retro experience of an iconic 1984 Apple Macintosh with mouse, keyboard, MicroSD storage, and video output for retro TVs or modern PC monitors.

---

## ⚡ 1. Quick System Installation on the RP2040 (In 3 Steps)

You do not need to install complicated software or compile code from source. The firmware is pre-built and ready to flash via the file **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**:

```text
  [ .UF2 File ]       ------------------------->  [ RPI-RP2 Drive ]   ---> Flashed!
  (PiMac 2040 Firmware)        Drag and Drop             (RP2040 in Boot Mode)      (Reboots in 2 sec)
```

1. **Connect in Boot Mode:** Grab your **Waveshare / Tenstar Robot RP2040-Zero** (or Raspberry Pi Pico) board. Press and hold down the white **BOOT** (or BOOTSEL) button and, while holding it, plug the USB-C cable into your computer. Then release the button.
2. **Drive Appearance:** A new mass storage volume named **`RPI-RP2`** will automatically mount on your computer (just like plugging in a standard USB thumb drive).
3. **Copy the File:** Drag and drop into the `RPI-RP2` drive the file:
   👉 **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**
4. **Done!** Within two seconds the board's LED will flash, the drive will automatically unmount, and PiMac 2040 will be permanently installed in the microcontroller's Flash memory.

---

## 💾 2. Prepare the MicroSD Card with Disks & Apps

1. Take any MicroSD card (from 256 MB up to 32 GB).
2. Connect it to your PC and format it with **FAT32** (Quick Format).
3. Open the **`disks/`** directory and choose the disk image you want to use:
   * **`umac0_oficina_almacenamiento_20mb.img`:** Complete Office Suite (Microsoft Word 4.0, Excel 2.2, Works 3.0, PageMaker 2.0, MacPaint, MacDraw) with over 10 MB free space in the *My Documents* folder for persistent work.
   * **`umac0_aventura_juegos_15mb.img`:** Adventure & Strategy Pack (Prince of Persia, SimCity 1.11, official Tetris, Dark Castle, Stunt Copter, Shufflepuck Café) with over 8 MB free space for persistent game saves.
   * **`umac0_master_10mb.img`:** Balanced all-in-one disk image with games, paint, and system utilities.
4. **Copy your chosen image file to the root of the MicroSD card** and rename it exactly to:
   👉 **`umac0.img`**
5. Insert the MicroSD card into your PiMac 2040 card reader.

---

## 🛠️ 3. The 2 Hardware Versions: Which One to Choose?

PiMac 2040 features a **smart dual video engine** that natively drives vintage CRT televisions as well as standard computer monitors. You can build either of these two versions:

```text
+-------------------------------------------------------------------------------------------------+
|                                    VERSION COMPARISON                                           |
+-------------------------------------------------------------------------------------------------+
| FEATURE                        | VERSION 1: COMPOSITE VIDEO ONLY | VERSION 2: DUAL VGA + COMP.  |
+--------------------------------+---------------------------------+------------------------------+
| Compatible Display             | Retro CRT TV or RCA AV monitor  | CRT TV + VGA PC Monitor      |
| Video Connectors               | 1x Female RCA Jack              | 1x RCA Female + 1x VGA DE-15 |
| Assembly Complexity            | Ultra-simple (only 2 resistors) | Moderate (3 resistors + VGA) |
| Display Mode Switching         | Automatic                       | SPDT Switch or Jumper (GP0)  |
| MicroSD Read / Write           | Yes                             | Yes                          |
| USB Keyboard & Mouse           | Yes                             | Yes                          |
| Total Component BOM Cost       | Ultra-low (~$4 to $6 USD)       | Budget-friendly (~$6 to $8)  |
+--------------------------------+---------------------------------+------------------------------+
```

---

## 📺 VERSION 1: Simple / Budget Build (Composite Video Only)

[![PiMac 2040 Version 1 Composite Video Assembly](assets/pimac2040_version1_composite.jpg)](assets/pimac2040_version1_composite.jpg)
*Real hardware build of Version 1: Composite RCA connection with 560 Ω and 270 Ω resistor divider, MicroSD SPI adapter hack, and USB ports.*

### How Does It Work?
This version is designed to connect PiMac 2040 directly to any retro CRT television tube, modern LCD TV with an analog yellow AV/RCA input, or composite video monitor.

The RP2040 microcontroller natively synthesizes a monochrome standard **NTSC 480i** analog video signal. By passing the sync and pixel GPIO lines (GP8 and GP9) through two simple axial resistors, they digitally combine into the precise 1.0V peak-to-peak signal at 75 Ω impedance expected by television composite video inputs.

### Composite Video Wiring Diagram:
```text
   RP2040-Zero (Pins)                            Yellow Female Panel-Mount RCA Jack
  +--------------------+                         +----------------------------------+
  |                    |      560 Ω (Green-Blue-Brown)                              |
  |  GP8 (Sync)        +-----[1/4W Resistor]-------+                                |
  |                    |                           |                                |
  |                    |      270 Ω (Red-Violet-Brown)                              |
  |  GP9 (Video)       +-----[1/4W Resistor]-------+----> Center Pin (Signal Hot)   |
  |                    |                                                            |
  |  GND (Ground)      +--------------------------------> Outer Metal Shield / Lug  |
  +--------------------+                         +----------------------------------+
```

### Component Shopping List (Exact Technical Names):
1. **1x Microcontroller Board:** **Waveshare RP2040-Zero** (or Tenstar Robot RP2040-Zero).
2. **1x Panel-Mount Female RCA Chassis Jack:** Yellow insulator (*RCA Female Jack Panel Mount Connector*).
3. **1x 560 Ω (Ohm) Resistor:** Metal or carbon film, 1/4W or 1/8W, 5% tolerance (Color bands: Green - Blue - Brown - Gold).
4. **1x 270 Ω (Ohm) Resistor:** Metal or carbon film, 1/4W or 1/8W, 5% tolerance (Color bands: Red - Violet/Purple - Brown - Gold).
5. **1x Passive MicroSD to SD Adapter Sleeve** (the standard black plastic adapter often bundled with MicroSD cards) or 1x 3.3V MicroSD SPI breakout board.
6. **1x USB-C Male to USB-A Female OTG Adapter** (to connect USB keyboard and mouse).

---

## 🖥️ VERSION 2: Complete Dual Build (Composite Video + VGA Monitor)

[![PiMac 2040 Version 2 Dual VGA and Composite Assembly](assets/pimac2040_version2_dual_vga_composite.jpg)](assets/pimac2040_version2_dual_vga_composite.jpg)
*Real hardware build of Version 2: Complete dual video build with DE-15 VGA port (100 Ω resistor), yellow RCA jack, SPDT video switch, and MicroSD SPI.*

### How Does the Smart Dual Video Engine Work?
The firmware inspects the logic level of **GP0** during startup:
* **Booting with GP0 floating (disconnected):** PiMac 2040 boots into **Composite Video Mode**, transmitting NTSC at 15.734 kHz through the RCA jack (ideal for CRT TVs).
* **Booting with GP0 grounded (pulled to GND):** PiMac 2040 switches into **Standard VGA Mode**, outputting 640x480 at 60 Hz (31.468 kHz) through the DE-15 connector (ideal for PC monitors).

Both connectors can be soldered permanently to your board simultaneously. A simple slide switch lets you choose between your desk monitor and your living room CRT TV!

### Dual Connection Wiring Diagram (VGA + Composite):
```text
   RP2040-Zero (Pins)                            Female DE-15 / DB-15 VGA Connector
  +--------------------+                         +-----------------------------------+
  |  GP26 (Video)      +-----[ 100 Ω (1/4W) ]----+----> Pins 1, 2, 3 (Red, Green, Blue tied together)
  |  GP27 (VSync)      +-------------------------> Pin 14 (Vertical Sync)
  |  GP29 (HSync)      +-------------------------> Pin 13 (Horizontal Sync)
  |  GND (Ground)      +-------------------------> Pins 5, 6, 7, 8, 10 (Video Grounds)
  +--------------------+                         +-----------------------------------+

   VIDEO DISPLAY SELECTOR:
  +--------------------+                         +-----------------------------------+
  |  GP0               +----> [ SPDT Switch ] ---> GND (Ground)
  |                    |      Open: Boots into Composite Video (CRT TV)
  |                    |      Closed: Boots into VGA (PC Monitor)
  +--------------------+                         +-----------------------------------+

   COMPOSITE VIDEO RCA (Simultaneous):
  +--------------------+                         +-----------------------------------+
  |  GP8 (Sync)        +-----[ 560 Ω (1/4W) ]----+
  |  GP9 (Video)       +-----[ 270 Ω (1/4W) ]----+----> Center Pin of RCA Jack
  |  GND (Ground)      +------------------------------> Outer Shield of RCA Jack
  +--------------------+                         +-----------------------------------+
```

### Additional Components for Version 2:
1. **Everything from Version 1** (RP2040-Zero, RCA jack, 560 Ω and 270 Ω resistors, MicroSD, USB).
2. **1x High-Density DE-15 / DB-15 Female VGA Chassis Connector:** 15 pins across 3 rows (*VGA DB15 Female 3-Row D-Sub Connector*).
3. **1x 100 Ω (Ohm) Resistor:** Metal or carbon film, 1/4W or 1/8W (Color bands: Brown - Black - Brown - Gold).
4. **1x Miniature SPDT Slide Switch** or 2-pin jumper header (*SPDT Mini Slide Switch 3 Pin* or *2.54mm Jumper Cap*).

---

## 💾 4. MicroSD Card SPI Connection

You can use a dedicated 3.3V MicroSD breakout or solder 6 thin AWG 30 wires directly to the rear gold fingers of a **passive MicroSD-to-SD adapter sleeve**:

```text
       RP2040-Zero                               Passive SD Adapter (Rear Contacts)
   +-----------------------+                    +------------------------------------+
   |   GP5 (CS)            +------------------->| Pad 1 (CD/DAT3)                    |
   |   GP3 (MOSI)          +------------------->| Pad 2 (CMD / MOSI)                 |
   |   GND                 +------------------->| Pad 3 (VSS1 / Ground)              |
   |   3V3 (3.3 Volts)     +------------------->| Pad 4 (VDD)  ⚠️ CRITICAL: 3.3V ONLY!|
   |   GP2 (SCK)           +------------------->| Pad 5 (CLK / Clock)                |
   |   GND                 +------------------->| Pad 6 (VSS2 / Ground)              |
   |   GP4 (MISO)          +------------------->| Pad 7 (DAT0 / MISO)                |
   +-----------------------+                    +------------------------------------+
```

> [!CAUTION]
> Power the MicroSD card **strictly from the 3V3 (3.3V) pin** on the RP2040-Zero board. **NEVER** connect it to the 5V rail or you will permanently damage your memory card!

---

## 🖱️ 5. USB Keyboard & Mouse Connection

PiMac 2040 features a hardware-assisted (PIO) **USB Host controller**:

```text
       RP2040-Zero                               Dual Recycled USB-A Female Jacks
   +-----------------------+                    +-------------------------------------+
   |   5V (VBUS)           +------------------->| Pin 1 (+5V USB Power) [Both Ports]  |
   |                       |                    +-------------------------------------+
   |                       |                    | PORT 1 (USB KEYBOARD):              |
   |   GP10                +----[ 27 Ω ]--------+ Pin 3: D+ (Data Positive)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP11                +----[ 27 Ω ]--------+ Pin 2: D- (Data Negative)           |
   |                       |          |         +-------------------------------------+
   |                       |       [ 15 kΩ ]    | PORT 2 (USB MOUSE):                 |
   |   GP12                +----[ 27 Ω ]--------+ Pin 3: D+ (Data Positive)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP13                +----[ 27 Ω ]--------+ Pin 2: D- (Data Negative)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GND (Ground)        +----------+---------+ Pin 4: GND (USB Ground) [Both Ports]|
   +-----------------------+                    +-------------------------------------+
```

* **Peripheral Compatibility:** Works out of the box with standard wired USB keyboards and mice, as well as combo wireless keyboards and mice using a 2.4 GHz USB dongle.
* **USB-C OTG Option:** You can also plug a keyboard or hub straight into the native USB-C port using an OTG adapter.

---

## 🚦 6. WS2812 RGB LED Diagnostic Feedback (GP16)

The onboard WS2812 RGB LED provides real-time system diagnostics:

| LED Color | Animation | Meaning |
| :--- | :--- | :--- |
| 🟧 **Soft Orange** | Slow pulse | System booting and loading Macintosh Plus ROM. |
| 🟩 **Steady Green** | Gentle breathing | **System ready!** Finder desktop is active and listening for user input. |
| 🟨 **Bright Amber** | Fast flashes | Reading data blocks from the MicroSD card. |
| 🟪 **Bright Magenta**| Fast flashes | **Writing to MicroSD:** Saving files, documents, or high scores. |
| 🔴 **Continuous Red**| Alarm blinking | MicroSD Error: check SPI wiring or confirm card is FAT32 with `umac0.img`. |

---

## 🔋 7. Powering the Circuit

1. **Via USB-C Cable:** The easiest method. Connect the RP2040-Zero USB-C port to any phone wall charger (5V / 1A or 2A).
2. **Via Fixed 5V DC Power Supply:** Connect the +5V wire to the pad labeled **`5V` (VBUS)** and the negative wire to **`GND`**.
3. **Via Rechargeable Battery (Portable):** Connect a 3.7V 18650 lithium battery through a **TP4056 charging module with built-in 5V step-up booster**, feeding the `5V` and `GND` pads.

---

## 📜 Open License & Credits

This project is open-source software and open-source hardware, distributed under the **MIT License**. You are free to use, inspect, improve, and share it worldwide.

Engineered, optimized, and documented with passion by **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl)). Please maintain attribution and citation in any derivative builds.
