# 🛠️ Guía de Compilación y Arquitectura del Código Fuente
### Proyecto **PiMac 2040** — Desarrollado por **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

Esta guía proporciona toda la información técnica necesaria para compilar el firmware desde cero, entender la arquitectura del software y modificar el código para agregar nuevas funciones.

---

## 🏗️ 1. Estructura y Módulos del Código Fuente

El proyecto está organizado de manera modular y limpia:

```text
github/
├── src/
│   ├── main.c                 # Punto de entrada, inicialización de hardware, montaje SD y bucle principal
│   ├── video_manager.c        # Detección de jumper GP0 y conmutador de motor de video (Compuesto vs VGA)
│   ├── video_composite.c      # Generador de señal de Video Compuesto Monocromo NTSC 480i con PIO
│   ├── video.c                # Generador de señal VGA estándar (640x480 @ 60Hz) con PIO
│   ├── mac_status.c           # Controlador WS2812 RGB en GP16 con temporizaciones precisas a 250 MHz
│   ├── hid.c & kbd.c          # Pila USB Host TinyUSB para teclado y mouse USB
│   ├── sd_hw_config.c         # Configuración del bus SPI para tarjeta MicroSD
│   ├── pio_composite.pio      # Máquina de estados PIO para sincronismo y píxeles analógicos CVBS
│   └── pio_video.pio          # Máquina de estados PIO para sincronismo HSync/VSync y píxeles VGA
├── include/
│   ├── hw.h                   # Mapeo de pines GPIO de la RP2040-Zero
│   ├── video.h                # Interfaz abstracta del subsistema de video
│   ├── mac_status.h           # Estados visuales del LED RGB (Boot, Read, Write, Panic)
│   └── tusb_config.h          # Configuración TinyUSB en modo Host
├── external/
│   ├── umac/                  # Emulador Macintosh clásico (MMU virtual, VIA, RTC, Sound, Floppy .Sony)
│   ├── umac/external/Musashi/ # Núcleo de emulación Motorola 68000 en C de Karl Stenerud
│   └── no-OS-FatFS-SD-SPI.../ # Driver FatFS optimizado con transferencias DMA por bus SPI
├── rom/
│   └── rom.bin                # Imagen de ROM de Macintosh Plus (128 KB) parcheada para 208K
├── tools/
│   ├── patch_rom.py           # Herramienta para parchear la resolución y vectores de la ROM
│   ├── bin2h.py               # Conversor de binarios a cabeceras C (incbin)
│   ├── build_disk_collection.py # Ensamblador de imágenes de disco HFS con machfs
│   └── sync_github_folder.py  # Sincronizador de la suite para GitHub
├── CMakeLists.txt             # Script de construcción para Raspberry Pi Pico SDK
├── pico_sdk_import.cmake      # Importador oficial de Pico SDK
└── build.bat                  # Script de compilación automática para Windows
```

---

## ⚙️ 2. Requisitos de Compilación

Para compilar el código fuente necesitas:
1. **Raspberry Pi Pico SDK** (versión 1.5.0 o superior):
   * Variable de entorno configurada: `PICO_SDK_PATH` apuntando a la carpeta de tu Pico SDK.
2. **Toolchain ARM GCC**: `arm-none-eabi-gcc` (versión 10.3 o superior).
3. **CMake** (versión 3.13 o superior).
4. **Ninja** (recomendado) o **Make**.
5. **Python 3** (para scripts de generación de cabeceras).

---

## 💻 3. Instrucciones de Compilación

### En Windows (Método Rápido con `build.bat`):
Si tienes el entorno de desarrollo de ARM GCC y Pico SDK configurado en tu sistema, simplemente ejecuta:
```cmd
build.bat
```
El script creará la carpeta `build/`, configurará CMake con Ninja y generará el archivo `build/firmware.uf2`.

### En Windows o Linux (Método Manual por Terminal):
```bash
# 1. Crear carpeta de compilación
mkdir build
cd build

# 2. Configurar el proyecto con CMake (especificando placa pico o pico-zero)
cmake -G Ninja -DPICO_BOARD=pico -DCMAKE_BUILD_TYPE=Release ..

# 3. Compilar el firmware
ninja -j4
```

Al finalizar la compilación, se generará el archivo ejecutable listo para flashear:
* **`build/firmware.uf2`** (aprox. 1.4 MB)

---

## 🧠 4. Claves Técnicas de la Arquitectura

### A. Overclocking a 250 MHz
La RP2040-Zero opera de fábrica a 125 MHz. Para poder emular la CPU Motorola 68000 a velocidad completa ($7.83\text{ MHz}$) y simultáneamente generar señales analógicas de video en tiempo real mediante máquinas de estado PIO sin ningún retardo:
* El reloj del sistema (`sys_clk`) se eleva automáticamente a **$250\text{ MHz}$** en [`src/main.c`](src/main.c).

### B. Expansión de Memoria a 208 KB (Mac 208K)
El Macintosh 128K original contaba con 128 KB de RAM. La RP2040 dispone de 264 KB de SRAM interna:
* Se reservan 208 KB exclusivamente para la memoria RAM emulada del Mac.
* Los 56 KB restantes se asignan al frame buffer de video, buffers DMA de SPI para la MicroSD y pila del sistema.
* Esto permite ejecutar aplicaciones que normalmente exigirían un Macintosh 512K, como **MacPaint**, **Dark Castle** o procesadores de texto complejos.

### C. Conmutación de Video Permanente (Video Compuesto + VGA)
En [`src/video_manager.c`](src/video_manager.c), al arrancar el procesador:
1. Se configura el pin **`GP0`** con resistencia pull-up interna.
2. Si `GP0` está flotante (abierto), activa el motor de **Video Compuesto NTSC 480i** en `GP8` y `GP9`.
3. Si `GP0` está conectado a `GND` (con un jumper), activa el motor **VGA 640x480 @ 60Hz** en `GP26..GP29`.
4. Ambos circuitos analógicos pueden estar conectados permanentemente sin interferirse entre sí.
