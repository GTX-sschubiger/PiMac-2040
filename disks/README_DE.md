# Disk-Image-Sammlung für PiMac 2040 (Macintosh 208K)
### Zusammengestellt und entwickelt von **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="README.md">🇪🇸 Español</a> |
  <a href="README_EN.md">🇬🇧 English</a> |
  <a href="README_PT.md">🇵🇹 Português</a> |
  <a href="README_DE.md"><strong>🇩🇪 Deutsch</strong></a> |
  <a href="README_ZH.md">🇨🇳 中文</a> |
  <a href="README_FR.md">🇫🇷 Français</a>
</p>


Dieses Verzeichnis enthält eine umfassende Bibliothek startbereiter Disk-Images mit vollständiger Schreib- und Leseunterstützung für MicroSD-Karten auf dem **RP2040-Zero**.

---

## 💽 Katalog der verfügbaren Disk-Images

| Dateiname | Größe | Betriebssystem | Typ | Enthaltene Software & Highlights |
| :--- | :---: | :---: | :---: | :--- |
| **`umac0_oficina_almacenamiento_20mb.img`** | **20 MB** | System 3.2 / Finder 5.3 | HFS Büro & Speicher | **Echtes Arbeiten & Produktivität:**<br>• **Microsoft Office Suite:** Word 4.0a, Excel 2.2a, Works 3.0 (integrierte Textverarbeitung, Tabellenkalkulation und Datenbank).<br>• **DTP & Design:** Aldus PageMaker 2.0a, MacPaint 2.0, MacDraw 1.9.<br>• **Texteditoren:** TeachText, BBEdit Lite 3.5.1.<br>• **System-Tools:** Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm 1.0.1.<br>• **📁 Meine Dokumente:** Eigener Ordner mit **über 10 MB freiem Speicherplatz** zum Speichern von Dateien auf der MicroSD. |
| **`umac0_aventura_juegos_15mb.img`** | **15 MB** | System 3.2 / Finder 5.3 | HFS Abenteuer & Spiele | **Spitzen-Retro-Gaming:**<br>• **Prince of Persia:** Jordan Mechners legendäres Action-Plattform-Meisterwerk mit Schwertkämpfen (optimierte S/W-Fassung).<br>• **SimCity 1.11:** Will Wrights klassische Städtebausimulation mit Szenarien und Sound.<br>• **Tetris:** Offizielle Spectrum HoloByte-Edition mit Musikthemen.<br>• **Silicon Beach Klassiker:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter v1.x/2.0.<br>• **Arcade & Brettspiele:** Shufflepuck Café, Risk (Weltstrategie), Cannon Fodder, Lode Runner, Billiard Parlour.<br>• **📁 Meine Spielstände:** Über 8 MB freier Speicherplatz für SimCity-Städte und Spielstände. |
| **`umac0_master_10mb.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS Alles-in-Einem | **Optimale Balance:** Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA, MacPaint, MacDraw, TeachText, Disk Copy, Dienstprogramme. |
| **`umac0.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS/MFS Klassiker | **Originale Klassikersammlung:** MacPaint 1.3, MacWrite 4.5, MacDraw, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma. |
| **`umac0_games_pack.img`** | 4 MB | System 3.2 / Finder 5.3 | HFS Arcade-Paket | **Kompakte Spielesammlung:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA. |
| **`umac0_productivity.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Produktivität | **Wesentliche Werkzeuge:** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock. |
| **`umac0_dark_castle.img`** | 800 KB | Eigenständiges System | HFS Einzelspiel | **Dark Castle v1.2:** Direkt startbare Version des legendären Plattformer-Hits. |
| **`umac0_beyond_dark_castle.img`** | 800 KB | Eigenständiges System | HFS Einzelspiel | **Beyond Dark Castle:** Geniale Fortsetzung mit Jetpack, Bomben und Geheimräumen. |
| **`umac0_stunt_copter.img`** | 800 KB | Eigenständiges System | HFS Einzelspiel | **Stunt Copter:** Physik-Klassiker von Duane Blehm (v1.0 & v2.0). |
| **`umac0_system11_1984.img`** | 400 KB | System 1.1 / Finder 1.1g | MFS Historisch 1984 | **Macintosh 128K Original:** Das historische System der Originalpräsentation von Steve Jobs am 24. Januar 1984. |
| **`umac0_system32_utilities.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS System-Tools | **Offizielle Apple-Werkzeuge:** Font/DA Mover, historische Schriftarten (Chicago, Geneva, Monaco, San Francisco) und Disk-Tools. |

---

## 🚀 Disketten auf der MicroSD-Karte verwenden und wechseln

Die Firmware des **PiMac 2040** sucht im Stammverzeichnis der MicroSD-Karte nach der Datei namens **`umac0.img`**.

### Verwendungsmöglichkeiten:

### Option 1: All-in-One Master-Disk (Empfohlen)
Kopieren Sie `umac0_oficina_almacenamiento_20mb.img` oder `umac0_master_10mb.img` auf Ihre MicroSD-Karte und benennen Sie die Datei in **`umac0.img`** um:
* Sie erhalten reichlich Speicherplatz mit allen Büroanwendungen, Zeichenprogrammen und Spielen übersichtlich in Ordnern organisiert mit vollständiger Lese- und Schreibunterstützung.

### Option 2: Mehrere Images vorhalten und das aktive wählen
Sie können alle Images gleichzeitig auf der MicroSD-Karte speichern:
* `umac0.img` (das aktuell aktive Boot-Image)
* `office.img`
* `games.img`
* `darkcastle.img`
* `system1984.img`

Wenn Sie ein anderes System starten möchten, stecken Sie die MicroSD-Karte in Ihren PC oder Ihr Smartphone und benennen Sie das gewünschte Image in **`umac0.img`** um.

---

## 💾 Dauerhafte Datenspeicherung (Read/Write)
Im Gegensatz zu schreibgeschützten ROMs bietet das Ausführen von der MicroSD-Karte auf dem RP2040-Zero echte Persistenz:
* **Dokumente speichern** in MacWrite oder Grafiken in MacPaint.
* **Spielstände und Highscores sichern** in Prince of Persia, SimCity, Dark Castle, Stunt Copter und Shufflepuck Café.
* **Desk Accessories und Systemeinstellungen anpassen**; alle Einstellungen bleiben auch nach dem Neustart erhalten!
