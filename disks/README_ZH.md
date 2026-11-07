# PiMac 2040 (Macintosh 208K) 磁盘镜像全集
### 由 **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl)) 整理与开发

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="README.md">🇪🇸 Español</a> |
  <a href="README_EN.md">🇬🇧 English</a> |
  <a href="README_PT.md">🇵🇹 Português</a> |
  <a href="README_DE.md">🇩🇪 Deutsch</a> |
  <a href="README_ZH.md"><strong>🇨🇳 中文</strong></a> |
  <a href="README_FR.md">🇫🇷 Français</a>
</p>


本目录提供了一套开箱即用的完整磁盘镜像库，支持直接在 **RP2040-Zero** 开发板所连接的 MicroSD 卡上引导启动并持久化读写数据。

---

## 💽 可用磁盘镜像目录清单

| 镜像文件名 | 容量 | 操作系统版本 | 分区格式 | 核心应用与特色内容 |
| :--- | :---: | :---: | :---: | :--- |
| **`umac0_oficina_almacenamiento_20mb.img`** | **20 MB** | System 3.2 / Finder 5.3 | HFS 办公与大容量存储 | **办公生产力实战套装：**<br>• **Microsoft Office 办公三件套：** Word 4.0a, Excel 2.2a, Works 3.0（集成文字处理、电子表格与数据库）。<br>• **排版印刷与美术设计：** Aldus PageMaker 2.0a, MacPaint 2.0, MacDraw 1.9。<br>• **文本编辑器：** TeachText, BBEdit Lite 3.5.1。<br>• **系统运维工具：** Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm 1.0.1。<br>• **📁 我的文档：** 专属用户目录，在 MicroSD 卡上提供**超过 10 MB 永久剩余可用空间**。 |
| **`umac0_aventura_juegos_15mb.img`** | **15 MB** | System 3.2 / Finder 5.3 | HFS 冒险与游戏大合辑 | **顶级复古冒险与策略名作：**<br>• **波斯王子 (Prince of Persia)：** Jordan Mechner 经典刀剑动作冒险跳跃神作（黑白优化版）。<br>• **模拟城市 1.11 (SimCity)：** Will Wright 经典城市营造模拟游戏，内含完整关卡与音效。<br>• **俄罗斯方块 (Tetris)：** Spectrum HoloByte 官方声效正版。<br>• **Silicon Beach 传奇动作：** 黑暗城堡 (Dark Castle v1.2), 城堡飞跃 (Beyond Dark Castle), 特技直升机 (Stunt Copter v1.x/2.0)。<br>• **街机与桌面游戏：** 飞碟咖啡馆 (Shufflepuck Café), 战国风云 (Risk 策略), 炮灰 (Cannon Fodder), 淘金者 (Lode Runner), 台球 (Billiard Parlour)。<br>• **📁 我的游戏存档：** 预留超过 8 MB 剩余空间，用于存储波斯王子进度与模拟城市地图。 |
| **`umac0_master_10mb.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS 全能合辑 | **黄金均衡盘：** Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA, MacPaint, MacDraw, TeachText, Disk Copy, 系统工具。 |
| **`umac0.img`** | 10 MB | System 3.2 / Finder 5.3 | HFS/MFS 经典盘 | **初代经典组合包：** MacPaint 1.3, MacWrite 4.5, MacDraw, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma。 |
| **`umac0_games_pack.img`** | 4 MB | System 3.2 / Finder 5.3 | HFS 街机特辑 | **纯粹游戏合辑：** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA。 |
| **`umac0_productivity.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS 办公工具 | **轻量生产力工具：** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock。 |
| **`umac0_dark_castle.img`** | 800 KB | 独立启动系统 | HFS 单盘游戏 | **黑暗城堡 v1.2 (Dark Castle)：** 开机即玩的平台跳跃独立盘。 |
| **`umac0_beyond_dark_castle.img`** | 800 KB | 独立启动系统 | HFS 单盘游戏 | **城堡飞跃 (Beyond Dark Castle)：** 带喷气背包、炸弹的超好玩续作。 |
| **`umac0_stunt_copter.img`** | 800 KB | 独立启动系统 | HFS 单盘游戏 | **特技直升机 (Stunt Copter)：** Duane Blehm 经典物理技巧力作（v1.0 与 v2.0）。 |
| **`umac0_system11_1984.img`** | 400 KB | System 1.1 / Finder 1.1g | MFS 1984 历史原版 | **Macintosh 128K 历史盘：** 1984 年 1 月 24 日史蒂夫·乔布斯在发布会上演示的原装系统。 |
| **`umac0_system32_utilities.img`** | 800 KB | System 3.2 / Finder 5.3 | HFS 系统工具 | **Apple 官方磁盘工具：** Font/DA Mover 字体工具、历史字体（Chicago, Geneva, Monaco, San Francisco）与磁盘诊断。 |

---

## 🚀 如何在 MicroSD 卡中使用与切换磁盘镜像？

**PiMac 2040** 固件在开机时会自动检测 MicroSD 卡根目录下名为 **`umac0.img`** 的文件作为启动主盘。

### 使用方案：

### 方案 1：使用全能十全大补盘（推荐）
将 `umac0_oficina_almacenamiento_20mb.img` 或 `umac0_master_10mb.img` 拷贝到 MicroSD 卡并重命名为 **`umac0.img`**：
* 您将拥有充裕的存储空间，所有办公软件、设计绘图工具与经典游戏已分门别类整理完毕，且支持直接存盘。

### 方案 2：存放多张盘，按需切换引导
您可以将所有镜像文件同时存放在 MicroSD 卡中：
* `umac0.img`（当前开机默认启动的主盘）
* `office.img`
* `games.img`
* `darkcastle.img`
* `system1984.img`

当您想切换到另一个系统体验时，只需将存储卡插入电脑或手机，将想玩的那张镜像改名为 **`umac0.img`** 即可！

---

## 💾 数据持久化特性 (完整支持读写操作)
与单片机中写死的只读 ROM 不同，在 RP2040-Zero 上通过 MicroSD 运行这些镜像支持真正的可读写持久化：
* **保存工作文档**：在 MacWrite 中撰写文章或在 MacPaint 中画画可随时保存。
* **保存游戏通关进度与排行榜**：在波斯王子、模拟城市、黑暗城堡与特技直升机中可随存随取。
* **系统配置持久化**：自定义桌面小工具（Desk Accessories）与控制面板设置，重启后配置依旧生效！
