# Colección de Imágenes de Disco para PiMac 2040 (Macintosh 208K)
### Curado y Desarrollado por **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="README.md"><strong>🇪🇸 Español</strong></a> |
  <a href="README_EN.md">🇬🇧 English</a> |
  <a href="README_PT.md">🇵🇹 Português</a> |
  <a href="README_DE.md">🇩🇪 Deutsch</a> |
  <a href="README_ZH.md">🇨🇳 中文</a> |
  <a href="README_FR.md">🇫🇷 Français</a>
</p>


Este directorio contiene una colección completa de imágenes de disco listas para arrancar y guardar datos directamente en una tarjeta MicroSD en la placa **RP2040-Zero**.

---

## 💽 Catálogo de Imágenes de Disco Disponibles

| Nombre de Archivo | Tamaño | Sistema Operativo | Tipo | Software Principal Incluido |
| :--- | :---: | :---: | :---: | :--- |
| **`umac0_oficina_almacenamiento_20mb.img`** | **20 MB** | System 3.2 / Finder 5.3 | HFS Oficina & Almacenamiento | **Productividad y Trabajo Real:**<br>• **Microsoft Office:** Word 4.0a, Excel 2.2a, Works 3.0 (suite integrada con textos, hojas de cálculo y base de datos).<br>• **Autoedición y Diseño:** Aldus PageMaker 2.0a, MacPaint 2.0, MacDraw 1.9.<br>• **Editores:** TeachText, BBEdit Lite 3.5.1.<br>• **Herramientas:** Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm 1.0.1.<br>• **📁 Mis Documentos:** Carpeta dedicada con **más de 10 MB de espacio libre permanente** para guardar tus propios archivos en la MicroSD. |
| **`umac0_aventura_juegos_15mb.img`** | **15 MB** | System 3.2 / Finder 5.3 | HFS Aventura & Juegos | **Aventura y Estrategia Top:**<br>• **Prince of Persia:** La legendaria obra maestra de acción y plataformas de Jordan Mechner con duelos a espada (versión BW optimizada).<br>• **SimCity 1.11:** El simulador clásico de construcción de ciudades de Will Wright con escenarios y sonidos.<br>• **Tetris:** Edición oficial de Spectrum HoloByte con temas musicales y efectos.<br>• **Clásicos Silicon Beach:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter v1.x/2.0.<br>• **Juegos de Mesa y Arcade:** Shufflepuck Café, Risk (Estrategia Mundial), Cannon Fodder, Lode Runner, Billiard Parlour.<br>• **📁 Mis Partidas Guardadas:** Más de 8 MB libres para almacenar partidas de Prince of Persia, ciudades de SimCity y records. |
| **`umac0_master_10mb.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS Todo-en-Uno | **Equilibrio Óptimo:** Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA, MacPaint, MacDraw, TeachText, Disk Copy, Utilitarios. |
| **`umac0.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS/MFS Clásico | **Colección Original:** MacPaint 1.3, MacWrite 4.5, MacDraw, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma. |
| **`umac0_games_pack.img`** | 4 MB | System 3.2 / Finder 5.3 | HFS Arcade Pack | **Especial Juegos Rápidos:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA. |
| **`umac0_productivity.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Productividad | **Esencial de Trabajo:** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock. |
| **`umac0_dark_castle.img`** | 800 KB | System Autónomo | HFS Juego Individual | **Dark Castle v1.2:** Versión booteable directa del legendario juego de plataformas. |
| **`umac0_beyond_dark_castle.img`** | 800 KB | System Autónomo | HFS Juego Individual | **Beyond Dark Castle:** Secuela con mochila propulsora, bombas y salas secretas. |
| **`umac0_stunt_copter.img`** | 800 KB | System Autónomo | HFS Juego Individual | **Stunt Copter:** Físicas clásicas de Duane Blehm (v1.0 y v2.0). |
| **`umac0_system11_1984.img`** | 400 KB | System 1.1 / Finder 1.1g | MFS Histórico 1984 | **Macintosh 128K Histórico:** La experiencia original con la que Steve Jobs presentó el Macintosh el 24 de enero de 1984. |
| **`umac0_system32_utilities.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Herramientas | **Utilidades Oficiales de Apple:** Font/DA Mover, Fuentes históricas (Chicago, Geneva, Monaco, San Francisco) y herramientas de disco. |

---

## 🚀 ¿Cómo Usar y Cambiar Discos en la Tarjeta MicroSD?

El firmware **PiMac 2040** busca en el directorio raíz de la tarjeta MicroSD cualquier archivo cuyo nombre sea **`umac0.img`**.

### Opciones de Uso:

### Opción 1: Disco Todo-En-Uno (Recomendado)
Copia `umac0_oficina_almacenamiento_20mb.img` o `umac0_master_10mb.img` a tu MicroSD y renómbralo a **`umac0.img`**:
* Tendrás almacenamiento de sobra con prácticamente todas las aplicaciones de oficina, diseño y juegos organizadas en carpetas con soporte de lectura y escritura.

### Opción 2: Tener Varios Discos y Seleccionar el Activo
Puedes copiar todas las imágenes a tu tarjeta MicroSD:
* `umac0.img` (el disco que arrancará por defecto)
* `oficina.img`
* `juegos.img`
* `darkcastle.img`
* `system1984.img`

Cuando quieras cambiar de disco, conecta la tarjeta a tu PC o teléfono y simplemente renombra el que deseas arrancar a **`umac0.img`**.

---

## 💾 Persistencia de Datos (Read/Write)
A diferencia de las ROMs embebidas en microcontroladores, al ejecutar estos discos desde la MicroSD conectada a la RP2040-Zero:
* **Puedes guardar documentos** en MacWrite o dibujos en MacPaint.
* **Puedes guardar puntuaciones más altas y partidas** en Prince of Persia, SimCity, Dark Castle, Stunt Copter y Shufflepuck Café.
* **Puedes configurar Desk Accessories** y el Panel de Control, y la configuración se mantendrá al reiniciar la consola.
