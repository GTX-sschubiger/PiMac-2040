# PiMac 2040 (Macintosh 208K) – Guía Oficial de Instalación y Hardware
### Proyecto de Código y Hardware Abierto por [SCHUBIGER.CL](https://schubiger.cl)
### Licencia MIT – Libre para Usar, Modificar y Compartir

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="RELEASE_README.md"><strong>🇪🇸 Español</strong></a> |
  <a href="RELEASE_README_EN.md">🇬🇧 English</a> |
  <a href="RELEASE_README_PT.md">🇵🇹 Português</a> |
  <a href="RELEASE_README_DE.md">🇩🇪 Deutsch</a> |
  <a href="RELEASE_README_ZH.md">🇨🇳 中文</a> |
  <a href="RELEASE_README_FR.md">🇫🇷 Français</a>
</p>


¡Bienvenido a **PiMac 2040**! Esta guía está redactada en un lenguaje simple, directo y práctico para que cualquier persona —incluso sin experiencia previa en microcontroladores— pueda instalar el sistema en una placa **RP2040**, armar su circuito en minutos y revivir la experiencia completa de una computadora Apple Macintosh clásica con ratón, teclado, tarjeta MicroSD y salida de video para televisores o monitores.

---

## ⚡ 1. Instalación Rápida del Sistema en el RP2040 (En 3 Pasos)

No necesitas instalar programas complejos ni compilar código fuente. El firmware ya está compilado y listo para usar en el archivo **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**:

```text
  [ Archivo .UF2 ]  ------------------------->  [ Unidad RPI-RP2 ]  ---> ¡Instalado!
  (Firmware PiMac 2040)       Arrastrar y soltar       (RP2040 en modo Boot)       (Se reinicia en 2 seg)
```

1. **Conectar en modo Boot:** Toma tu placa **Waveshare / Tenstar Robot RP2040-Zero** (o Raspberry Pi Pico). Mantén presionado el botón blanco **BOOT** (o BOOTSEL) de la placa y, sin soltarlo, conéctala a tu computadora con el cable USB-C. Luego suelta el botón.
2. **Aparición de la unidad:** En tu computadora aparecerá automáticamente una nueva unidad de disco extraíble llamada **`RPI-RP2`** (exactamente igual a cuando conectas un pendrive USB).
3. **Copiar el archivo:** Arrastra y suelta dentro de la unidad `RPI-RP2` el archivo:
   👉 **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**
4. **¡Listo!** En 2 segundos la placa parpadeará, la ventana se cerrará sola y el sistema PiMac 2040 quedará instalado permanentemente en la memoria Flash del microcontrolador.

---

## 💾 2. Preparar la Tarjeta MicroSD con los Discos y Aplicaciones

1. Toma cualquier tarjeta MicroSD (desde 256 MB hasta 32 GB).
2. Conéctala a tu PC y formatéala en formato **FAT32** (Formato rápido).
3. Entra en la carpeta **`disks/`** y elige el disco que quieras usar:
   * **`umac0_oficina_almacenamiento_20mb.img`:** Suite de oficina completa (Microsoft Word 4.0, Excel 2.2, Works 3.0, PageMaker 2.0, MacPaint, MacDraw) con más de 10 MB libres en la carpeta *Mis Documentos* para guardar tus trabajos.
   * **`umac0_aventura_juegos_15mb.img`:** Aventura y estrategia (Prince of Persia, SimCity 1.11, Tetris oficial, Dark Castle, Stunt Copter, Shufflepuck Café) con más de 8 MB libres para tus partidas guardadas.
   * **`umac0_master_10mb.img`:** Imagen todo-en-uno equilibrada con juegos, dibujo y utilitarios.
4. **Copia el archivo elegido a la raíz de tu MicroSD** y renómbralo exactamente a:
   👉 **`umac0.img`**
5. Inserta la tarjeta MicroSD en el lector de tu PiMac 2040.

---

## 🛠️ 3. Las 2 Versiones de Hardware: ¿Cuál Elegir?

El firmware de PiMac 2040 incorpora un **motor de video inteligente** que soporta tanto pantallas de televisión analógicas como monitores de computadora. Puedes armar tu proyecto en cualquiera de estas dos versiones:

```text
+-------------------------------------------------------------------------------------------------+
|                                 COMPARATIVA DE VERSIONES                                        |
+-------------------------------------------------------------------------------------------------+
| CARACTERÍSTICA                 | VERSIÓN 1: SOLO VIDEO COMPUESTO | VERSIÓN 2: COMPLETA DUAL      |
+--------------------------------+---------------------------------+------------------------------+
| Pantalla compatible            | TV Tubo CRT o pantalla con RCA  | TV Tubo CRT + Monitor VGA PC |
| Conector de video              | 1 conector RCA hembra           | 1 RCA hembra + 1 VGA DE-15   |
| Complejidad de armado          | Muy baja (solo 2 resistencias)  | Media (3 resistencias + VGA) |
| Selección de pantalla          | Automática                      | Con Switch o Jumper (GP0)    |
| MicroSD (Lectura y Escritura)  | Sí                              | Sí                           |
| Puertos USB (Teclado y Ratón)  | Sí                              | Sí                           |
| Costo total de componentes     | Ultrabajo (~4 a 6 USD)          | Muy económico (~6 a 8 USD)   |
+--------------------------------+---------------------------------+------------------------------+
```

---

## 📺 VERSIÓN 1: Versión Simple / Económica (Solo Video Compuesto)

[![Montaje Real PiMac 2040 - Versión 1 Video Compuesto](assets/pimac2040_version1_composite.jpg)](assets/pimac2040_version1_composite.jpg)
*Montaje real de la Versión 1: Conexión de Video Compuesto RCA con divisor resistivo de 560 Ω y 270 Ω, adaptador MicroSD SPI y puertos USB.*

### ¿Cómo funciona?
Esta versión está pensada para conectar el PiMac 2040 directamente a cualquier televisor retro de tubo (CRT), televisor moderno con entrada amarilla de video (AV / RCA), o monitor de seguridad analógico.

El microcontrolador RP2040 genera de forma nativa la señal de video analógica en blanco y negro estándar **NTSC 480i**. Mediante dos resistencias corrientes conectadas a los pines GP8 y GP9, se mezclan digitalmente las señales de sincronismo y los píxeles de video para entregar la señal exacta de 1.0V pico a pico con impedancia de 75 Ω que necesita cualquier televisor.

### Diagrama de Conexión de Video Compuesto:
```text
   RP2040-Zero (Pines)                           Conector RCA Hembra Amarillo
  +--------------------+                         +---------------------------+
  |                    |      560 Ω (Verde-Azul-Marrón)                      |
  |  GP8 (Sync)        +-----[Resistencia 1/4W]----+                         |
  |                    |                           |                         |
  |                    |      270 Ω (Rojo-Morado-Marrón)                     |
  |  GP9 (Video)       +-----[Resistencia 1/4W]----+----> Pin Central (Vivo) |
  |                    |                                                     |
  |  GND (Tierra)      +--------------------------------> Malla Exterior/GND |
  +--------------------+                         +---------------------------+
```

### Lista de Componentes para Comprar (Nombres Técnicos Exactos):
1. **1x Microcontrolador:** Placa de desarrollo **Waveshare RP2040-Zero** (o Tenstar Robot RP2040-Zero).
2. **1x Conector RCA Hembra para Chasis / Panel:** Color amarillo (en inglés: *RCA Female Jack Panel Mount Connector*).
3. **1x Resistencia de 560 Ω (Ohmios):** Película de carbón o metal, 1/4W o 1/8W, 5% de tolerancia (Bandas: Verde - Azul - Marrón - Dorado).
4. **1x Resistencia de 270 Ω (Ohmios):** Película de carbón o metal, 1/4W o 1/8W, 5% de tolerancia (Bandas: Rojo - Morado/Violeta - Marrón - Dorado).
5. **1x Adaptador pasivo MicroSD a SD** (el adaptador plástico que suele venir de regalo con las memorias MicroSD) o 1x Módulo SPI MicroSD de 3.3V.
6. **1x Adaptador OTG USB-C a USB-A Hembra** (para conectar teclado y ratón).

---

## 🖥️ VERSIÓN 2: Versión Completa Dual (Video Compuesto + Monitor VGA)

[![Montaje Real PiMac 2040 - Versión 2 Dual VGA y Compuesto](assets/pimac2040_version2_dual_vga_composite.jpg)](assets/pimac2040_version2_dual_vga_composite.jpg)
*Montaje real de la Versión 2: Conexión Dual con puerto VGA DE-15 (resistencia de 100 Ω), conector RCA, selector SPDT de video y MicroSD SPI.*

### ¿Cómo funciona el Motor Dual Inteligente?
El firmware incorpora detección automática del pin **GP0**:
* **Al encender con GP0 al aire (sin conectar a nada):** El RP2040 arranca en **Modo Video Compuesto**, enviando video NTSC a 15.734 kHz por el conector RCA (ideal para televisores CRT).
* **Al encender con GP0 conectado a masa (GND):** El RP2040 conmuta al instante a **Modo VGA Estándar**, emitiendo señal 640x480 a 60 Hz (31.468 kHz) por el conector VGA DB-15 (ideal para monitores de computadora).

Puedes conectar ambos conectores (RCA y VGA) a la misma placa al mismo tiempo y usar un pequeño interruptor o jumper para alternar entre el monitor de tu escritorio y tu televisor clásico.

### Diagrama de Conexiones Dual (VGA + Compuesto):
```text
   RP2040-Zero (Pines)                           Conector VGA Hembra (DE-15 / DB-15)
  +--------------------+                         +-----------------------------------+
  |  GP26 (Video)      +-----[ 100 Ω (1/4W) ]----+----> Pines 1, 2 y 3 (Rojo, Verde y Azul unidos)
  |  GP27 (VSync)      +-------------------------> Pin 14 (Sincronismo Vertical)
  |  GP29 (HSync)      +-------------------------> Pin 13 (Sincronismo Horizontal)
  |  GND (Masa)        +-------------------------> Pines 5, 6, 7, 8 y 10 (GNDs de Video)
  +--------------------+                         +-----------------------------------+

   SELECTOR DE PANTALLA:
  +--------------------+                         +-----------------------------------+
  |  GP0               +----> [ Interruptor ] ---> GND (Masa General)
  |                    |      Abierto: Inicia en Video Compuesto (TV CRT)
  |                    |      Cerrado: Inicia en VGA (Monitor PC)
  +--------------------+                         +-----------------------------------+

   VIDEO COMPUESTO RCA (Simultáneo):
  +--------------------+                         +-----------------------------------+
  |  GP8 (Sync)        +-----[ 560 Ω (1/4W) ]----+
  |  GP9 (Video)       +-----[ 270 Ω (1/4W) ]----+----> Pin Central Conector RCA
  |  GND (Tierra)      +------------------------------> Malla Exterior Conector RCA
  +--------------------+                         +-----------------------------------+
```

### Lista de Componentes Adicionales para Comprar (Versión 2):
1. **Todo lo de la Versión 1** (RP2040-Zero, conector RCA, resistencias de 560 Ω y 270 Ω, MicroSD y USB).
2. **1x Conector VGA Hembra para Panel/Chasis:** Conector D-Sub DE-15 hembra de 15 pines en 3 filas (en inglés: *VGA DB15 Female 3-Row D-Sub Connector*).
3. **1x Resistencia de 100 Ω (Ohmios):** Película de metal o carbón, 1/4W o 1/8W (Bandas: Marrón - Negro - Marrón - Dorado).
4. **1x Interruptor Deslizante Miniatura SPDT** (de 2 posiciones) o un Jumper de 2 pines (en inglés: *SPDT Mini Slide Switch 3 Pin* o *2.54mm Jumper Cap with Pin Header*).

---

## 💾 4. Conexión de la Tarjeta MicroSD (SPI)

Puedes usar un módulo MicroSD comercial de 3.3V o soldar directamente cables a un **adaptador MicroSD a SD pasivo**:

```text
       RP2040-Zero                               Adaptador SD Pasivo (Pistas Traseras)
   +-----------------------+                    +------------------------------------+
   |   GP5 (CS)            +------------------->| Pista 1 (CD/DAT3)                  |
   |   GP3 (MOSI)          +------------------->| Pista 2 (CMD / MOSI)               |
   |   GND                 +------------------->| Pista 3 (VSS1 / Masa)              |
   |   3V3 (3.3 Voltios)   +------------------->| Pista 4 (VDD)  ¡IMPORTANTE: SOLO 3.3V!
   |   GP2 (SCK)           +------------------->| Pista 5 (CLK / Reloj)              |
   |   GND                 +------------------->| Pista 6 (VSS2 / Masa)              |
   |   GP4 (MISO)          +------------------->| Pista 7 (DAT0 / MISO)              |
   +-----------------------+                    +------------------------------------+
```

> [!CAUTION]
> Conecta la alimentación de la MicroSD **exclusivamente al pin de 3V3 (3.3V)** de la placa RP2040. **NUNCA** la conectes al pin de 5V porque destruirás la tarjeta de memoria.

---

## 🖱️ 5. Conexión de los Puertos USB para Teclado y Ratón

El PiMac 2040 incluye emulación de controlador **USB Host** por hardware (PIO):

```text
       RP2040-Zero                               Conectores USB-A Hembra
   +-----------------------+                    +-------------------------------------+
   |   5V (VBUS)           +------------------->| Pin 1 (+5V Alimentación USB) [Ambos]|
   |                       |                    +-------------------------------------+
   |                       |                    | PUERTO 1 (TECLADO USB):             |
   |   GP10                +----[ 27 Ω ]--------+ Pin 3: D+ (Datos Positivos)         |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP11                +----[ 27 Ω ]--------+ Pin 2: D- (Datos Negativos)         |
   |                       |          |         +-------------------------------------+
   |                       |       [ 15 kΩ ]    | PUERTO 2 (RATÓN USB):               |
   |   GP12                +----[ 27 Ω ]--------+ Pin 3: D+ (Datos Positivos)         |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP13                +----[ 27 Ω ]--------+ Pin 2: D- (Datos Negativos)         |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GND (Tierra)        +----------+---------+ Pin 4: GND (Masa USB) [Ambos]       |
   +-----------------------+                    +-------------------------------------+
```

* **Compatibilidad de periféricos:** Funciona con prácticamente cualquier teclado y ratón USB con cable, o teclados/ratones inalámbricos que usen un receptor USB dongle de 2.4 GHz estándar.
* **Opción USB-C OTG:** También puedes conectar un teclado directamente al puerto USB-C nativo usando un pequeño adaptador OTG USB-C macho a USB-A hembra.

---

## 🚦 6. Diagnóstico con el LED RGB Integrado (GP16)

La placa Waveshare RP2040-Zero incluye un LED RGB integrado (WS2812). El firmware lo utiliza como panel de diagnóstico en tiempo real:

| Color del LED | Comportamiento | Significado |
| :--- | :--- | :--- |
| 🟧 **Naranja suave** | Pulso lento | Arrancando el sistema y leyendo la ROM del Mac Plus. |
| 🟩 **Verde continuo** | Respiración suave | **¡Sistema listo!** El escritorio de Finder está activo y esperando tus órdenes. |
| 🟨 **Ámbar brillante** | Destellos rápidos | Leyendo bloques de datos desde la tarjeta MicroSD. |
| 🟪 **Magenta brillante**| Destellos rápidos | **Grabando datos en la MicroSD:** Guardando un archivo, partida o dibujo. |
| 🔴 **Rojo continuo** | Parpadeo de alarma | Error de MicroSD: revisa el cableado SPI o que la tarjeta esté en FAT32 con el archivo `umac0.img`. |

---

## 🔋 7. Cómo Alimentar el Circuito

1. **Por cable USB-C:** La forma más simple. Conecta el puerto USB-C de la RP2040-Zero a un cargador de pared de teléfono (5V / 1A o 2A).
2. **Por fuente de alimentación fija de 5V:** Conecta el polo positivo de 5V al pin marcado como **`5V` (VBUS)** y el polo negativo al pin **`GND`**.
3. **Por batería recargable (Portátil):** Puedes conectar una batería de litio 18650 (3.7V) mediante un módulo de carga y elevador **TP4056 con Booster de 5V integrado**, alimentando el pin `5V` y `GND` de la placa.

---

## 📜 Licencia Abierta y Créditos

Este proyecto es software y hardware de código abierto, distribuido bajo la **Licencia MIT**. Eres libre de usarlo, estudiarlo, mejorarlo y compartirlo libremente.

Desarrollado, optimizado y documentado con dedicación por **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl)). Te agradecemos mantener una mención a este sitio web en cualquier versión o proyecto derivado.
