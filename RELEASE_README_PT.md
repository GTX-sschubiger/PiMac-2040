# PiMac 2040 (Macintosh 208K) – Guia Oficial de Instalação e Hardware
### Projeto de Código e Hardware Aberto por [SCHUBIGER.CL](https://schubiger.cl)
### Licença MIT – Livre para Usar, Modificar e Compartilhar

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="RELEASE_README.md">🇪🇸 Español</a> |
  <a href="RELEASE_README_EN.md">🇬🇧 English</a> |
  <a href="RELEASE_README_PT.md"><strong>🇵🇹 Português</strong></a> |
  <a href="RELEASE_README_DE.md">🇩🇪 Deutsch</a> |
  <a href="RELEASE_README_ZH.md">🇨🇳 中文</a> |
  <a href="RELEASE_README_FR.md">🇫🇷 Français</a>
</p>


Bem-vindo ao **PiMac 2040**! Este guia foi redigido em linguagem simples, direta e prática para que qualquer pessoa — mesmo sem experiência prévia em microcontroladores — possa instalar o sistema em uma placa **RP2040**, montar seu circuito em minutos e reviver a experiência completa de um computador clássico Apple Macintosh de 1984 com mouse, teclado, cartão MicroSD e saída de vídeo para televisores ou monitores de computador.

---

## ⚡ 1. Instalação Rápida do Sistema no RP2040 (Em 3 Passos)

Não é necessário instalar ferramentas complexas nem compilar código-fonte. O firmware já está compilado e pronto para uso no arquivo **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**:

```text
  [ Arquivo .UF2 ]  ------------------------->  [ Unidade RPI-RP2 ]  ---> Instalado!
  (Firmware PiMac 2040)        Arrastar e soltar         (RP2040 em modo Boot)      (Reinicia em 2 seg)
```

1. **Conectar em modo Boot:** Pegue sua placa **Waveshare / Tenstar Robot RP2040-Zero** (ou Raspberry Pi Pico). Mantenha pressionado o botão branco **BOOT** (ou BOOTSEL) da placa e, sem soltá-lo, conecte-a ao computador com o cabo USB-C. Em seguida, solte o botão.
2. **Aparecimento da unidade:** No computador aparecerá automaticamente uma unidade de disco removível chamada **`RPI-RP2`** (exatamente igual a um pendrive USB comum).
3. **Copiar o arquivo:** Arraste e solte dentro da unidade `RPI-RP2` o arquivo:
   👉 **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**
4. **Pronto!** Em 2 segundos o LED da placa piscará, a janela fechará sozinha e o PiMac 2040 estará instalado permanentemente na memória Flash do microcontrolador.

---

## 💾 2. Preparar o Cartão MicroSD com os Discos e Aplicativos

1. Pegue qualquer cartão MicroSD (de 256 MB até 32 GB).
2. Conecte-o ao seu PC e formate-o no formato **FAT32** (Formatação rápida).
3. Acesse a pasta **`disks/`** e escolha o disco que deseja utilizar:
   * **`umac0_oficina_almacenamiento_20mb.img`:** Pacote de escritório completo (Word 4.0, Excel 2.2, Works 3.0, PageMaker 2.0, MacPaint, MacDraw) com mais de 10 MB livres na pasta *Meus Documentos* para salvar trabalhos de forma persistente.
   * **`umac0_aventura_juegos_15mb.img`:** Aventura e estratégia (Prince of Persia, SimCity 1.11, Tetris oficial, Dark Castle, Stunt Copter, Shufflepuck Café) com mais de 8 MB livres para saves.
   * **`umac0_master_10mb.img`:** Imagem equilibrada tudo-em-um com jogos, aplicativos de desenho e utilitários.
4. **Copie o arquivo escolhido para a raiz do seu cartão MicroSD** e renomeie-o exatamente para:
   👉 **`umac0.img`**
5. Insira o cartão MicroSD no leitor do seu PiMac 2040.

---

## 🛠️ 3. As 2 Versões de Hardware: Qual Escolher?

O firmware do PiMac 2040 conta com um **motor de vídeo inteligente** que suporta tanto telas analógicas de TV quanto monitores de PC. Você pode montar seu circuito em qualquer uma destas opções:

```text
+-------------------------------------------------------------------------------------------------+
|                                 COMPARAÇÃO DAS VERSÕES                                          |
+-------------------------------------------------------------------------------------------------+
| CARACTERÍSTICA                 | VERSÃO 1: APENAS VÍDEO COMPOSTO | VERSÃO 2: COMPLETA DUAL      |
+--------------------------------+---------------------------------+------------------------------+
| Tela compatível                | TV de tubo CRT ou tela com RCA  | TV CRT + Monitor VGA PC      |
| Conector de vídeo              | 1x conector RCA fêmea           | 1x RCA fêmea + 1x VGA DE-15  |
| Complexidade de montagem       | Mínima (apenas 2 resistores)    | Média (3 resistores + VGA)   |
| Seleção de tela                | Automática                      | Por Chave ou Jumper (GP0)    |
| MicroSD (Leitura e Gravação)   | Sim                             | Sim                          |
| Portas USB (Teclado e Mouse)   | Sim                             | Sim                          |
| Custo total dos componentes    | Ultrabaixo (~4 a 6 USD)         | Muito econômico (~6 a 8 USD) |
+--------------------------------+---------------------------------+------------------------------+
```

---

## 📺 VERSÃO 1: Versão Simples / Econômica (Apenas Vídeo Composto)

[![Montagem Real PiMac 2040 - Versão 1 Vídeo Composto](assets/pimac2040_version1_composite.jpg)](assets/pimac2040_version1_composite.jpg)
*Montagem real da Versão 1: Conexão de Vídeo Composto RCA com divisor resistivo de 560 Ω e 270 Ω, adaptador MicroSD SPI e portas USB.*

### Como funciona?
Esta versão foi projetada para conectar o PiMac 2040 diretamente a qualquer TV antiga de tubo (CRT), televisor moderno com entrada amarela de vídeo (AV / RCA), ou monitor analógico de CFTV.

O microcontrolador RP2040 gera de forma nativa o sinal de vídeo analógico monocromático no padrão **NTSC 480i**. Por meio de dois resistores comuns conectados aos pinos GP8 e GP9, os pulsos de sincronismo e os pixels são somados para formar o sinal exato de 1.0V pico a pico com 75 Ω de impedância exigido por televisores.

### Esquema de Conexão de Vídeo Composto:
```text
   RP2040-Zero (Pinos)                           Conector RCA Fêmea Amarelo
  +--------------------+                         +---------------------------+
  |                    |      560 Ω (Verde-Azul-Marrom)                      |
  |  GP8 (Sync)        +-----[Resistor 1/4W]-------+                         |
  |                    |                           |                         |
  |                    |      270 Ω (Vermelho-Violeta-Marrom)                |
  |  GP9 (Vídeo)       +-----[Resistor 1/4W]-------+----> Pino Central (Sinal)|
  |                    |                                                     |
  |  GND (Massa)       +--------------------------------> Carcaça Externa/GND|
  +--------------------+                         +---------------------------+
```

### Lista de Componentes para Comprar (Nomes Técnicos Exatos):
1. **1x Placa Microcontroladora:** **Waveshare RP2040-Zero** (ou Tenstar Robot RP2040-Zero).
2. **1x Conector RCA Fêmea para Painel/Chassi:** Cor amarela (*RCA Female Jack Panel Mount Connector*).
3. **1x Resistor de 560 Ω (Ohms):** Filme de metal ou carbono, 1/4W ou 1/8W (Faixas: Verde - Azul - Marrom - Dourado).
4. **1x Resistor de 270 Ω (Ohms):** Filme de metal ou carbono, 1/4W ou 1/8W (Faixas: Vermelho - Violeta/Roxo - Marrom - Dourado).
5. **1x Adaptador Passivo MicroSD para SD** (o adaptador plástico preto que acompanha os cartões MicroSD) ou 1x Módulo MicroSD SPI de 3.3V.
6. **1x Adaptador OTG USB-C Macho para USB-A Fêmea** (para conectar teclado e mouse).

---

## 🖥️ VERSÃO 2: Versão Completa Dual (Vídeo Composto + Monitor VGA)

[![Montagem Real PiMac 2040 - Versão 2 Dual VGA e Composto](assets/pimac2040_version2_dual_vga_composite.jpg)](assets/pimac2040_version2_dual_vga_composite.jpg)
*Montagem real da Versão 2: Conexão Dual com porta VGA DE-15 (resistor de 100 Ω), conector RCA, chave SPDT de seleção e MicroSD SPI.*

### Como funciona o Motor Dual Inteligente?
O firmware detecta o nível lógico do pino **GP0** no momento da inicialização:
* **Ligando com GP0 desconectado (ao ar):** O sistema inicia em **Modo Vídeo Composto**, emitindo sinal NTSC de 15,734 kHz pelo conector RCA (ideal para TVs de tubo).
* **Ligando com GP0 conectado a GND (massa):** O sistema comuta para **Modo VGA Padrão**, emitindo 640x480 a 60 Hz (31,468 kHz) pelo conector VGA DB-15 (ideal para monitores de PC).

Ambos os conectores podem ser soldados simultaneamente na mesma placa. Use uma pequena chave seletora ou jumper para alternar entre o monitor da sua bancada e a TV da sala!

### Diagrama de Ligações Dual (VGA + Composto):
```text
   RP2040-Zero (Pinos)                           Conector VGA Fêmea (DE-15 / DB-15)
  +--------------------+                         +-----------------------------------+
  |  GP26 (Vídeo)      +-----[ 100 Ω (1/4W) ]----+----> Pinos 1, 2 e 3 (Vermelho, Verde e Azul unidos)
  |  GP27 (VSync)      +-------------------------> Pino 14 (Sincronismo Vertical)
  |  GP29 (HSync)      +-------------------------> Pino 13 (Sincronismo Horizontal)
  |  GND (Massa)       +-------------------------> Pinos 5, 6, 7, 8 e 10 (GND de Vídeo)
  +--------------------+                         +-----------------------------------+

   SELETOR DE TELA:
  +--------------------+                         +-----------------------------------+
  |  GP0               +----> [ Chave SPDT ] ----> GND (Massa Geral)
  |                    |      Aberto: Inicia em Vídeo Composto (TV CRT)
  |                    |      Fechado: Inicia em VGA (Monitor PC)
  +--------------------+                         +-----------------------------------+

   VÍDEO COMPOSTO RCA (Simultâneo):
  +--------------------+                         +-----------------------------------+
  |  GP8 (Sync)        +-----[ 560 Ω (1/4W) ]----+
  |  GP9 (Vídeo)       +-----[ 270 Ω (1/4W) ]----+----> Pino Central do Conector RCA
  |  GND (Massa)       +------------------------------> Malha Externa do Conector RCA
  +--------------------+                         +-----------------------------------+
```

### Componentes Adicionais para a Versão 2:
1. **Todos os itens da Versão 1** (RP2040-Zero, conector RCA, resistores de 560 Ω e 270 Ω, MicroSD e USB).
2. **1x Conector VGA Fêmea para Painel/Chassi:** D-Sub DE-15 fêmea de 15 pinos em 3 fileiras (*VGA DB15 Female 3-Row D-Sub Connector*).
3. **1x Resistor de 100 Ω (Ohms):** Filme de metal ou carbono, 1/4W ou 1/8W (Faixas: Marrom - Preto - Marrom - Dourado).
4. **1x Mini Chave Deslizante SPDT** ou Jumper de 2 pinos (*SPDT Mini Slide Switch 3 Pin* ou *Jumper 2.54mm*).

---

## 💾 4. Ligação do Cartão MicroSD (SPI)

Você pode utilizar um módulo MicroSD de 3.3V comercial ou soldar 6 fios finos diretamente nos contatos traseiros de um **adaptador MicroSD para SD**:

```text
       RP2040-Zero                               Adaptador SD Passivo (Pistas Traseiras)
   +-----------------------+                    +------------------------------------+
   |   GP5 (CS)            +------------------->| Pista 1 (CD/DAT3)                  |
   |   GP3 (MOSI)          +------------------->| Pista 2 (CMD / MOSI)               |
   |   GND                 +------------------->| Pista 3 (VSS1 / Massa)             |
   |   3V3 (3.3 Volts)     +------------------->| Pista 4 (VDD)  ⚠️ APENAS 3.3 VOLTS! |
   |   GP2 (SCK)           +------------------->| Pista 5 (CLK / Clock)              |
   |   GND                 +------------------->| Pista 6 (VSS2 / Massa)             |
   |   GP4 (MISO)          +------------------->| Pista 7 (DAT0 / MISO)              |
   +-----------------------+                    +------------------------------------+
```

> [!CAUTION]
> Ligue a alimentação do cartão MicroSD **estritamente no pino 3V3 (3.3V)** da placa RP2040. **NUNCA** ligue no pino de 5V, caso contrário o cartão de memória será danificado permanentemente!

---

## 🖱️ 5. Ligação das Portas USB para Teclado e Mouse

O PiMac 2040 conta com controlador **USB Host** gerenciado por hardware (PIO):

```text
       RP2040-Zero                               Conectores USB-A Fêmea
   +-----------------------+                    +-------------------------------------+
   |   5V (VBUS)           +------------------->| Pino 1 (+5V Alimentação USB) [Ambos]|
   |                       |                    +-------------------------------------+
   |                       |                    | PORTA 1 (TECLADO USB):              |
   |   GP10                +----[ 27 Ω ]--------+ Pino 3: D+ (Dados Positivos)        |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP11                +----[ 27 Ω ]--------+ Pino 2: D- (Dados Negativos)        |
   |                       |          |         +-------------------------------------+
   |                       |       [ 15 kΩ ]    | PORTA 2 (MOUSE USB):                |
   |   GP12                +----[ 27 Ω ]--------+ Pino 3: D+ (Dados Positivos)        |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP13                +----[ 27 Ω ]--------+ Pino 2: D- (Dados Negativos)        |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GND (Massa)         +----------+---------+ Pino 4: GND (Massa USB) [Ambos]     |
   +-----------------------+                    +-------------------------------------+
```

* **Compatibilidade:** Funciona com a maioria dos teclados e mouses USB com fio convencionais, bem como kits sem fio com receptor dongle USB de 2.4 GHz.
* **Opção USB-C OTG:** Você também pode conectar o teclado diretamente à porta USB-C da placa com um adaptador OTG simples.

---

## 🚦 6. Diagnóstico com o LED RGB Integrado (GP16)

A placa RP2040-Zero possui um LED RGB integrado (WS2812). O firmware utiliza-o como painel de diagnóstico em tempo real:

| Cor do LED | Comportamento | Significado |
| :--- | :--- | :--- |
| 🟧 **Laranja suave** | Pulsação lenta | Inicializando o sistema e carregando a ROM do Mac Plus. |
| 🟩 **Verde contínuo** | Respiração suave | **Sistema pronto!** O Finder está ativo aguardando comandos. |
| 🟨 **Âmbar brilhante** | Flashes rápidos | Lendo blocos de dados do cartão MicroSD. |
| 🟪 **Magenta brilhante**| Flashes rápidos | **Gravando dados no MicroSD:** Salvando arquivos, partidas ou desenhos. |
| 🔴 **Vermelho contínuo**| Pisca de alarme | Erro de MicroSD: revise as ligações SPI ou certifique-se de que o cartão está em FAT32 com o arquivo `umac0.img`. |

---

## 🔋 7. Como Alimentar o Circuito

1. **Por cabo USB-C:** O método mais simples. Ligue a porta USB-C da RP2040-Zero a um carregador comum de celular (5V / 1A ou 2A).
2. **Por fonte fixa de 5V DC:** Conecte o polo positivo de 5V ao pino marcado como **`5V` (VBUS)** e o negativo ao pino **`GND`**.
3. **Por bateria recarregável (Portátil):** Utilize uma bateria de lítio 18650 (3.7V) acoplada a um módulo carregador **TP4056 com elevador Booster 5V integrado**, alimentando os pinos `5V` e `GND` da placa.

---

## 📜 Licença Aberta e Créditos

Este projeto é software e hardware de código aberto, distribuído sob os termos da **Licença MIT**. Você é livre para usá-lo, estudá-lo, aprimorá-lo e compartilhá-lo com a comunidade.

Desenvolvido, otimizado e documentado com dedicação por **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl)). Agradecemos manter a citação e o link original em projetos derivados.
