# Arduino IDE

La toolchain permet de développer des programmes pour un processeur donné. Elle doit être installée et configurée au début.

## Installation

Installez d'abord l'outil de développement Arduino IDE que vous pouvez télécharger [ici](https://www.arduino.cc/en/software).

## Configuration

### Paramètres

Ouvrez les paramètres :

* Cochez les cases `compilation` et `upload`.
* Copiez le lien suivant dans le champ `Additional Board Manager URLs`.

```text
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

```{figure} resources/arduino-preferences.svg
---
width: 90%
name: arduino preferences-v1
---
Préférences Arduino IDE
```

### Installation de la librairie du processeur

Ouvrez sous `Tools` => `Board` => `Board Manager...` le Boardmanager.

```{figure} resources/arduino-boardmanager.png
---
width: 50%
name: arduino boardmanager-v1
---
Outils Arduino Boardmanager
```

Cherchez `attiny` et installez la dernière version de `attiny` de David A. Mellis.

```{figure} resources/arduino-boardmanager-attiny.png
---
width: 80%
name: arduino boardmanager attiny-v1
---
Bibliothèque Arduino Boardmanager ATtiny
```

### Installation de la librairie d'écran

Ouvrir le gestionnaire de librairies sous `Tools` => `Manage Libraries...`.

```{figure} resources/arduino-managelibraries.png
---
width: 40%
name: arduino manage libraries-v1
---
Outils Arduino Manage Libraries
```

Cherchez `ssd1306xled` et installez le dernier sera la librairie `ssd1306xled`vopn Tejashwi Kalp Taru.

```{figure} resources/arduino-librarymanager-ssd1306xlcd.png
---
width: 80%
name: arduino librarymanager-v1
---
Gestionnaire de librairie Arduino
```

### Configuration du matériel

Configurer le programme pour qu'il puisse programmer l'ATTiny85 dans les différents menus `Tools`.

* Carte : `ATtiny25/45/85`.
* Processeur : `ATtiny85`.
* Horloge : `interne 16MHz`.
* Port : En fonction de votre système USB SerialPort
* Programmeur : `Arduino as ISP`.

```{figure} resources/arduino-attiny85.svg
---
width: 80%
name: board settings-v1
---
Paramètres du matériel Arduino
```

## Compiler et programmer

Les deux boutons en haut à droite permettent de compiler et de programmer le code ouvert.

```{figure} resources/arduino-gui.png
---
width: 80%
name: arduino gui-v1
---
Arduino GUI
```

```{note}
Si vous êtes intéressés, vous pouvez aussi lire la fiche technique du processeur pour en savoir plus sur le processeur.

[Fiche technique du processeur](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook/content-de/arduino/attiny-console/resources/microcontroller-attiny-datasheet.pdf)
```