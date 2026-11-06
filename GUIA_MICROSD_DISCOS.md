# 💽 Guía de Uso e Instalación de Discos en Tarjeta MicroSD
### Proyecto **PiMac 2040** — Desarrollado por **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

Esta guía detalla paso a paso cómo preparar cualquier tarjeta MicroSD, cómo cargar los discos incluidos con sus aplicaciones y juegos, y cómo alternar entre diferentes entornos de Macintosh clásico en la placa **RP2040-Zero**.

---

## 📋 1. Requisitos de la Tarjeta MicroSD
* **Capacidad:** Cualquier tarjeta MicroSD o MicroSDHC desde **256 MB hasta 32 GB** (las tarjetas de 64GB o superiores también funcionan si se formatean en FAT32 con herramientas como *GUIFormat* o *Rufus*).
* **Formato de Archivos Requerido:** **FAT32** (o ExFAT).
* **Adaptador:** Puedes usar un módulo lector MicroSD SPI comercial o un adaptador pasivo de plástico SD a MicroSD soldado directamente a la RP2040-Zero (ver [GUIA_HARDWARE_PINOUT.md](GUIA_HARDWARE_PINOUT.md)).

---

## 🛠️ 2. Cómo Formatear la Tarjeta en FAT32

### En Windows:
1. Inserta tu tarjeta MicroSD en tu computadora.
2. Abre **Este equipo**, haz clic derecho sobre la unidad de la MicroSD y selecciona **Formatear...**
3. En **Sistema de archivos**, selecciona **FAT32**.
4. En **Tamaño de unidad de asignación**, selecciona **32 kilobytes** (o el tamaño predeterminado).
5. Marca **Formato rápido** y presiona **Iniciar**.

### En macOS:
1. Abre **Utilidad de Discos** (*Disk Utility*).
2. Selecciona la tarjeta MicroSD en la barra lateral.
3. Haz clic en **Borrar** (*Erase*).
4. En **Formato**, elige **MS-DOS (FAT)** y en **Esquema**, **Registro de arranque principal (MBR)**.
5. Haz clic en **Borrar**.

### En Linux:
```bash
# Identifica la unidad (ej. /dev/sdb1)
sudo mkfs.vfat -F 32 -n "PIMAC" /dev/sdb1
```

---

## 📁 3. Catálogo de Imágenes de Disco Disponibles en `disks/`

| Archivo | Tamaño | SO | Aplicaciones y Videojuegos Incluidos |
| :--- | :---: | :---: | :--- |
| **`umac0_oficina_almacenamiento_20mb.img`** | **20 MB** | System 3.2 | **Productividad y Almacenamiento (Recomendado para Trabajar):**<br>• *Microsoft Office:* Word 4.0a, Excel 2.2a, Works 3.0 (suite con texto, hoja de cálculo y base de datos).<br>• *Autoedición y Diseño:* Aldus PageMaker 2.0a, MacPaint 2.0, MacDraw 1.9.<br>• *Editores:* TeachText, BBEdit Lite 3.5.1.<br>• *Herramientas:* Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm 1.0.1.<br>• *📁 Mis Documentos:* Carpeta con **más de 10 MB de espacio libre permanente** para guardar tus archivos en la MicroSD. |
| **`umac0_master_10mb.img`** | **10 MB** | System 3.2 | **Todo-En-Uno (Recomendado para Juegos):**<br>• *Juegos:* Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café (Air Hockey), Risk, Cannon Fodder, Tetris DA.<br>• *Productividad:* MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock.<br>• *Utilitarios:* Font/DA Mover, Fuentes históricas e instaladores. |
| **`umac0.img`** | **10 MB** | System 3.2 | **Colección Clásica:** MacPaint 1.3/1.5, MacWrite 4.5/1.0, MacDraw 1.9, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma, Desk Accessories. |
| **`umac0_games_pack.img`** | **4 MB** | System 3.2 | **Arcade Pack:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA. |
| **`umac0_productivity.img`** | **800 KB** | System 3.2 | **Oficina y Diseño:** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock. |
| **`umac0_dark_castle.img`** | **800 KB** | Autónomo | **Dark Castle v1.2:** Disco dedicado con carga directa al legendario juego de plataformas de Silicon Beach Software. |
| **`umac0_beyond_dark_castle.img`** | **800 KB** | Autónomo | **Beyond Dark Castle:** Secuela completa con helicóptero personal, bombas y salas avanzadas. |
| **`umac0_stunt_copter.img`** | **800 KB** | Autónomo | **Stunt Copter:** Físicas acrobáticas de Duane Blehm (v1.0 a 2.0 y versión parcheada). |
| **`umac0_system11_1984.img`** | **400 KB** | System 1.1 | **Macintosh 128K 1984 Histórico:** La experiencia original con la que Steve Jobs presentó la Mac en 1984. |
| **`umac0_system32_utilities.img`** | **800 KB** | System 3.2 | **Apple Utilities:** Font/DA Mover, Fuentes tipográficas completas y herramientas de diagnóstico. |

---

## ⚡ 4. Cómo Cargar los Discos en la MicroSD

El firmware de la RP2040-Zero escanea el directorio raíz de la MicroSD en busca del archivo que empiece por **`umac0*.img`**. El primer archivo que coincida será montado como la unidad de arranque principal:

### Método A: Disco Maestro Todo-En-Uno (La opción más fácil)
1. Toma el archivo `disks/umac0_master_10mb.img`.
2. Cópialo a la raíz de tu tarjeta MicroSD.
3. Renómbralo a **`umac0.img`**.
4. ¡Listo! Al encender la placa, tendrás todas las aplicaciones y juegos disponibles en tu escritorio.

### Método B: Tener Múltiples Discos en la Tarjeta
Puedes guardar todos los discos en la tarjeta MicroSD para tenerlos a mano:
* `E:\umac0.img` *(el disco que arrancará activamente)*
* `E:\juegos.img`
* `E:\oficina.img`
* `E:\darkcastle.img`
* `E:\system1984.img`

Cuando quieras cambiar de sistema o juego, simplemente conecta la MicroSD a tu PC o teléfono y renombra el que quieras jugar a **`umac0.img`**.

---

## 💾 5. Grabación y Persistencia (Read / Write)
A diferencia de los emuladores básicos que solo leen ROMs de solo lectura:
* **En MacPaint:** Puedes crear dibujos y presionar `Command + S` para guardarlos en el disco.
* **En MacWrite:** Puedes redactar documentos completos y almacenarlos en carpetas.
* **En Dark Castle y Stunt Copter:** Tus puntuaciones más altas (*High Scores*) quedan grabadas en la MicroSD.
* **En el Escritorio:** La posición de los iconos, las carpetas que crees y las preferencias del Panel de Control persisten para la próxima vez que enciendas tu PiMac 2040.

---

## 🔍 6. Diagnóstico y Estado con el LED RGB Integrado
El LED RGB integrado en la placa RP2040-Zero (`GP16`) te indica exactamente lo que está haciendo la MicroSD:
* 🟡 **Parpadeo Ámbar:** Lectura activa de bloques desde la tarjeta MicroSD.
* 🟣 **Parpadeo Magenta:** Escritura activa de datos hacia la tarjeta MicroSD.
* 🟠 **Pulso Naranja Suave:** Cargando System y Finder desde la MicroSD.
* 🟢 **Respiración Verde:** Sistema arrancado con éxito y listo para usar en Finder.
* 🔴 **Destello Rojo:** Error de lectura/escritura (verifica el cableado SPI o el formato FAT32).
