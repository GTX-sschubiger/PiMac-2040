# Collection d'Images Disques pour PiMac 2040 (Macintosh 208K)
### Conçu et Développé par **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl))

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="README.md">🇪🇸 Español</a> |
  <a href="README_EN.md">🇬🇧 English</a> |
  <a href="README_PT.md">🇵🇹 Português</a> |
  <a href="README_DE.md">🇩🇪 Deutsch</a> |
  <a href="README_ZH.md">🇨🇳 中文</a> |
  <a href="README_FR.md"><strong>🇫🇷 Français</strong></a>
</p>


Ce répertoire contient une collection complète d'images disques prêtes à démarrer avec prise en charge de la lecture et de l'écriture directe sur carte MicroSD avec la carte **RP2040-Zero**.

---

## 💽 Catalogue des Images Disques Disponibles

| Nom de Fichier | Taille | Système d'Exploitation | Format | Logiciels Inclus & Points Forts |
| :--- | :---: | :---: | :---: | :--- |
| **`umac0_oficina_almacenamiento_20mb.img`** | **20 Mo** | System 3.2 / Finder 5.3 | HFS Bureautique & Stockage | **Productivité Réelle & Travail :**<br>• **Suite Microsoft Office :** Word 4.0a, Excel 2.2a, Works 3.0 (suite intégrée traitement de texte, tableur et base de données).<br>• **Édition & Graphisme :** Aldus PageMaker 2.0a, MacPaint 2.0, MacDraw 1.9.<br>• **Éditeurs de Texte :** TeachText, BBEdit Lite 3.5.1.<br>• **Utilitaires Système :** Disk Copy 4.2, ResEdit 2.1.3, Disinfectant 3.7.1, StuffIt Expander, Compact Pro, ZTerm 1.0.1.<br>• **📁 Mes Documents :** Dossier dédié avec **plus de 10 Mo d'espace libre permanent** pour vos fichiers sur la MicroSD. |
| **`umac0_aventura_juegos_15mb.img`** | **15 Mo** | System 3.2 / Finder 5.3 | HFS Aventure & Jeux | **Aventure & Stratégie Rétro :**<br>• **Prince of Persia :** Le chef-d'œuvre légendaire d'action et de plates-formes de Jordan Mechner avec duels à l'épée (version N&B optimisée).<br>• **SimCity 1.11 :** Le simulateur de ville culte de Will Wright avec scénarios complets et effets sonores.<br>• **Tetris :** Édition officielle de Spectrum HoloByte sonorisée.<br>• **Classiques Silicon Beach :** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter v1.x/2.0.<br>• **Jeux d'Arcade et de Société :** Shufflepuck Café, Risk (Stratégie Mondiale), Cannon Fodder, Lode Runner, Billiard Parlour.<br>• **📁 Mes Sauvegardes :** Plus de 8 Mo libres pour sauvegarder villes SimCity et parties en cours. |
| **`umac0_master_10mb.img`** | 10 Mo | System 3.2 / Finder 5.3 | HFS Tout-en-Un | **Équilibre Optimal :** Dark Castle, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA, MacPaint, MacDraw, TeachText, Disk Copy, Utilitaires. |
| **`umac0.img`** | 10 Mo | System 3.2 / Finder 5.3 | HFS/MFS Classique | **Pack Classique Original :** MacPaint 1.3, MacWrite 4.5, MacDraw, Lode Runner, Aliens, Billiard Parlour, Mouse Eaters, DaliClock, Planetfall, MacLanding, Enigma. |
| **`umac0_games_pack.img`** | 4 Mo | System 3.2 / Finder 5.3 | HFS Pack Arcade | **Spécial Jeux d'Arcade :** Dark Castle v1.2, Beyond Dark Castle, Stunt Copter, Shufflepuck Café, Risk, Cannon Fodder, Tetris DA. |
| **`umac0_productivity.img`** | 800 Ko | System 3.2 / Finder 5.3 | HFS Bureautique | **Outils Essentiels :** MacPaint, MacDraw, TeachText, Disk Copy, Draw Tour, Woodblock. |
| **`umac0_dark_castle.img`** | 800 Ko | Système Autonome | HFS Jeu Dédié | **Dark Castle v1.2 :** Version amorçable directe du jeu de plates-formes mythique. |
| **`umac0_beyond_dark_castle.img`** | 800 Ko | Système Autonome | HFS Jeu Dédié | **Beyond Dark Castle :** Suite incontournable avec jetpack, bombes et passages secrets. |
| **`umac0_stunt_copter.img`** | 800 Ko | Système Autonome | HFS Jeu Dédié | **Stunt Copter :** Jeu d'adresse et de physique de Duane Blehm (v1.0 et v2.0). |
| **`umac0_system11_1984.img`** | 400 Ko | System 1.1 / Finder 1.1g | MFS Historique 1984 | **Macintosh 128K Historique :** Le système original présenté par Steve Jobs le 24 janvier 1984. |
| **`umac0_system32_utilities.img`** | 800 Ko | System 3.2 / Finder 5.3 | HFS Outils Système | **Utilitaires Officiels Apple :** Font/DA Mover, polices vintage (Chicago, Geneva, Monaco, San Francisco) et outils disques. |

---

## 🚀 Comment Utiliser et Changer de Disque sur la Carte MicroSD ?

Le firmware **PiMac 2040** recherche à la racine de la carte MicroSD le fichier portant le nom exact **`umac0.img`**.

### Méthodes d'Utilisation :

### Option 1 : Le Disque Tout-en-Un (Recommandé)
Copiez `umac0_oficina_almacenamiento_20mb.img` ou `umac0_master_10mb.img` sur votre carte MicroSD et renommez-le en **`umac0.img`** :
* Vous disposerez de tout l'espace nécessaire avec applications bureautiques, dessin et jeux classés dans des dossiers, avec support de lecture/écriture.

### Option 2 : Conserver Plusieurs Disques et Choisir le Disque Actif
Vous pouvez stocker toutes les images disques sur votre carte MicroSD :
* `umac0.img` (le disque actif qui démarrera par défaut)
* `office.img`
* `jeux.img`
* `darkcastle.img`
* `system1984.img`

Lorsque vous souhaitez changer de système, insérez la carte MicroSD dans votre PC ou téléphone et renommez simplement l'image de votre choix en **`umac0.img`**.

---

## 💾 Persistance des Données (Lecture / Écriture Réelle)
Contrairement aux mémoires mortes figées des microcontrôleurs traditionnels, l'exécution depuis la carte MicroSD sur le RP2040-Zero offre une vraie persistance :
* **Enregistrez vos documents** sous MacWrite ou vos illustrations sous MacPaint.
* **Sauvegardez vos scores et progressions** dans Prince of Persia, SimCity, Dark Castle, Stunt Copter et Shufflepuck Café.
* **Personnalisez vos Desk Accessories** et le Tableau de Bord ; vos réglages sont conservés après chaque redémarrage !
