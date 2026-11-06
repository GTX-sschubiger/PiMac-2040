# Colección de Imágenes de Disco para PiMac 2040 (Macintosh 208K)
### Curado y Desarrollado por **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

Este directorio contiene una colección completa de imágenes de disco listas para arrancar y guardar datos directamente en una tarjeta MicroSD en la placa **RP2040-Zero**.

---

## 💽 Catálogo de Imágenes de Disco Disponibles

| Nombre de Archivo | Tamaño | Sistema Operativo | Tipo | Software Principal Incluido |
| :--- | :---: | :---: | :---: | :--- |
| **`umac0_master_10mb.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS Master | **Suite Completa:** Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA, MacPaint, MacDraw, TeachText, Disk Copy, Utilitarios e instaladores. |
| **`umac0.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS/MFS Clásico | MacPaint 1.3/1.5, MacWrite 4.5/1.0, MacDraw 1.9, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma, Recursive Curves, Desk Accessories. |
| **`umac0_games_pack.img`** | 4 MB | System 3.2 / Finder 5.3 | HFS Arcade | **Top Juegos Clásicos:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café (Air Hockey), Risk (Estrategia), Cannon Fodder, Tetris DA. |
| **`umac0_productivity.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Oficina | **Diseño y Oficina:** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock demo. |
| **`umac0_dark_castle.img`** | 800 KB | System Autónomo | HFS Juego | **Dark Castle v1.2:** La mítica aventura de plataformas y acción de Silicon Beach Software. Arranque directo. |
| **`umac0_beyond_dark_castle.img`** | 800 KB | System Autónomo | HFS Juego | **Beyond Dark Castle:** La aclamada secuela con salas avanzadas, helicóptero personal y bombas. |
| **`umac0_stunt_copter.img`** | 800 KB | System Autónomo | HFS Juego | **Stunt Copter:** Clásico juego de física y acrobacias aéreas con versiones 1.0, 1.2, 1.5, 1.6 y 2.0. |
| **`umac0_system11_1984.img`** | 400 KB | System 1.1 / Finder 1.1g | MFS Histórico | **Macintosh 128K 1984 Original:** La experiencia histórica y pura del lanzamiento de Steve Jobs en 1984. |
| **`umac0_system32_utilities.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Utilitarios | Disco oficial de utilidades de Apple con Font/DA Mover, Fuentes tipográficas completas, Desk Accessories e instaladores. |

---

## 🚀 ¿Cómo Usar y Cambiar Discos en la Tarjeta MicroSD?

El firmware **PiMac 2040** busca en el directorio raíz de la tarjeta MicroSD cualquier archivo cuyo nombre comience por `umac0*.img`.

### Opciones de Uso:

### Opción 1: Disco Todo-En-Uno (Recomendado)
Copia `umac0_master_10mb.img` a tu MicroSD y renómbralo a **`umac0.img`**:
* Tendrás **10 Megabytes** de almacenamiento con prácticamente todas las aplicaciones de oficina, diseño y juegos organizadas en carpetas con soporte de lectura y escritura.

### Opción 2: Tener Varios Discos y Seleccionar el Activo
Puedes copiar todas las imágenes a tu tarjeta MicroSD:
* `umac0.img` (el disco que arrancará por defecto)
* `games.img`
* `office.img`
* `darkcastle.img`
* `system1984.img`

Cuando quieras cambiar de disco, conecta la tarjeta a tu PC o teléfono y simplemente renombra el que deseas arrancar a **`umac0.img`**.

---

## 💾 Persistencia de Datos (Read/Write)
A diferencia de las ROMs embebidas en microcontroladores, al ejecutar estos discos desde la MicroSD conectada a la RP2040-Zero:
* **Puedes guardar documentos** en MacWrite o dibujos en MacPaint.
* **Puedes guardar puntuaciones más altas y partidas** en Dark Castle, Stunt Copter y Shufflepuck Café.
* **Puedes configurar Desk Accessories** y el Panel de Control, y la configuración se mantendrá al reiniciar la consola.
