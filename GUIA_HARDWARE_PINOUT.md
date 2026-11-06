# PiMac 2040 - Guía Completa de Conexiones y Pinout Hardware
### Ingeniería y Diseño por [SCHUBIGER.CL](https://schubiger.cl)

Esta guía explica en detalle cómo conectar todos los periféricos a la placa **RP2040-Zero** para construir la computadora retro **PiMac 2040**, permitiendo salida de **Video Compuesto (TV antiguo)**, salida **VGA (Monitor CRT/LCD)**, ranura **MicroSD** de lectura/escritura y **puertos USB** directos.

---

## 🗺️ 1. Mapa Físico de Pines de la RP2040-Zero

La placa **RP2040-Zero** (Tenstar Robot / Waveshare) expone pines laterales y pads inferiores. A continuación se muestra la correspondencia física exacta vista de frente con el conector USB-C arriba:

`text
                               +-------------------+
                               |     [ USB-C ]     |
                               +-------------------+
  (Alimentación 5V / Bat) 5V [ | (o)           (o) | ] 0   GP0 (Selector VGA / RCA)
  (Masa / Tierra General)GND [ | (o)           (o) | ] 1   GP1 (Libre)
  (Alimentación MicroSD) 3V3 [ | (o)  +-----+  (o) | ] 2   GP2 (SD SCK - Reloj)
  (HSync VGA DB-15 p.13)  29 [ | (o)  | RP  |  (o) | ] 3   GP3 (SD MOSI - Cmd)
  (Libre / Opcional)      28 [ | (o)  |2040 |  (o) | ] 4   GP4 (SD MISO - Dat0)
  (VSync VGA DB-15 p.14)  27 [ | (o)  +-----+  (o) | ] 5   GP5 (SD CS - Chip Select)
  (Video VGA 100Ω p.1,2,3)26 [ | (o)           (o) | ] 6   GP6 (Libre)
  (Libre)                 15 [ | (o) [BOOT] [RST] (o)| ] 7   GP7 (Libre)
  (Libre)                 14 [ | (o)           (o) | ] 8   GP8 (CVBS Sync 560Ω -> RCA)
                               +-------------------+
                                  13  12  11  10  9
                                   |   |   |   |  +--> GP9  (CVBS Video 270Ω -> RCA)
                                   |   |   |   +-----> GP10 (USB Teclado D+)
                                   |   |   +---------> GP11 (USB Teclado D-)
                                   |   +-------------> GP12 (USB Mouse D+)
                                   +-----------------> GP13 (USB Mouse D-)
`

---

## 📋 2. Tabla Maestra de Conexiones

| Pin RP2040-Zero | Función en PiMac 2040 | Componentes Requeridos | Conexión Destino |
| :--- | :--- | :--- | :--- |
| **GP0** | **Selector de Modo de Video** | Jumper o Switch a GND | • **Abierto (Sin Jumper):** Video Compuesto (TV CRT)<br>• **Cerrado a GND:** Salida VGA (Monitor PC) |
| **GP8** | **Sync Compuesto (CVBS)** | Resistencia **560 Ω** (1/4 W) | Pin central de conector RCA hembra |
| **GP9** | **Data Compuesto (CVBS)** | Resistencia **270 Ω** (1/4 W) | Pin central de conector RCA hembra |
| **GND** | **Malla Blindaje RCA** | Cable directo | Malla exterior del conector RCA |
| **GP26** | **Video Monocromo VGA** | Resistencia **100 Ω a 120 Ω** | Pines 1, 2 y 3 (Rojo, Verde y Azul unidos) de VGA DB-15 |
| **GP27** | **Sincronismo Vertical VGA** | Conexión directa (o 100 Ω) | Pin 14 (VSync) del conector VGA DB-15 |
| **GP29** | **Sincronismo Horizontal VGA**| Conexión directa (o 100 Ω) | Pin 13 (HSync) del conector VGA DB-15 |
| **GND** | **Masa / Tierra VGA** | Cable directo | Pines 5, 6, 7, 8 y 10 del conector VGA DB-15 |
| **GP2** | **MicroSD SPI SCK (Reloj)** | Cable directo | Pin 5 (CLK) del adaptador MicroSD |
| **GP3** | **MicroSD SPI TX (MOSI)** | Cable directo | Pin 2 (CMD) del adaptador MicroSD |
| **GP4** | **MicroSD SPI RX (MISO)** | Cable directo | Pin 7 (DAT0) del adaptador MicroSD |
| **GP5** | **MicroSD SPI CS (Chip Select)**| Cable directo | Pin 1 (CD/DAT3) del adaptador MicroSD |
| **3V3** | **Alimentación MicroSD** | Cable directo | Pin 4 (VDD) del adaptador MicroSD *(¡NUNCA 5V!)* |
| **GND** | **Masa MicroSD** | Cable directo | Pines 3 y 6 (VSS) del adaptador MicroSD |
| **GP10** | **USB Host 1 D+ (Teclado)** | Resistencia **27 Ω** + **15 kΩ** a GND | Pin 3 (D+) de conector USB-A hembra 1 |
| **GP11** | **USB Host 1 D- (Teclado)** | Resistencia **27 Ω** + **15 kΩ** a GND | Pin 2 (D-) de conector USB-A hembra 1 |
| **GP12** | **USB Host 2 D+ (Mouse)** | Resistencia **27 Ω** + **15 kΩ** a GND | Pin 3 (D+) de conector USB-A hembra 2 |
| **GP13** | **USB Host 2 D- (Mouse)** | Resistencia **27 Ω** + **15 kΩ** a GND | Pin 2 (D-) de conector USB-A hembra 2 |
| **5V (VBUS)** | **Alimentación USBs** | Cable directo | Pin 1 (+5V) de ambos conectores USB-A hembra |
| **GND** | **Masa USBs** | Cable directo | Pin 4 (GND) de ambos conectores USB-A hembra |
| **GP16** | **LED de Estado RGB** | Interno en PCB | LED WS2812 de estado dinámico del sistema |

---

## 📺 3. Conexión de Video Compuesto (TV Antiguo / Tubo CRT)

![Esquema de Montaje Video Compuesto](assets/pimac2040_version1_composite.jpg)

Genera señal analógica estándar NTSC monocromática en blanco y negro para cualquier televisor o monitor con entrada de video RCA amarillo:

```text
       RP2040-Zero
    +-----------------+
    |  GP8 (Sync)     +-------[ 560Ω (o 470Ω) ]-------+
    |                 |                               |
    |  GP9 (Data)     +-------[ 270Ω (o 240Ω) ]-------+-----> PIN CENTRAL RCA (Amarillo)
    |                 |                                       (Entrada Video TV CRT)
    |  GND            +-------------------------------------> MALLA EXTERIOR RCA (GND)
    +-----------------+
```

---

## 🖥️ 4. Conexión de Salida VGA (Monitor de PC)

![Esquema de Montaje Dual VGA y Compuesto](assets/pimac2040_version2_dual_vga_composite.jpg)

Para conectar a monitores de computadora CRT o pantallas planas con entrada VGA DB-15:

```text
       RP2040-Zero                                Conector VGA DB-15 Hembra
    +-----------------+                          +----------------------------+
    |  GP26 (Video)   +-----[ 100Ω a 120Ω ]----+ | Pin 1: Red (Rojo)          |
    |                 |                        +-+ Pin 2: Green (Verde)       |
    |                 |                        +-+ Pin 3: Blue (Azul)         |
    |                 |                          |                            |
    |  GP27 (VSync)   +------------------------->| Pin 14: VSync (Vertical)   |
    |                 |                          |                            |
    |  GP29 (HSync)   +------------------------->| Pin 13: HSync (Horizontal) |
    |                 |                          |                            |
    |  GND            +------------------------->| Pines 5, 6, 7, 8, 10: GND  |
    +-----------------+                          +----------------------------+
```

### 🔘 Selección Automática de Modo de Video (Jumper en GP0):
* **Sin jumper en GP0 (Pin 1 libre al aire):** El microcontrolador activa su resistencia interna de pull-up (3.3V) y arranca en **Modo Video Compuesto (TV CRT 480i NTSC)**.
* **Con jumper entre GP0 y GND (Pin 1 a Pin 19):** Al detectar 0V, el microcontrolador conmuta automáticamente e inicializa el motor **VGA (640x480 @ 60Hz)**.

---

## 💾 5. Soldadura Directa a Adaptador SD a MicroSD Pasivo

No compres módulos SD para Arduino; cualquier adaptador convencional MicroSD-a-SD es $100\%$ pasivo. Al soldar cables directos a sus pistas doradas, obtienes un zócalo ultraeconómico y de perfil plano:

### Vista Posterior del Adaptador SD (Contactos hacia arriba):
```text
      +-----------------------------------------+
      |  [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]    |
      |   9   1   2   3   4   5   6   7   8     |
      |       |   |   |   |   |   |   |         |
      |      CS  MOSI GND VDD SCK GND MISO      |
      |                                         |
      |      ADAPTADOR SD A MICROSD PASIVO      |
      |         (Ranura MicroSD aquí)           |
      +-------------------vvvvv-----------------+
```

* **Paso 1:** Con la punta de un cúter o lija muy fina, raspa ligeramente el barniz dorado de las pistas 1, 2, 3, 4, 5, 6 y 7 del adaptador.
* **Paso 2:** Aplica una gota minúscula de estaño con flux en cada pista.
* **Paso 3:** Suelda cables finos (AWG 28 o AWG 30) conectando:
  - **Pista 1** $\rightarrow$ **GP5** (CS)
  - **Pista 2** $\rightarrow$ **GP3** (MOSI)
  - **Pista 3** $\rightarrow$ **GND** (Masa)
  - **Pista 4** $\rightarrow$ **3V3** (¡IMPORTANTE: Alimentación a 3.3V, NUNCA a 5V!)
  - **Pista 5** $\rightarrow$ **GP2** (SCK)
  - **Pista 6** $\rightarrow$ **GND** (Masa)
  - **Pista 7** $\rightarrow$ **GP4** (MISO)
* **Paso 4:** Coloca una gota de pegamento caliente (silicona caliente) sobre las soldaduras para asegurar los cables mecánicamente contra tirones.

---

## 🔌 6. Conexión de Puertos USB para Teclado y Ratón

```text
       RP2040-Zero                                Conectores USB-A Hembra
    +-----------------+                          +-----------------------------+
    |  5V (VBUS)      +------------------------->| Pin 1: VBUS (5V) [Ambos]    |
    |                 |                          +-----------------------------+
    |                 |                          | PUERTO 1 (TECLADO):         |
    |  GP10           +----[ 27Ω ]---------------+ Pin 3: D+ (Teclado)         |
    |                 |            |             |                             |
    |                 |          [ 15kΩ ]        |                             |
    |                 |            |             |                             |
    |  GP11           +----[ 27Ω ]-|-------------+ Pin 2: D- (Teclado)         |
    |                 |            |   |         +-----------------------------+
    |                 |              [ 15kΩ ]    | PUERTO 2 (RATÓN):           |
    |  GP12           +----[ 27Ω ]-|---|---------+ Pin 3: D+ (Ratón)           |
    |                 |            |   |   |     |                             |
    |                 |                  [ 15kΩ ]|                             |
    |                 |                    |     |                             |
    |  GP13           +----[ 27Ω ]---------|-----+ Pin 2: D- (Ratón)           |
    |                 |                    | |   |                             |
    |                 |                    [ 15kΩ]                             |
    |                 |                      |   |                             |
    |  GND            +----------------------+---+ Pin 4: GND [Ambos]          |
    +-----------------+                          +-----------------------------+
```

---

## 🔋 7. Opciones de Alimentación Eléctrica

1. **Alimentación por USB-C:** Puedes alimentar todo el circuito simplemente conectando el cable USB-C de la placa a un cargador de celular estándar de 5V (1A o 2A).
2. **Alimentación Directa por 5V Fijo:** Conecta el positivo de tu fuente externa de 5V al pin **`5V` (VBUS)** y el negativo al pin **`GND`**.
3. **Alimentación por Batería de Litio (Li-Ion 3.7V / 18650):** Conecta la batería a un módulo **TP4056 con Booster a 5V**, y la salida de 5V del módulo al pin **`5V`** y **`GND`** de la placa. Así mantendrás 5V constantes para el teclado y mouse USB mientras la batería se descarga.
