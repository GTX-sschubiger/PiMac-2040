# Coleção de Imagens de Disco para PiMac 2040 (Macintosh 208K)
### Curadoria e Desenvolvimento por **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="README.md">🇪🇸 Español</a> |
  <a href="README_EN.md">🇬🇧 English</a> |
  <a href="README_PT.md"><strong>🇵🇹 Português</strong></a> |
  <a href="README_DE.md">🇩🇪 Deutsch</a> |
  <a href="README_ZH.md">🇨🇳 中文</a> |
  <a href="README_FR.md">🇫🇷 Français</a>
</p>


Este diretório contém uma coleção completa de imagens de disco prontas para inicialização e gravação de dados diretamente no cartão MicroSD na placa **RP2040-Zero**.

---

## 💽 Catálogo de Imagens de Disco Disponíveis

| Nome do Arquivo | Tamanho | Sistema Operacional | Tipo | Principais Softwares e Destaques |
| :--- | :---: | :---: | :---: | :--- |
| **`umac0_oficina_almacenamiento_20mb.img`** | **20 MB** | System 3.2 / Finder 5.3 | HFS Escritório & Armazenamento | **Produtividade e Trabalho Real:**<br>• **Microsoft Office:** Word 4.0a, Excel 2.2a, Works 3.0 (suíte integrada com processador de texto, planilhas e banco de dados).<br>• **Editoração e Desenho:** Aldus PageMaker 2.0a, MacPaint 2.0, MacDraw 1.9.<br>• **Editores de Texto:** TeachText, BBEdit Lite 3.5.1.<br>• **Utilitários:** Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm 1.0.1.<br>• **📁 Meus Documentos:** Pasta dedicada com **mais de 10 MB de espaço livre permanente** para salvar seus arquivos no MicroSD. |
| **`umac0_aventura_juegos_15mb.img`** | **15 MB** | System 3.2 / Finder 5.3 | HFS Aventura & Jogos | **Aventura e Estratégia de Alto Nível:**<br>• **Prince of Persia:** A obra-prima lendária de Jordan Mechner com duelos de espada (versão P&B otimizada).<br>• **SimCity 1.11:** O clássico simulador de cidades de Will Wright com cenários e efeitos sonoros.<br>• **Tetris:** Edição oficial da Spectrum HoloByte com trilhas sonoras clássicas.<br>• **Clássicos Silicon Beach:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter v1.x/2.0.<br>• **Jogos de Mesa e Arcade:** Shufflepuck Café, Risk (Guerra Mundial), Cannon Fodder, Lode Runner, Billiard Parlour.<br>• **📁 Meus Jogos Salvos:** Mais de 8 MB livres para armazenar cidades no SimCity e progresso de jogos. |
| **`umac0_master_10mb.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS Tudo-em-Um | **Equilíbrio Perfeito:** Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA, MacPaint, MacDraw, TeachText, Disk Copy, Utilitários. |
| **`umac0.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS/MFS Clássico | **Pacote Clássico Original:** MacPaint 1.3, MacWrite 4.5, MacDraw, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma. |
| **`umac0_games_pack.img`** | 4 MB | System 3.2 / Finder 5.3 | HFS Pacote Arcade | **Especial Jogos:** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA. |
| **`umac0_productivity.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Produtividade | **Ferramentas Essenciais:** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock. |
| **`umac0_dark_castle.img`** | 800 KB | Sistema Autônomo | HFS Jogo Individual | **Dark Castle v1.2:** Versão inicializável autônoma do clássico jogo de ação. |
| **`umac0_beyond_dark_castle.img`** | 800 KB | Sistema Autônomo | HFS Jogo Individual | **Beyond Dark Castle:** Sequência aclamada com jetpack, bombas e salas secretas. |
| **`umac0_stunt_copter.img`** | 800 KB | Sistema Autônomo | HFS Jogo Individual | **Stunt Copter:** Físicas clássicas de precisão por Duane Blehm (v1.0 e v2.0). |
| **`umac0_system11_1984.img`** | 400 KB | System 1.1 / Finder 1.1g | MFS Histórico 1984 | **Macintosh 128K Histórico:** O sistema original demonstrado por Steve Jobs em 24 de janeiro de 1984. |
| **`umac0_system32_utilities.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS Ferramentas | **Utilitários Apple Oficiais:** Font/DA Mover, fontes vintage (Chicago, Geneva, Monaco, San Francisco) e ferramentas de disco. |

---

## 🚀 Como Usar e Alternar Discos no Cartão MicroSD

O firmware **PiMac 2040** procura na raiz do cartão MicroSD pelo arquivo com o nome **`umac0.img`**.

### Opções de Uso:

### Opção 1: Disco Tudo-em-Um (Recomendado)
Copie `umac0_oficina_almacenamiento_20mb.img` ou `umac0_master_10mb.img` para o seu MicroSD e renomeie-o para **`umac0.img`**:
* Você terá muito espaço livre e praticamente todos os aplicativos de escritório, desenho e jogos organizados em pastas com suporte a leitura e escrita.

### Opção 2: Manter Vários Discos e Selecionar o Ativo
Você pode armazenar todas as imagens no cartão MicroSD:
* `umac0.img` (o disco ativo que inicializará por padrão)
* `oficina.img`
* `jogos.img`
* `darkcastle.img`
* `system1984.img`

Quando desejar alternar de disco, conecte o cartão ao computador ou celular e simplesmente renomeie a imagem desejada para **`umac0.img`**.

---

## 💾 Persistência de Dados (Leitura e Gravação)
Diferente das memórias ROM fixas em microcontroladores, executar esses discos a partir do MicroSD no RP2040-Zero garante persistência real:
* **Grave documentos** no MacWrite ou desenhos no MacPaint.
* **Salve recordes e progresso de fases** no Prince of Persia, SimCity, Dark Castle, Stunt Copter e Shufflepuck Café.
* **Ajuste Desk Accessories** e preferências no Painel de Controle; as alterações permanecem salvas após reiniciar!
