# Souder le PCB

Il s'agit de souder des composants sur le PCB.

```{figure} resources/pcb.png
---
width: 80%
name: pcb 2-v1
---
PCB ATtiny
```

## Souder le condensateur `C1`.

Il s'agit du petit composant jaune.

```{figure} resources/pcb-positions-01.svg
---
width: 80%
name: condensateur c1-v1
---
Condensateur `C1`
```

## Souder les résistances `R1` à `R7`.

Ce sont les composants, sous la forme suivante.

```{figure} resources/pcb-positions-02.svg
---
width: 80%
name: résistance r1-r7-v1
---
Résistance `R1` à `R7`.
```

Pliez les extrémités des fils, insérez le composant et pressez-le complètement contre le circuit imprimé. Coupez les pattes en laissant dépasser environ 2 mm.

Chaque résistance a des anneaux de couleur avec lesquels on peut lire sa valeur.

```{figure} resources/resistor-color-code.svg
---
width: 50%
name: resistor color code-v1
---
Code couleur de la résistance
```

```{admonition} Résistances dans notre cas.
$R_1 = R_4 = R_7 = 22k\Omega$.
* Rouge-Rouge-Noir-Rouge-Brun

$R_2 = R_5 = 33k\Omega$.
* orange-orange-noir-rouge-brun

$R_3 = R_6 = 82k\Omega$.
* Gris-rouge-orange-or
```

## Soudure des boutons-poussoirs `S2` à `S6`.

Ce sont les boutons de direction et le bouton d'action.

```{figure} resources/pcb-positions-03.svg
---
width: 80%
name: pcb bouton-v1
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
name: pcb switch-v1
---
commutateur `S1`
```

## Souder le socle du circuit intégré `U1`.

Le processeur est enfiché dans ce socle.

```{important}
Attention au sens de montage ! L'encoche sur le côté du petit condensateur jaune.
```

```{figure} resources/pcb-positions-05.svg
---
width: 80%
name: pcb cpu socket-v1
---
Socle de processeur `U1`
```

## Soudez le trimmer `R8`.

Ce composant sert à régler le volume à l'aide du bouton blanc.

```{figure} resources/pcb-positions-06.svg
---
width: 80%
name: pcb potentiomètre-v1
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
name: pcb buzzer-v1
---
Buzzer `SP1`
```

## Soude le contact de la pile.

Il doit être bien chauffé et centré. Celui-ci établit le contact avec la batterie.

```{important}
Le contact a d'un côté des butées qui maintiennent la pile en place et de l'autre une ouverture pour insérer la pile, de sorte qu'il ne peut être monté que dans un sens.
```

```{figure} resources/pcb-batteryholder.jpeg
---
width: 30%
name: pcb batteryholder-v1
---
Porte-piles
```

## Installer le processeur `ATtiny 85`.

Mise en place du circuit intégré `ATtiny 85` dans le socle `U1`.

````{important}
Placer l'encoche du circuit intégré ATtiny 85 dans la même direction que l'encoche du socle.

```{figure} resources/pcb-positions-08.svg
---
width: 80%
name: pcb cpu socket install-v1
---
Installer le processeur dans le socket `U1`.
```
````

## Souder l'écran

Souder l'écran sur le point de connexion à 4 pôles.

```{important}
Pour que l'écran repose de manière plane et stable sur le PCB, vous pouvez installer le support imprimé en 3D à l'opposé du point de raccordement.
```

```{figure} resources/pcb-positions-09.svg
---
width: 80%
name: pcb oled-v1
---
Écran Oled SBC-OLED01
```