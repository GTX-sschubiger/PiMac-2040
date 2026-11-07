# PiMac 2040 (Macintosh 208K) – Offizielles Hardware- und Installationshandbuch
### Open-Source-Software- und Hardware-Projekt von [SCHUBIGER.CL](https://schubiger.cl)
### MIT-Lizenz – Frei zur Nutzung, Anpassung und Weitergabe

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="RELEASE_README.md">🇪🇸 Español</a> |
  <a href="RELEASE_README_EN.md">🇬🇧 English</a> |
  <a href="RELEASE_README_PT.md">🇵🇹 Português</a> |
  <a href="RELEASE_README_DE.md"><strong>🇩🇪 Deutsch</strong></a> |
  <a href="RELEASE_README_ZH.md">🇨🇳 中文</a> |
  <a href="RELEASE_README_FR.md">🇫🇷 Français</a>
</p>


Willkommen bei **PiMac 2040**! Dieses Handbuch ist einfach, praxisnah und verständlich formuliert, sodass jeder — selbst ohne vorherige Mikrocontroller-Erfahrung — das System auf einem **RP2040** installieren, die Hardware in wenigen Minuten verdrahten und das vollständige Erlebnis eines klassischen 1984 Apple Macintosh mit Maus, Tastatur, MicroSD-Speicher und Videoausgabe auf Retro-Röhrenfernsehern oder PC-Monitoren erleben kann.

---

## ⚡ 1. Schnelle Systeminstallation auf dem RP2040 (In 3 Schritten)

Sie müssen keine Programmierwerkzeuge installieren oder Quellcode kompilieren. Die Firmware ist vorkompiliert und einsatzbereit in der Datei **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**:

```text
  [ .UF2-Datei ]      ------------------------->  [ RPI-RP2 Laufwerk ]  ---> Fertig geflasht!
  (PiMac 2040 Firmware)        Per Drag & Drop            (RP2040 im Boot-Modus)    (Neustart in 2 Sek.)
```

1. **Im Boot-Modus verbinden:** Nehmen Sie Ihre **Waveshare / Tenstar Robot RP2040-Zero** (oder Raspberry Pi Pico) Platine. Halten Sie die weiße **BOOT**-Taste (bzw. BOOTSEL) gedrückt und schließen Sie die Platine mit dem USB-C-Kabel an Ihren PC an. Lassen Sie die Taste anschließend los.
2. **Laufwerk erscheint:** Auf Ihrem PC öffnet sich automatisch ein Wechsellaufwerk namens **`RPI-RP2`** (genau wie beim Einstecken eines normalen USB-Speichersticks).
3. **Datei kopieren:** Ziehen Sie die folgende Datei direkt per Drag & Drop in das `RPI-RP2`-Laufwerk:
   👉 **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**
4. **Fertig!** Nach etwa 2 Sekunden blinkt die Platine kurz auf, das Wechsellaufwerk schließt sich automatisch und PiMac 2040 ist dauerhaft im internen Flash-Speicher installiert.

---

## 💾 2. MicroSD-Karte mit Diskettenabbildern einrichten

1. Verwenden Sie eine beliebige MicroSD-Karte (von 256 MB bis 32 GB).
2. Schließen Sie sie an Ihren PC an und formatieren Sie sie im Dateisystem **FAT32** (Schnellformatierung).
3. Öffnen Sie den Ordner **`disks/`** und wählen Sie das gewünschte Disk-Image:
   * **`umac0_oficina_almacenamiento_20mb.img`:** Vollwertiges Büro-Paket (Word 4.0, Excel 2.2, Works 3.0, PageMaker 2.0, MacPaint, MacDraw) mit über 10 MB freiem Speicherplatz im Ordner *Meine Dokumente* zum dauerhaften Speichern Ihrer Dateien.
   * **`umac0_aventura_juegos_15mb.img`:** Abenteuer- und Strategiepaket (Prince of Persia, SimCity 1.11, offizielles Tetris mit Audio, Dark Castle, Stunt Copter, Shufflepuck Café) mit über 8 MB freiem Speicher für Spielstände.
   * **`umac0_master_10mb.img`:** Ausgewogenes All-in-One-Image mit Spielen, Grafik- und System-Tools.
4. **Kopieren Sie die ausgewählte Imagedatei in das Hauptverzeichnis der MicroSD-Karte** und benennen Sie sie exakt um in:
   👉 **`umac0.img`**
5. Stecken Sie die MicroSD-Karte in Ihren PiMac 2040.

---

## 🛠️ 3. Die zwei Hardware-Varianten: Welche wählen?

Die Firmware verfügt über eine **intelligente Dual-Video-Engine**, die sowohl klassische Röhrenfernseher als auch PC-Monitore unterstützt:

```text
+-------------------------------------------------------------------------------------------------+
|                                    VARIANTENVERGLEICH                                           |
+-------------------------------------------------------------------------------------------------+
| MERKMAL                        | VERSION 1: NUR COMPOSITE-VIDEO  | VERSION 2: DUAL VGA + COMP.  |
+--------------------------------+---------------------------------+------------------------------+
| Unterstützte Bildschirme       | CRT-Röhren-TV / Cinch-AV-Monitor| CRT-Röhren-TV + VGA-Monitor  |
| Videoanschlüsse                | 1x Cinch-Buchse (RCA gelb)      | 1x Cinch + 1x VGA (DE-15)    |
| Aufbauaufwand                  | Minimal (nur 2 Widerstände)     | Moderat (3 Widerstände + VGA)|
| Display-Umschaltung            | Automatisch                     | Per Schalter / Jumper (GP0)  |
| MicroSD (Lesen & Schreiben)    | Ja                              | Ja                           |
| USB-Ports (Tastatur & Maus)    | Ja                              | Ja                           |
| Bauteilkosten gesamt           | Extrem niedrig (~4 bis 6 USD)   | Sehr günstig (~6 bis 8 USD)  |
+--------------------------------+---------------------------------+------------------------------+
```

---

## 📺 VERSION 1: Einfacher / Günstiger Aufbau (Nur Composite-Video)

[![Realer Hardware-Aufbau Version 1 Composite Video](assets/pimac2040_version1_composite.jpg)](assets/pimac2040_version1_composite.jpg)
*Realer Aufbau von Version 1: Composite-Cinch-Anschluss mit Spannungsteiler aus 560 Ω und 270 Ω Widerständen, MicroSD-SPI-Hack und USB-Ports.*

### Wie funktioniert das?
Diese Variante ermöglicht den direkten Anschluss des PiMac 2040 an jeden Retro-Röhrenfernseher (CRT) mit gelbem Cinch-Videoeingang (AV) oder Sicherheitsmonitor.

Der RP2040 erzeugt nativ das analoge Schwarz-Weiß-Videosignal nach dem **NTSC 480i** Standard. Über zwei herkömmliche Widerstände an den Pins GP8 und GP9 werden Synchronimpulse und Bildpixel digital gemischt, um das normgerechte 1,0 Vss Signal mit 75 Ω Wellenwiderstand zu liefern.

### Schaltplan Composite-Video:
```text
   RP2040-Zero (Pins)                            Gelbe Cinch-Buchse (RCA Female)
  +--------------------+                         +------------------------------+
  |                    |      560 Ω (Grün-Blau-Braun)                           |
  |  GP8 (Sync)        +-----[1/4W Widerstand]-----+                            |
  |                    |                           |                            |
  |                    |      270 Ω (Rot-Violett-Braun)                         |
  |  GP9 (Video)       +-----[1/4W Widerstand]-----+----> Mittelpin (Videosignal)|
  |                    |                                                        |
  |  GND (Masse)       +--------------------------------> Äußerer Schirm/Masse  |
  +--------------------+                         +------------------------------+
```

### Einkaufsliste Bauteile (Genaue Fachbegriffe):
1. **1x Entwicklungsboard:** **Waveshare RP2040-Zero** (oder Tenstar Robot RP2040-Zero).
2. **1x Cinch-Einbaubuchse gelb:** (*RCA Female Jack Panel Mount Connector*).
3. **1x 560 Ω Widerstand:** Metall- oder Kohleschicht, 1/4W oder 1/8W (Farbringe: Grün - Blau - Braun - Gold).
4. **1x 270 Ω Widerstand:** Metall- oder Kohleschicht, 1/4W oder 1/8W (Farbringe: Rot - Violett - Braun - Gold).
5. **1x Passiver MicroSD-auf-SD-Kartenadapter** (handelsüblicher Adapter aus SD-Kartenverpackungen) oder 3.3V MicroSD-SPI-Breakout-Modul.
6. **1x USB-C auf USB-A OTG-Adapter** (zum Anschluss von USB-Maus und -Tastatur).

---

## 🖥️ VERSION 2: Vollversion Dual (Composite-Video + VGA-Monitor)

[![Realer Hardware-Aufbau Version 2 Dual VGA und Composite](assets/pimac2040_version2_dual_vga_composite.jpg)](assets/pimac2040_version2_dual_vga_composite.jpg)
*Realer Aufbau von Version 2: Dual-Video-Betrieb mit DE-15 VGA-Buchse (100 Ω Widerstand), gelber Cinch-Buchse, SPDT-Umschalter und MicroSD-SPI.*

### Wie funktioniert die intelligente Dual-Video-Engine?
Beim Start prüft die Firmware den logischen Pegel an **GP0**:
* **Start mit GP0 unbeschaltet (offen):** Der RP2040 startet im **Composite-Video-Modus** mit 15,734 kHz über Cinch (ideal für Röhren-TVs).
* **Start mit GP0 auf Masse (GND):** Der RP2040 schaltet auf **Standard-VGA-Modus** mit 640x480 @ 60 Hz (31,468 kHz) über die DE-15 Buchse (ideal für PC-Monitore).

Beide Anschlüsse können dauerhaft verlötet sein. Mit einem kleinen Schiebeschalter wählen Sie bequem zwischen Schreibtischmonitor und Fernseher!

### Schaltplan Dual-Video (VGA + Composite):
```text
   RP2040-Zero (Pins)                            VGA-Buchse (DE-15 / DB-15)
  +--------------------+                         +-----------------------------------+
  |  GP26 (Video)      +-----[ 100 Ω (1/4W) ]----+----> Pins 1, 2 und 3 (Rot, Grün, Blau gebrückt)
  |  GP27 (VSync)      +-------------------------> Pin 14 (Vertikalsynchronisation)
  |  GP29 (HSync)      +-------------------------> Pin 13 (Horizontalsynchronisation)
  |  GND (Masse)       +-------------------------> Pins 5, 6, 7, 8 und 10 (Video-GND)
  +--------------------+                         +-----------------------------------+

   MONITOR-WAHLSCHALTER:
  +--------------------+                         +-----------------------------------+
  |  GP0               +----> [ SPDT Schalter]---> GND (Masse)
  |                    |      Offen: Startet im Composite-Modus (CRT TV)
  |                    |      Geschlossen: Startet im VGA-Modus (PC-Monitor)
  +--------------------+                         +-----------------------------------+

   COMPOSITE-VIDEO CINCH (Gleichzeitig):
  +--------------------+                         +-----------------------------------+
  |  GP8 (Sync)        +-----[ 560 Ω (1/4W) ]----+
  |  GP9 (Video)       +-----[ 270 Ω (1/4W) ]----+----> Mittelpin der Cinch-Buchse
  |  GND (Masse)       +------------------------------> Äußerer Schirm der Cinch-Buchse
  +--------------------+                         +-----------------------------------+
```

### Zusätzliche Komponenten für Version 2:
1. **Alle Teile aus Version 1** (RP2040-Zero, Cinch-Buchse, 560 Ω und 270 Ω Widerstände, MicroSD, USB).
2. **1x 15-polige VGA-D-Sub-Buchse DE-15:** 3-reihig für Gehäuseeinbau (*VGA DB15 Female 3-Row D-Sub Connector*).
3. **1x 100 Ω Widerstand:** Metall- oder Kohleschicht, 1/4W oder 1/8W (Farbringe: Braun - Schwarz - Braun - Gold).
4. **1x SPDT Miniatur-Schiebeschalter** oder 2-Pin Jumper (*SPDT Mini Slide Switch 3 Pin*).

---

## 💾 4. MicroSD-Karten-Verbindung (SPI)

Sie können ein handelsübliches 3.3V-MicroSD-Modul verwenden oder 6 dünne Drähte direkt an die goldenen Kontakte auf der Rückseite eines **passiven SD-Adapters** löten:

```text
       RP2040-Zero                               Passiver SD-Adapter (Rückseite)
   +-----------------------+                    +------------------------------------+
   |   GP5 (CS)            +------------------->| Kontakt 1 (CD/DAT3)                |
   |   GP3 (MOSI)          +------------------->| Kontakt 2 (CMD / MOSI)             |
   |   GND                 +------------------->| Kontakt 3 (VSS1 / Masse)           |
   |   3V3 (3.3 Volt)      +------------------->| Kontakt 4 (VDD) ⚠️ ACHTUNG: NUR 3.3V!
   |   GP2 (SCK)           +------------------->| Kontakt 5 (CLK / Takt)             |
   |   GND                 +------------------->| Kontakt 6 (VSS2 / Masse)           |
   |   GP4 (MISO)          +------------------->| Kontakt 7 (DAT0 / MISO)            |
   +-----------------------+                    +------------------------------------+
```

> [!CAUTION]
> Schließen Sie die Stromversorgung der MicroSD-Karte **ausschließlich an den 3V3 (3.3V) Pin** des RP2040-Zero an. Verbinden Sie sie **niemals mit 5V**, da die Speicherkarte sonst sofort zerstört wird!

---

## 🖱️ 5. USB-Anschluss für Tastatur und Maus

PiMac 2040 verfügt über einen hardwaregestützten (PIO) **USB-Host-Controller**:

```text
       RP2040-Zero                               Zwei USB-A Buchsen
   +-----------------------+                    +-------------------------------------+
   |   5V (VBUS)           +------------------->| Pin 1 (+5V USB Strom) [Beide Ports] |
   |                       |                    +-------------------------------------+
   |                       |                    | PORT 1 (USB-TASTATUR):              |
   |   GP10                +----[ 27 Ω ]--------+ Pin 3: D+ (Daten positiv)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP11                +----[ 27 Ω ]--------+ Pin 2: D- (Daten negativ)           |
   |                       |          |         +-------------------------------------+
   |                       |       [ 15 kΩ ]    | PORT 2 (USB-MAUS):                  |
   |   GP12                +----[ 27 Ω ]--------+ Pin 3: D+ (Daten positiv)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP13                +----[ 27 Ω ]--------+ Pin 2: D- (Daten negativ)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GND (Masse)         +----------+---------+ Pin 4: GND (USB Masse) [Beide Ports]|
   +-----------------------+                    +-------------------------------------+
```

* **Kompatibilität:** Kompatibel mit nahezu allen gängigen USB-Tastaturen und -Mäusen sowie Funk-Kombinationen mit 2,4-GHz-USB-Dongle.
* **USB-C OTG-Option:** Alternativ kann eine Tastatur über einen OTG-Adapter direkt an den USB-C-Anschluss der Platine gesteckt werden.

---

## 🚦 6. Statusdiagnose über die WS2812 RGB-LED (GP16)

Die integrierte RGB-LED auf der Platine dient als Echtzeit-Statusanzeige:

| LED-Farbe | Anzeige | Bedeutung |
| :--- | :--- | :--- |
| 🟧 **Sanftes Orange** | Langsames Pulsieren | Systemstart und Laden der Macintosh Plus ROM. |
| 🟩 **Dauerhaft Grün** | Sanftes Atmen | **System betriebsbereit!** Der Finder-Desktop wartet auf Eingaben. |
| 🟨 **Helles Bernstein** | Schnelles Blitzen | Datenblöcke werden von der MicroSD gelesen. |
| 🟪 **Helles Magenta** | Schnelles Blitzen | **Daten schreiben:** Speichern von Dateien, Bildern oder Spielständen. |
| 🔴 **Dauerhaft Rot** | Warnblinken | MicroSD-Fehler: SPI-Verdrahtung oder FAT32-Formatierung mit `umac0.img` prüfen. |

---

## 🔋 7. Stromversorgung

1. **Per USB-C-Kabel:** Die einfachste Variante. Verbinden Sie den USB-C-Port mit einem handelsüblichen Handyladegerät (5V / 1A bis 2A).
2. **Per 5V Festspannungsnetzteil:** Pluspol an den Pin **`5V` (VBUS)** und Minuspol an **`GND`** anschließen.
3. **Per Akku (Portabler Betrieb):** Verwendung eines 3.7V 18650 Lithium-Akkus mit einem **TP4056 Lademodul inklusive 5V Step-up Booster**.

---

## 📜 Offene Lizenz & Danksagung

Dieses Projekt ist Open-Source-Software und Open-Source-Hardware unter der **MIT-Lizenz**. Es darf frei studiert, verbessert und geteilt werden.

Entwickelt, optimiert und dokumentiert von **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl)). Bitte behalten Sie bei Weiterverbreitung die Quellenangabe bei.
