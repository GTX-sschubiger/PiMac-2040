# PiMac 2040 (Macintosh 208K) – Guide Officiel d'Installation et Matériel
### Projet Logiciel et Matériel Open-Source par [SCHUBIGER.CL](https://schubiger.cl)
### Licence MIT – Libre d'Utilisation, de Modification et de Partage

<p align="center">
  <strong>🌐 Idiomas / Languages / Sprachen / 语言 / Langues:</strong><br>
  <a href="RELEASE_README.md">🇪🇸 Español</a> |
  <a href="RELEASE_README_EN.md">🇬🇧 English</a> |
  <a href="RELEASE_README_PT.md">🇵🇹 Português</a> |
  <a href="RELEASE_README_DE.md">🇩🇪 Deutsch</a> |
  <a href="RELEASE_README_ZH.md">🇨🇳 中文</a> |
  <a href="RELEASE_README_FR.md"><strong>🇫🇷 Français</strong></a>
</p>


Bienvenue sur **PiMac 2040** ! Ce guide est rédigé de façon simple, claire et accessible à tous — même sans expérience préalable des microcontrôleurs — afin que vous puissiez flasher le système sur une carte **RP2040**, assembler votre circuit en quelques minutes et revivre l'expérience complète de l'emblématique Apple Macintosh de 1984 avec souris, clavier, stockage MicroSD et sortie vidéo pour téléviseurs cathodiques ou moniteurs d'ordinateur.

---

## ⚡ 1. Installation Rapide sur RP2040 (En 3 Étapes)

Aucune installation de chaîne de compilation complexe n'est requise. Le firmware est déjà compilé et prêt à l'emploi dans le fichier **`release/PiMac2040_DualVideo_RP2040Zero.uf2`** :

```text
  [ Fichier .UF2 ]    ------------------------->  [ Lecteur RPI-RP2 ]  ---> Installé !
  (Firmware PiMac 2040)        Glisser-déposer             (RP2040 en mode Boot)      (Redémarre en 2 sec)
```

1. **Connexion en mode Boot :** Munissez-vous de votre carte **Waveshare / Tenstar Robot RP2040-Zero** (ou Raspberry Pi Pico). Maintenez enfoncé le bouton blanc **BOOT** (ou BOOTSEL) et, sans le relâcher, branchez le câble USB-C à votre ordinateur. Relâchez ensuite le bouton.
2. **Apparition du lecteur :** Un nouveau lecteur amovible nommé **`RPI-RP2`** apparaît automatiquement sur votre ordinateur (exactement comme une clé USB).
3. **Copier le firmware :** Glissez-déposez dans le lecteur `RPI-RP2` le fichier :
   👉 **`release/PiMac2040_DualVideo_RP2040Zero.uf2`**
4. **C'est prêt !** En deux secondes, la LED clignote, le lecteur se ferme automatiquement et PiMac 2040 est installé de façon permanente dans la mémoire Flash.

---

## 💾 2. Préparation de la Carte MicroSD avec Disques et Applications

1. Prenez une carte MicroSD quelconque (de 256 Mo à 32 Go).
2. Connectez-la à votre ordinateur et formatez-la en **FAT32** (Formatage rapide).
3. Ouvrez le dossier **`disks/`** et choisissez l'image de disque que vous souhaitez démarrer :
   * **`umac0_oficina_almacenamiento_20mb.img` :** Suite bureautique complète (Word 4.0, Excel 2.2, Works 3.0, PageMaker 2.0, MacPaint, MacDraw) avec plus de 10 Mo d'espace libre dans *Mes Documents* pour enregistrer vos fichiers durablement.
   * **`umac0_aventura_juegos_15mb.img` :** Pack aventure et stratégie (Prince of Persia, SimCity 1.11, Tetris officiel, Dark Castle, Stunt Copter, Shufflepuck Café) avec plus de 8 Mo libres pour vos sauvegardes.
   * **`umac0_master_10mb.img` :** Image disque tout-en-un équilibrée avec jeux, dessin et utilitaires système.
4. **Copiez l'image choisie à la racine de la carte MicroSD** et renommez-la exactement en :
   👉 **`umac0.img`**
5. Insérez la carte MicroSD dans le lecteur de votre PiMac 2040.

---

## 🛠️ 3. Les 2 Versions Matérielles : Laquelle Choisir ?

Le firmware de PiMac 2040 intègre un **moteur vidéo double intelligent** compatible avec les téléviseurs analogiques et les moniteurs d'ordinateur :

```text
+-------------------------------------------------------------------------------------------------+
|                                    COMPARATIF DES VERSIONS                                      |
+-------------------------------------------------------------------------------------------------+
| CARACTÉRISTIQUE                | VERSION 1 : VIDÉO COMPOSITE SEULE| VERSION 2 : DOUBLE VGA + COMP.|
+--------------------------------+----------------------------------+------------------------------+
| Écrans compatibles             | TV cathodique CRT ou écran RCA   | TV CRT + Moniteur PC VGA     |
| Prises vidéo                   | 1x Prise RCA femelle             | 1x RCA femelle + 1x VGA DE-15|
| Complexité d'assemblage        | Minimale (seulement 2 résistances| Moyenne (3 résistances + VGA)|
| Choix du mode d'affichage      | Automatique                      | Par Interrupteur/Jumper (GP0)|
| MicroSD (Lecture & Écriture)   | Oui                              | Oui                          |
| Ports USB (Clavier & Souris)   | Oui                              | Oui                          |
| Coût total des composants      | Minime (~4 à 6 USD)              | Très économique (~6 à 8 USD) |
+--------------------------------+----------------------------------+------------------------------+
```

---

## 📺 VERSION 1 : Montage Simple / Économique (Vidéo Composite Seule)

[![Montage Réel PiMac 2040 Version 1 Vidéo Composite](assets/pimac2040_version1_composite.jpg)](assets/pimac2040_version1_composite.jpg)
*Montage réel de la Version 1 : Prise RCA composite avec pont diviseur de 560 Ω et 270 Ω, hack MicroSD SPI et ports USB.*

### Comment cela fonctionne-t-il ?
Cette version permet de raccorder directement le PiMac 2040 à un téléviseur cathodique vintage (CRT), un écran plat avec prise jaune composite (AV / RCA), ou un moniteur de contrôle vidéo.

Le microcontrôleur RP2040 génère de manière matérielle un signal vidéo composite monochrome **NTSC 480i**. Deux résistances connectées aux broches GP8 et GP9 mélangent de manière numérique la synchronisation et la vidéo active pour délivrer le signal standard de 1,0 V crête-à-crête sous 75 Ω d'impédance.

### Schéma de Câblage Vidéo Composite :
```text
   RP2040-Zero (Broches)                         Prise Châssis RCA Femelle Jaune
  +--------------------+                         +------------------------------+
  |                    |      560 Ω (Vert-Bleu-Marron)                          |
  |  GP8 (Sync)        +-----[Résistance 1/4W]-----+                            |
  |                    |                           |                            |
  |                    |      270 Ω (Rouge-Violet-Marron)                       |
  |  GP9 (Vidéo)       +-----[Résistance 1/4W]-----+----> Broche Centrale (+)   |
  |                    |                                                        |
  |  GND (Masse)       +--------------------------------> Blindage Extérieur (-) |
  +--------------------+                         +------------------------------+
```

### Liste des Composants (Nomenclature Technique) :
1. **1x Carte microcontrôleur :** **Waveshare RP2040-Zero** (ou Tenstar Robot RP2040-Zero).
2. **1x Prise RCA femelle à monter sur châssis :** Isolateur jaune (*RCA Female Jack Panel Mount Connector*).
3. **1x Résistance de 560 Ω :** Couche métallique ou carbone, 1/4W ou 1/8W (Anneaux : Vert - Bleu - Marron - Or).
4. **1x Résistance de 270 Ω :** Couche métallique ou carbone, 1/4W ou 1/8W (Anneaux : Rouge - Violet - Marron - Or).
5. **1x Adaptateur passif MicroSD vers SD** (adaptateur plastique standard fourni avec les cartes MicroSD) ou 1x module SPI MicroSD 3.3V.
6. **1x Adaptateur OTG USB-C mâle vers USB-A femelle** (pour brancher clavier et souris).

---

## 🖥️ VERSION 2 : Montage Complet Dual (Vidéo Composite + Moniteur VGA)

[![Montage Réel PiMac 2040 Version 2 Dual VGA et Composite](assets/pimac2040_version2_dual_vga_composite.jpg)](assets/pimac2040_version2_dual_vga_composite.jpg)
*Montage réel de la Version 2 : Câblage dual complet avec prise VGA DE-15 (résistance 100 Ω), prise RCA, sélecteur SPDT et MicroSD SPI.*

### Fonctionnement du Moteur Vidéo Double :
Au démarrage, le firmware analyse l'état logique de **GP0** :
* **Démarrage avec GP0 en l'air (non relié) :** Le RP2040 s'initialise en **Mode Vidéo Composite** à 15,734 kHz sur la prise RCA (idéal pour les téléviseurs CRT).
* **Démarrage avec GP0 relié à la masse (GND) :** Le RP2040 bascule en **Mode VGA Standard** en 640x480 à 60 Hz (31,468 kHz) sur la prise VGA DB-15 (idéal pour moniteurs PC).

Les deux prises peuvent être soudées sur la même carte en permanence. Un simple petit interrupteur permet de passer de votre bureau à votre téléviseur de salon !

### Schéma de Câblage Dual (VGA + Composite) :
```text
   RP2040-Zero (Broches)                         Connecteur VGA Femelle (DE-15 / DB-15)
  +--------------------+                         +-----------------------------------+
  |  GP26 (Vidéo)      +-----[ 100 Ω (1/4W) ]----+----> Broches 1, 2 et 3 (Rouge, Vert, Bleu reliés)
  |  GP27 (VSync)      +-------------------------> Broche 14 (Synchronisation Verticale)
  |  GP29 (HSync)      +-------------------------> Broche 13 (Synchronisation Horizontale)
  |  GND (Masse)       +-------------------------> Broches 5, 6, 7, 8 et 10 (Masse Vidéo)
  +--------------------+                         +-----------------------------------+

   SÉLECTEUR DE SORTIE VIDÉO :
  +--------------------+                         +-----------------------------------+
  |  GP0               +----> [ Interrupteur ] ---> GND (Masse)
  |                    |      Ouvert : Démarre en Vidéo Composite (TV CRT)
  |                    |      Fermé : Démarre en VGA (Moniteur PC)
  +--------------------+                         +-----------------------------------+

   VIDÉO COMPOSITE RCA (Simultané) :
  +--------------------+                         +-----------------------------------+
  |  GP8 (Sync)        +-----[ 560 Ω (1/4W) ]----+
  |  GP9 (Vidéo)       +-----[ 270 Ω (1/4W) ]----+----> Broche Centrale Prise RCA
  |  GND (Masse)       +------------------------------> Blindage Extérieur Prise RCA
  +--------------------+                         +-----------------------------------+
```

### Composants Additionnels pour la Version 2 :
1. **Tous les éléments de la Version 1** (RP2040-Zero, prise RCA, résistances de 560 Ω et 270 Ω, MicroSD et USB).
2. **1x Connecteur VGA femelle DE-15 / DB-15 à monter :** 15 broches sur 3 rangées (*VGA DB15 Female 3-Row D-Sub Connector*).
3. **1x Résistance de 100 Ω :** Couche métallique ou carbone, 1/4W ou 1/8W (Anneaux : Marron - Noir - Marron - Or).
4. **1x Mini interrupteur à glissière SPDT** ou cavalier à 2 broches (*SPDT Mini Slide Switch 3 Pin*).

---

## 💾 4. Raccordement de la Carte MicroSD (SPI)

Vous pouvez utiliser un module MicroSD 3.3V du commerce ou souder directement 6 fils fins sur les contacts dorés d'un **adaptateur passif MicroSD vers SD** :

```text
       RP2040-Zero                               Adaptateur SD Passif (Contacts Arrière)
   +-----------------------+                    +------------------------------------+
   |   GP5 (CS)            +------------------->| Piste 1 (CD/DAT3)                  |
   |   GP3 (MOSI)          +------------------->| Piste 2 (CMD / MOSI)               |
   |   GND                 +------------------->| Piste 3 (VSS1 / Masse)             |
   |   3V3 (3.3 Volts)     +------------------->| Piste 4 (VDD)  ⚠️ STRICTEMENT 3.3V !|
   |   GP2 (SCK)           +------------------->| Pista 5 (CLK / Horloge)            |
   |   GND                 +------------------->| Piste 6 (VSS2 / Masse)             |
   |   GP4 (MISO)          +------------------->| Piste 7 (DAT0 / MISO)              |
   +-----------------------+                    +------------------------------------+
```

> [!CAUTION]
> Alimentez la carte MicroSD **uniquement à partir de la broche 3V3 (3.3V)** de la carte RP2040. Ne la raccordez **JAMAIS** à la broche 5V sous peine de destruction immédiate de votre carte mémoire !

---

## 🖱️ 5. Raccordement des Ports USB pour Clavier et Souris

Le PiMac 2040 inclut un contrôleur **USB Host** piloté par le bloc matériel PIO :

```text
       RP2040-Zero                               Prises USB-A Femelles
   +-----------------------+                    +-------------------------------------+
   |   5V (VBUS)           +------------------->| Broche 1 (+5V Alimentation) [Deux]  |
   |                       |                    +-------------------------------------+
   |                       |                    | PORT 1 (CLAVIER USB) :              |
   |   GP10                +----[ 27 Ω ]--------+ Broche 3 : D+ (Données +)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP11                +----[ 27 Ω ]--------+ Broche 2 : D- (Données -)           |
   |                       |          |         +-------------------------------------+
   |                       |       [ 15 kΩ ]    | PORT 2 (SOURIS USB) :               |
   |   GP12                +----[ 27 Ω ]--------+ Broche 3 : D+ (Données +)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GP13                +----[ 27 Ω ]--------+ Broche 2 : D- (Données -)           |
   |                       |          |         |                                     |
   |                       |       [ 15 kΩ ]    |                                     |
   |                       |          |         |                                     |
   |   GND (Masse)         +----------+---------+ Broche 4 : GND (Masse USB) [Deux]   |
   +-----------------------+                    +-------------------------------------+
```

* **Compatibilité des périphériques :** Compatible avec la quasi-totalité des claviers et souris filaires USB standards, ainsi qu'avec les ensembles sans fil munis d'un récepteur USB dongle 2.4 GHz.
* **Option USB-C OTG :** Vous pouvez aussi raccorder votre clavier directement au port USB-C natif via un adaptateur OTG.

---

## 🚦 6. Diagnostic par la LED RGB WS2812 (GP16)

La LED RGB intégrée sert d'indicateur matériel d'état en temps réel :

| Couleur de la LED | Animation | Signification |
| :--- | :--- | :--- |
| 🟧 **Orange doux** | Pulsation lente | Initialisation du système et chargement de la ROM Mac Plus. |
| 🟩 **Vert continu** | Respiration lente | **Système prêt !** Le bureau Finder est actif et attend vos actions. |
| 🟨 **Ambre brillant**| Flashs rapides | Lecture de secteurs de données sur la carte MicroSD. |
| 🟪 **Magenta vif** | Flashs rapides | **Écriture sur la MicroSD :** Sauvegarde de fichiers ou de dessins. |
| 🔴 **Rouge continu**| Clignotement alarme | Erreur MicroSD : vérifiez le câblage SPI ou le formatage FAT32 avec `umac0.img`. |

---

## 🔋 7. Alimentation du Montage

1. **Par câble USB-C :** La solution la plus pratique. Raccordez le port USB-C à un chargeur de téléphone standard (5V / 1A ou 2A).
2. **Par alimentation fixe 5V :** Raccordez le fil positif 5V à la pastille **`5V` (VBUS)** et le fil négatif à **`GND`**.
3. **Par batterie rechargeable (Portable) :** Branchez une batterie lithium 18650 (3.7V) via un module chargeur **TP4056 avec élévateur Booster 5V intégré**, alimentant les pastilles `5V` et `GND`.

---

## 📜 Licence Ouverte & Crédits

Ce projet est un logiciel et un matériel open-source distribué sous la **Licence MIT**. Vous êtes libre de l'utiliser, l'étudier, l'améliorer et le partager.

Développé, optimisé et documenté avec soin par **SCHUBIGER.CL** ([https://schubiger.cl](https://schubiger.cl)). Merci de conserver la mention d'origine dans tout projet dérivé.
