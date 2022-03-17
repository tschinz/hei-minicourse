# Löten des PCB

Es geht darum auf dem PCB Komponenten zu verlöten.

```{figure} resources/pcb.png
---
width: 80%
name: pcb 2
---
PCB ATtiny
```

## Löten Sie den Kondensator `C1`

Es handelt sich um das kleine gelbe Bauteil.

```{figure} resources/pcb-positions-01.svg
---
width: 80%
name: condensator c1
---
Kondensator `C1`
```

## Löten Sie die Widerstände `R1` bis `R7`

Dies sind die Bauteile, in folgender Form.

```{figure} resources/pcb-positions-02.svg
---
width: 80%
name: resistor r1-r7
---
Resistor `R1` bis `R7`
```

Biegen Sie die Darhtenden, setzen Sie das Bauteil ein und drücken Sie es vollständig gegen die Platine. Schneiden Sie die Beinchen ab und lassen Sie dabei etwa 2 mm herausschauen.

Jeder Wiederstand hat Farbige Ringe mit welchem man deren Wert ablesen kann.

```{figure} resources/resistor-color-code.svg
---
width: 50%
name: resistor color code
---
Wiederstand Farbcode
```

```{admonition} Wiederstände in unserem Fall.
$R_1 = R_4 = R_7 = 22k\Omega$
* Rot-Rot-Schwarz-Rot-Braun

$R_2 = R_5 = 33k\Omega$
* Orange-Orange-Schwarz-Rot-Braun

$R_3 = R_6 = 82k\Omega$
* Grau-Rot-Orange-Gold
```



## Löten der Drucktasten `S2` bis `S6`

Dies sind die Richtungstasten und die Aktionstaste.

```{figure} resources/pcb-positions-03.svg
---
width: 80%
name: pcb button
---
Knopf `S2`- `S7`
```

## Löten des Druckknöpfes `S1`

Dies ist der Knopf, mit dem die Konsole eingeschaltet wird.

```{note}
Es gibt keine vorgegebene Montagerichtung.
```

```{figure} resources/pcb-positions-04.svg
---
width: 80%
name: pcb switch
---
Schalter `S1`
```

## Löten Sie den Sockel des integrierten Schaltkreises `U1`

In diesen Sockel wird der Prozessor gesteckt.

```{important}
Achten Sie auf die Einbaurichting! Die Kerbe auf der Seite des kleinen gelben Kondensators.
```

```{figure} resources/pcb-positions-05.svg
---
width: 80%
name: pcb cpu sockel
---
Prozessorsockel `U1`
```

## Löten Sie den Trimmer `R8`

Dieses Bauteil dient zur Einstellung der Lautstärke mithilfe des weissen Drehknopfes.

```{figure} resources/pcb-positions-06.svg
---
width: 80%
name: pcb potentiometer
---
Trimmer `R8`
```

## Löten Sie den Buzzer `SP1`

Dies ist der Lautsprecher welcher Töne von sich geben kann.

```{important}
Achten Sie auf die Richtung! Das `+` auf der `+`-Seite
```

```{figure} resources/pcb-positions-07.svg
---
width: 80%
name: pcb buzzer
---
Buzzer `SP1`
```

## Löten Sie den Batteriekontakt an

Er muss gut erhitzt und zentriert werden. Dieser stellt den Kontakt zu Batterie her.

```{important}
Der Kontakt hat auf der einen Seite Anschläge, die die Batterie festhalten, und auf der anderen Seite eine Öffnung zum Einsetzen der Batterie, so dass er nur in eine Richtung montiert werden kann.
```

```{figure} resources/pcb-batteryholder.jpeg
---
width: 30%
name: pcb batteryholder
---
Batteriehalter
```

## Installieren des Prozessors `ATtiny 85`

Einsetzen des integrierten Schaltkreises `ATtiny 85` in den `U1`-Sockel

````{important}
Bringen Sie die Kerbe des integrierten Schaltkreises ATtiny 85 in die gleiche Richtung wie die Kerbe des Sockels.

```{figure} resources/pcb-positions-08.svg
---
width: 80%
name: pcb cpu sockel install
---
Installieren des Prozessors in den Sockel `U1`
```
````

## Löten Sie den Bildschirm an

Sie müssen auswählen ob sie Pac-Man oder Space Invaders spielen möchten. Folgen Sie den jeweiligen Anweisungen.


````{admonition} Pac-Man
Löten Sie den Bildschirm vertikal, um PacMan zu spielen. Anschluss `J1`
```{figure} resources/pac-man.png
---
width: 20%
name: pacman
---
```
````

````{admonition} Space-Invaders
Löten Sie den Bildschirm horizontal, um Space Invaders zu spielen.
```{figure} resources/space-invaders.png
---
width: 20%
name: space invaders
---
````

```{figure} resources/pcb-positions-09.svg
---
width: 80%
name: pcb oled
---
Oled Display SBC-OLED01
```