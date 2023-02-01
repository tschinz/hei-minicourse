# Souder le PCB

Il s'agit de souder des composants sur le PCB.

```{figure} resources/pcb.png
---
width: 80%
name: pcb 2
---
PCB ATtiny
```

## Souder le condensateur `C1`.

Il s'agit du petit composant jaune.

```{figure} resources/pcb-positions-01.svg
---
width: 80%
name: condensateur c1
---
Condensateur `C1`
```

## Souder les résistances `R1` à `R7`.

Ce sont les composants, sous la forme suivante.

```{figure} resources/pcb-positions-02.svg
---
width: 80%
name: résistance r1-r7
---
Résistance `R1` à `R7`.
```

Pliez les extrémités du dart, insérez le composant et pressez-le complètement contre le circuit imprimé. Coupez les pattes en laissant dépasser environ 2 mm.

Chaque résistance a des anneaux de couleur avec lesquels on peut lire sa valeur.

```{figure} resources/resistor-color-code.svg
---
width: 50%
name: code couleur de la résistance
---
Code couleur de la résistance
```

```{admonition} Résistances dans notre cas.
$R_2 = R_3 = R_4 = 22k\Omega$.
* Rouge-Rouge-Noir-Rouge-Brun

$R_5 = R_7 = R_9 = 33k\Omega$.
* orange-orange-noir-rouge-marron

$R_6 = R_8 = R_{10} = 82k\Omega$.
* gris-rouge-orange-or
```

## Soudure des boutons-poussoirs `S2` à `S7`.

Ce sont les boutons de direction et les deux boutons d'action.

```{figure} resources/pcb-positions-03.svg
---
width: 80%
name: bouton pcb
---
bouton `S2`- `S7`
```

## Soudure du bouton poussoir `S1`.

Il s'agit du bouton qui permet d'allumer la console.

```{note}
Il n'y a pas de sens de montage prédéfini.
```

```{figure} resources/pcb-positions-04.svg
---
width: 80%
name: pcb switch
---
interrupteur `S1`
```

## Souder le socle du circuit intégré `U1`.

Le processeur est enfiché dans ce socle.

```{important}
Attention au sens de montage ! L'encoche sur le côté du petit condensateur jaune.
```

```{figure} resources/pcb-positions-05.svg
---
width: 80%
name: socle pcb cpu
---
Socle du processeur `U1`
```

## Soudez le trimmer `R8`.

Ce composant sert à régler le volume à l'aide du bouton blanc.

```{figure} resources/pcb-positions-06.svg
---
width: 80%
name: potentiomètre pcb
---
Trimmer `R8`
```

## Souder le buzzer `SP1`.

C'est le haut-parleur qui peut émettre des sons.

```{important}
Attention à la direction ! Le `+` sur le côté `+`.
```

```{figure} resources/pcb-positions-07.svg
---
width: 80%
name: buzzer pcb
---
Buzzer `SP1`
```

## Souder le contact de la pile `G1`.

Il doit être bien chauffé et centré. Celui-ci établit le contact avec la batterie.

```{important}
Le contact a d'un côté des butées qui maintiennent la pile en place et de l'autre une ouverture pour insérer la pile, de sorte qu'il ne peut être monté que dans un sens.
```

```{figure} resources/pcb-batteryholder.jpeg
---
width: 30%
name: porte-batterie pcb
---
Porte-pile
```

## Installer le processeur `ATtiny 85`.

Mise en place du circuit intégré `ATtiny 85` dans le socle `U1`.

````{important}
Placer l'encoche du circuit intégré ATtiny 85 dans la même direction que l'encoche du socle.

```{figure} resources/pcb-positions-08.svg
---
width: 80%
name: pcb cpu socket install
---
Installer le processeur dans le socket `U1`.
```
````

## Souder l'écran

Il existe deux versions d'écran. Utilise les instructions qui correspondent au tien.

### Écran OLED Joy-it SBC-OLED01 0.96''.

Soudez l'écran au point de connexion à 4 pôles `J2`.

```{important}
Pour que l'écran repose de manière plane et stable sur le PCB, vous pouvez installer le support imprimé en 3D à l'opposé du point de connexion.
```

```{figure} resources/pcb-positions-09.svg
---
width: 80%
name: pcb oled joyit
---
Écran Oled 0.96'' SBC-OLED01
```

### Écran OLED Adafruit 1.3''

Soudez l'écran au point de connexion à 8 pôles `J3`.

```{important}
Pour que l'écran repose de manière plane et stable sur le PCB, vous pouvez installer le support imprimé en 3D à l'opposé du point de connexion.
```

```{figure} resources/pcb-positions-09-1.svg
---
width: 80%
name: pcb oled adafruit
---
Écran Oled 1.3'' Adafruit
```