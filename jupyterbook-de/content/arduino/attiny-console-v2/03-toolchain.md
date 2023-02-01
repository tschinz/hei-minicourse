# Arduino IDE

Die Toolchain erlaubt es Programme für den gegebenen Prozessor zu entwickeln. Diese muss zu Beginn installiert und konfiguriert werden.

## Installation

Installieren Sie zuerst das Entwicklungs Tool Arduino IDE welches Sie [hier](https://www.arduino.cc/en/software) herunterladen können.

## Konfiguration

### Einstellungen

Öffnen Sie die Einstellungen:

* Setzen Sie die Checkboxen `compilation` sowie `upload`.
* Kopieren sie den folgenden Link in das Feld `Additional Board Manager URLs`

```text
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

```{figure} resources/arduino-preferences.svg
---
width: 90%
name: arduino preferences
---
Einstellungen Arduino IDE
```

### Installation Prozessor Library

Öffnen Sie unter `Tools` => `Board` => `Board Manager...` den Boardmanager.

```{figure} resources/arduino-boardmanager.png
---
width: 50%
name: arduino boardmanager
---
Arduino Tools Boardmanager
```

Suchen Sie nach `attiny` und installieren Sie die letzte Version von `attiny` von David A. Mellis.

```{figure} resources/arduino-boardmanager-attiny.png
---
width: 80%
name: arduino boardmanager attiny
---
Arduino Boardmanager ATtiny Library
```

### Installation der Bildschirm Library

Öffnen Sie den unter `Tools` => `Manage Libraries...` den Librarymanager.

```{figure} resources/arduino-managelibraries.png
---
width: 40%
name: arduino manage libraries
---
Arduino Tools Manage Libraries
```

Suchen Sie nach `ssd1306xled` und installieren Sie die letzte werden der Library `ssd1306xled`vopn Tejashwi Kalp Taru.

```{figure} resources/arduino-librarymanager-ssd1306xlcd.png
---
width: 80%
name: arduino librarymanager
---
Arduino Librarymanager
```

### Hardware Einstellungen

Konfigurieren Sie das Program damit es den ATTiny85 Programmieren kann unter den verschiedenen `Tools` Menus.

* Board: `ATtiny25/45/85`
* Prozessor: `ATtiny85`
* Clock: `Internal 16MHz`
* Port: Abhängig von Ihrem System USB SerialPort
* Programmer: `Arduino as ISP`

```{figure} resources/arduino-attiny85.svg
---
width: 80%
name: board settings
---
Arduino Hardware Einstellungen
```

## Kompilieren und Programmieren

Die beiden Knöpfe oben rechts erlauben es den geöffneten Code zu kompilieren und zu programmieren.

```{figure} resources/arduino-gui.png
---
width: 80%
name: arduino gui
---
Arduino GUI
```

```{note}
Falls interessiert könnte Ihr auch das Datasheet des Prozessors als Nachtlektüre lesen um mehr über den Prozessor zu erfahren.

[Datenblatt Prozessor](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook/content-de/arduino/attiny-console/resources/microcontroller-attiny-datasheet.pdf)
```