# PiMac 2040 (Macintosh 208K) — Guía Oficial de Instalación y Hardware
### Proyecto de Código y Hardware Abierto por [SCHUBIGER.CL](https://schubiger.cl)
### Licencia MIT — Libre para Usar, Modificar y Compartir

¡Bienvenido a **PiMac 2040**! Esta guía está redactada en un lenguaje simple, directo y práctico para que cualquier persona —incluso sin experiencia previa en microcontroladores— pueda instalar el sistema en una placa **RP2040**, armar su circuito en minutos y revivir la experiencia completa de una computadora Apple Macintosh clásica con ratón, teclado, tarjeta MicroSD y salida de video para televisores o monitores.

---

## ⚡ 1. Instalación Rápida del Sistema en el RP2040 (En 3 Pasos)

No necesitas instalar programas complejos ni compilar código fuente. El firmware ya está compilado y listo para usar en el archivo **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**:

```text
  [ Archivo .UF2 ]  ------------------------->  [ Unidad RPI-RP2 ]  ---> ¡Instalado!
  (Firmware PiMac 2040)       Arrastrar y soltar       (RP2040 en modo Boot)       (Se reinicia en 2 seg)
```

1. **Conectar en modo Boot:** Toma tu placa **Waveshare RP2040-Zero** (o Raspberry Pi Pico). Mantén presionado el botón blanco **BOOT** (o BOOTSEL) de la placa y, sin soltarlo, conéctala a tu computadora con el cable USB-C. Luego suelta el botón.
2. **Aparición de la unidad:** En tu computadora aparecerá automáticamente una nueva unidad de disco extraíble llamada **`RPI-RP2`** (exactamente igual a cuando conectas un pendrive USB).
3. **Copiar el archivo:** Arrastra y suelta dentro de la unidad `RPI-RP2` el archivo:
   👉 **`PiMac2040_DualVideo_RP2040Zero.uf2`**
4. **¡Listo!** En 2 segundos la placa parpadeará, la ventana se cerrará sola y el sistema PiMac 2040 quedará instalado permanentemente en la memoria Flash del microcontrolador.

---

## 💾 2. Preparar la Tarjeta MicroSD con los Discos y Aplicaciones

1. Toma cualquier tarjeta MicroSD (desde 256 MB hasta 32 GB).
2. Conéctala a tu PC y formatéala en formato **FAT32** (Formato rápido).
3. Entra en la carpeta **`disks/`** y elige el disco que quieras usar:
   * **`umac0_oficina_almacenamiento_20mb.img`:** Suite de oficina completa (Microsoft Word 4.0, Excel 2.2, Works 3.0, PageMaker 2.0, MacPaint, MacDraw) con más de 10 MB libres en la carpeta *Mis Documentos* para guardar tus trabajos.
   * **`umac0_aventura_juegos_15mb.img`:** Aventura y estrategia (Prince of Persia, SimCity 1.11, Tetris oficial, Dark Castle, Stunt Copter, Shufflepuck Café) con espacio para guardar partidas.
   * **`umac0_master_10mb.img`:** Suite todo-en-uno de acción y arcade.
4. **Copia el archivo elegido a la raíz de tu MicroSD y renómbralo a:**
   👉 **`umac0.img`**
5. Inserta la tarjeta MicroSD en el adaptador o lector conectado a la placa.

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
| MicroSD (Lectura y Escritura)  | SÍ                              | SÍ                           |
| Puertos USB (Teclado y Ratón)  | SÍ                              | SÍ                           |
| Costo total de componentes     | Ultrabajo (~4 a 6 USD)        | Muy económico (~6 a 8 USD) |
+--------------------------------+---------------------------------+------------------------------+
```

---

## 📺 VERSIÓN 1: Versión Simple / Económica (Solo Video Compuesto)

![Montaje Real PiMac 2040 - Versión 1 Video Compuesto](assets/pimac2040_version1_composite.jpg)
*Montaje real de la Versión 1: Conexión de Video Compuesto RCA con divisor resistivo de 560 Ω y 270 Ω, adaptador MicroSD SPI y puertos USB.*

### ¿Cómo funciona?
Esta versión está pensada para conectar el PiMac 2040 directamente a cualquier televisor retro de tubo (CRT), televisor moderno con entrada amarilla de video (AV / RCA), o monitor de seguridad analógico.

El microcontrolador RP2040 genera de forma nativa la señal de video analógica en blanco y negro estándar **NTSC 480i**. Mediante dos resistencias corrientes conectadas a los pines GP8 y GP9, se mezclan digitalmente las señales de sincronismo y los píxeles de video para entregar la señal exacta de 1.0V pico a pico con impedancia de 75 Ω que necesita cualquier televisor.

### Diagrama de Conexión de Video Compuesto:
```text
      Placa RP2040-Zero                             Conector RCA Hembra
   +---------------------+                        +---------------------+
   |                     |                        |                     |
   |   GP8 (Sync)        +-----[ Resistencia ]----+                     |
   |                     |          560 Ω         |                     |
   |                     |                        +--> PIN CENTRAL RCA  |
   |   GP9 (Video)       +-----[ Resistencia ]----+    (Entrada Video TV)
   |                     |          270 Ω         |                     |
   |   GND (Tierra)      +---------------------------> MALLA EXTERIOR   |
   |                     |                             (Tierra / Masa)  |
   +---------------------+                        +---------------------+
```

### Lista de Componentes para Comprar (Nombres Técnicos Exactos):
1. **Placa Microcontroladora:**
   * Nombre técnico: *Módulo RP2040-Zero (Tenstar Robot / Waveshare o genérico chino)*. Es la placa con RP2040 más compacta y económica del mercado (~18 x 23.5 mm, PCB morada/azul con puerto USB-C y pads almenados dorados).
2. **Conector de Video:**
   * Nombre técnico: *Conector RCA hembra para chasis* (color amarillo, con tuerca de fijación) o *Jack RCA hembra para PCB*.
3. **Resistencias de Video (2 unidades):**
   * 1x *Resistencia de película metálica de 560 Ω (óhmios) a 1/4W (0.25W), tolerancia 5% o 1%* (Si no encuentras de 560 Ω, sirve de 470 Ω).
   * 1x *Resistencia de película metálica de 270 Ω (óhmios) a 1/4W (0.25W), tolerancia 5% o 1%* (Si no encuentras de 270 Ω, sirve de 240 Ω).
4. **Ranura de Tarjeta MicroSD (DIY Directo):**
   * Opción A (Recomendada y sin costo extra): *Adaptador pasivo plástico de MicroSD a SD* (el adaptador negro que viene incluido gratis en los paquetes de tarjetas MicroSD). Se raspa ligeramente el barniz y se sueldan 6 cables finos directamente a sus pistas doradas traseras, conectándolos a la placa RP2040-Zero sin gastar en módulos adicionales.
   * Opción B: *Módulo lector MicroSD SPI de 3.3V* comercial.
5. **Puertos USB para Teclado y Ratón (Dos métodos a elección):**
   * **Método 1 (Puertos físicos reciclados o sueltos):** 2x *Conectores USB-A hembra* (pueden ser reciclados o desoldados de placas madre/cables viejos, o comprados sueltos tipo DIP/chasis) + 4 resistencias de 27 Ω y 4 resistencias de 15 kΩ conectadas a los pines GP10, GP11, GP12 y GP13.
   * **Método 2 (Adaptador OTG directo por USB-C):** Puedes conectar un *adaptador USB-C a USB-A OTG* miniatura directamente al puerto USB-C de la placa RP2040-Zero junto con un mini-hub USB pasivo, ahorrándote soldar resistencias USB.
6. **Opciones de Alimentación Eléctrica:**
   * **Por cable USB-C:** Conectando a cualquier cargador de celular estándar de 5V (1A o 2A).
   * **Alimentación directa por pines (Batería o Fuente 5V):** Puedes soldar cables directamente a los pines **5V (Pin 20 - VBUS)** y **GND (Pin 19)** de la RP2040-Zero para alimentar todo el proyecto con una batería de litio 18650 usando un módulo elevador booster TP4056 a 5V.

---

## 🖥️ VERSIÓN 2: Versión Completa Dual (Video Compuesto + Monitor VGA)

![Montaje Real PiMac 2040 - Versión 2 Dual VGA y Compuesto](assets/pimac2040_version2_dual_vga_composite.jpg)
*Montaje real de la Versión 2: Conexión dual completa con conector VGA DE-15 (DB-15), conector RCA, selector de modo y periféricos.*

### ¿Cómo funciona el Motor Dual Inteligente?
Esta versión incluye tanto el puerto RCA como un conector VGA estándar de 15 pines. Te permite utilizar el PiMac 2040 en un televisor retro de living o llevarlo a tu escritorio y conectarlo a un monitor de computadora CRT o pantalla LCD/LED con entrada VGA a **640x480 @ 60Hz**.

El firmware lee el estado del pin **GP0** en cada arranque:
* **Sin Jumper en GP0 (Pin libre al aire / Switch apagado):** El sistema activa la resistencia interna de *pull-up* del RP2040 (3.3V) y genera la señal de **Video Compuesto (TV CRT)** por GP8 y GP9.
* **Con Jumper en GP0 a GND (Pin conectado a masa / Switch encendido):** El sistema detecta 0V y conmuta automáticamente los generadores PIO para emitir **Video VGA con sincronismos HSync y VSync** por los pines GP26, GP27 y GP29.

### Diagrama de Conexiones Dual (VGA + Compuesto):

```text
       Placa RP2040-Zero                             Conector VGA DE-15 (DB-15) Hembra
   +-----------------------+                        +---------------------------------+
   |                       |                        | Pin 1: Red (Rojo)       \       |
   |   GP26 (Video)        +-----[ Resistencia ]----+ Pin 2: Green (Verde)     + Unidos
   |                       |       100 Ω a 120 Ω    | Pin 3: Blue (Azul)      /       |
   |                       |                        |                                 |
   |   GP27 (VSync)        +----------------------->| Pin 14: Sincronismo Vertical    |
   |   GP29 (HSync)        +----------------------->| Pin 13: Sincronismo Horizontal  |
   |   GND (Tierra)        +----------------------->| Pines 5, 6, 7, 8 y 10: Masa GND |
   |                       |                        +---------------------------------+
   |                       |
   |                       |                        Selector de Modo (Jumper o Switch)
   |   GP0 (Selector)      +----+                   +---------------------------------+
   |                       |    |                   | [ Abierto / OFF ] = Video RCA   |
   |   GND                 +----+---[ Switch ]----->| [ Cerrado / ON  ] = Monitor VGA |
   |                       |                        +---------------------------------+
   |                       |
   |                       |                        Conector RCA Hembra (TV Compuesto)
   |                       |                        +---------------------------------+
   |   GP8 (Sync)          +-----[ Res. 560 Ω ]-----+                                 |
   |   GP9 (Video)         +-----[ Res. 270 Ω ]-----+--> PIN CENTRAL RCA (Video TV)   |
   |   GND (Tierra)        +---------------------------> MALLA EXTERIOR RCA (GND)     |
   +-----------------------+                        +---------------------------------+
```

> [!NOTE]
> Al unir los pines 1, 2 y 3 (Rojo, Verde y Azul) del conector VGA, el monitor reproducirá la imagen clásica en blanco y negro puro, idéntica a la pantalla integrada original del Macintosh Plus de 1986.

### Lista de Componentes Adicionales para Comprar (Versión 2):
1. **Conector VGA:**
   * Nombre técnico: *Conector D-Sub DE-15 hembra de 15 pines en 3 filas* (comúnmente vendido como *Conector VGA DB15 hembra para chasis con postes roscados* o *Conector VGA hembra para circuito impreso*).
2. **Resistencia para VGA:**
   * 1x *Resistencia de película metálica de 100 Ω o 120 Ω a 1/4W (0.25W), 1% o 5%* (adapta el nivel de voltaje de 3.3V a los 0.7V estándar de video analógico VGA).
   * (Opcional recomendado) 2x *Resistencias de 100 Ω a 1/4W* colocadas en serie en las líneas GP27 y GP29 para proteger los sincronismos contra sobrecorriente.
3. **Interruptor o Selector de Modo:**
   * Nombre técnico: *Interruptor deslizante miniatura SPDT (1 polo, 2 posiciones)* O *Cabezal de pines macho 1x2 (paso 2.54 mm) con Jumper Shunt extraíble*.

---

## 🔌 4. Conexión de la Tarjeta MicroSD (SPI)

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

* **Compatibilidad de periféricos:** Funciona con prácticamente cualquier teclado y ratón USB con cable, o teclados/ratones inalámbricos que usen un receptor USB dongle de 2.4 GHz estándar (como los kits de Logitech, Genius, etc.).

---

## 💡 6. Diagnóstico con el LED RGB Integrado (GP16)

La placa Waveshare RP2040-Zero incluye un LED RGB integrado (WS2812). El firmware lo utiliza como panel de diagnóstico en tiempo real:

| Color del LED | Comportamiento | Significado |
| :--- | :--- | :--- |
| 🟠 **Naranja suave** | Pulso lento | Arrancando el sistema y leyendo la ROM del Mac Plus. |
| 🟢 **Verde continuo** | Respiración suave | **¡Sistema listo!** El escritorio de Finder está activo y esperando tus órdenes. |
| 🟡 **Ámbar brillante** | Destellos rápidos | Leyendo bloques de datos desde la tarjeta MicroSD. |
| 🟣 **Magenta brillante**| Destellos rápidos | **Grabando datos en la MicroSD:** Guardando un archivo, partida o dibujo. |
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
