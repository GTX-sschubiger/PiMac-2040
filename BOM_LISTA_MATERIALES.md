# PiMac 2040 - Lista de Materiales (BOM) y Dónde Comprar Económico
### Proyecto desarrollado por [SCHUBIGER.CL](https://schubiger.cl)

El objetivo de este proyecto es construir una réplica funcional del **Apple Macintosh 128K / Plus de 1984** con soporte de **Video Compuesto (TV CRT) y VGA**, ranura **MicroSD** y **puertos USB**, por un costo total de **entre $5 y $8 dólares estadounidenses (USD)** utilizando componentes estándar disponibles en **AliExpress**, Amazon o tiendas de electrónica locales.

---

## 🛒 Lista de Componentes y Presupuesto

| Componente | Cantidad | Descripción Técnica | Precio Estimado (AliExpress) | Términos de Búsqueda Recomendados |
| :--- | :---: | :--- | :---: | :--- |
| **RP2040-Zero** | 1 | Placa microcontroladora mini basada en Raspberry Pi RP2040 (conector USB-C, 2MB Flash, LED RGB WS2812). | **$1.50 - $2.20 USD** | `RP2040-Zero`, `Waveshare RP2040-Zero mini`, `RP2040 Zero Type-C` |
| **Adaptador SD a MicroSD** | 1 | Adaptador plástico pasivo convencional de MicroSD a SD estándar (el que viene de regalo en los paquetes de tarjetas). | **$0.00 - $0.50 USD** | `Micro SD to SD card adapter`, o reutilizar uno en desuso |
| **Tarjeta MicroSD** | 1 | Cualquier tarjeta MicroSD de 512 MB, 1 GB, 2 GB, 4 GB, 8 GB, 16 GB o 32 GB formateada en **FAT32**. | **$2.00 - $3.00 USD** | `MicroSD card 8GB FAT32`, `TF card Class 10` |
| **Conector RCA Hembra** | 1 | Conector de chasis tipo RCA hembra (color amarillo) o punta cortada de un cable de video RCA viejo. | **$0.25 - $0.40 USD** | `RCA female jack chassis`, `RCA panel mount yellow` |
| **Conector VGA DB-15 Hembra** | 1 | *(Opcional)* Conector hembra DB-15 de 3 filas para montaje en chasis (para conectar a monitor de PC). | **$0.40 - $0.60 USD** | `VGA DB15 female connector 3 row`, `D-SUB 15 pin female` |
| **Conectores USB-A Hembra** | 2 | *(Opcional)* Conectores hembra USB Tipo A para chasis o soldadura directa (para teclado y ratón). | **$0.30 - $0.50 USD** (pack de 5) | `USB Type A female connector dip`, `USB 2.0 female jack` |
| **Kit de Resistencias 1/4W** | 1 kit | Resistencias de película metálica o carbón de 1/4W (o 1/8W):<br>• 1x **560 Ω** (o 470 Ω)<br>• 1x **270 Ω** (o 240 Ω)<br>• 1x **100 Ω a 120 Ω**<br>• 4x **27 Ω** (o 22 Ω a 33 Ω)<br>• 4x **15 kΩ** (o 10 kΩ a 15 kΩ) | **$0.30 USD** | `1/4W metal film resistors pack 560 270 27 15k` |
| **Cable fino para conexiones** | 1 metro | Cable de cobre delgado tipo AWG 28 o AWG 30 (cable wrapping o cable de faja IDE antiguo). | **$0.40 USD** | `AWG 30 wrapping wire`, `30AWG jumper wire` |
| **Módulo de Batería (Opcional)** | 1 | *(Opcional)* Módulo cargador de litio TP4056 con elevador a 5V para alimentar con batería Li-Ion 18650. | **$0.80 - $1.20 USD** | `TP4056 with 5V booster step up`, `18650 battery power shield` |

---

## 🔍 Dónde y Cómo Encontrar los Componentes de Manera Económica

### 1. Placa RP2040-Zero (El corazón del proyecto)
* **Dónde buscar:** En **AliExpress** escribe en el buscador: `"RP2040-Zero"`.
* **Precio objetivo:** Entre **$1.40 y $2.00 USD**. Generalmente se encuentra en la sección *Choice* de AliExpress con envío gratis a partir de \$10 de compra combinada.
* **Fabricantes habituales:** Waveshare original o clones de marcas genéricas (Yingkewei, Tenstar Robot, etc.). Todos usan el silicio original **Raspberry Pi RP2040** y son $100\%$ compatibles pin a pin.
* **Importante:** Asegúrate de que tenga el puerto **USB-C** y los 20 pines exteriores almenados (*castellated pads*).

### 2. Lector MicroSD Gratis (Hack con Adaptador SD)
* No compres módulos comerciales de Arduino (esos módulos traen reguladores a 5V que añaden costo y tamaño innecesario).
* Busca en tu casa cualquier adaptador plástico negro que diga **"MicroSD to SD Adapter"** (SanDisk, Kingston, Samsung, etc.). Todos son $100\%$ pasivos y permiten soldar cables directos a sus pistas doradas posteriores.

### 3. Conectores de Video y Resistencias
* Si no quieres comprar conectores de chasis nuevos:
  * Puedes cortar la punta de un cable RCA amarillo viejo de un reproductor de DVD o consola vieja.
  * Puedes desoldar un conector VGA DB-15 hembra de una tarjeta de video rota o placa madre antigua de PC.
  * Las resistencias estándar de 1/4W cuestan centavos o se pueden reciclar de cualquier aparato electrónico en desuso.

---

## ⚡ Herramientas Mínimas Recomendadas

* **Cautín / Soldador:** De punta fina (25W a 40W o temperatura regulable a 300°C - 330°C).
* **Estaño fino:** Preferiblemente con núcleo de resina/flux (60/40 o libre de plomo de 0.6mm a 0.8mm).
* **Cúter o lija al agua fina:** Para raspar el esmalte de las almohadillas del adaptador MicroSD.
* **Pistola de silicona caliente (Hot Glue) o cinta Kapton:** Para fijar los cables al adaptador y evitar tirones.
* **Multímetro básico:** Para comprobar continuidad y verificar que no hayan quedado puentes de estaño accidentales entre pines contiguos.
