# Tâches à accomplir

## Chiffre de César

Le cryptage est basé sur le [Chiffre de César](https://en.wikipedia.org/wiki/Caesar_cipher).  Il s'agit de l'une des techniques de cryptage les plus simples et les plus répandues. L'alphabet est décalé de $k$, ce qui permet de relier différentes lettres entre elles. Cela signifie que pour un chiffrement donné, les lettres correspondent toujours les unes aux autres.

```{important}
   Le chiffrement de César n'offre aujourd'hui essentiellement plus aucune sécurité de communication.
```

```{figure} resources/01-caesar_cipher.svg
---
width: 40%
name: Chiffre de César
---
Chiffre de César avec $k = 3$ Source : Wikipedia
```

### Tâches
Tout d'abord, nous mettons en œuvre un chiffrement César à titre d'exemple. Cela se fait en plusieurs étapes :
1. vérifier si le caractère est une lettre
2. recherche de l'index de la lettre
3. incrémenter ou décrémenter l'index.
4. recherche de la nouvelle lettre

````{admonition} Tâche 1 - Lire une chaîne de caractères
:class : dropdown
Essaie de lire la lettre `"H"`.

```python
# TODO 1
```
````

````{admonition} Tâche 2 - Vérifier si le caractère est une lettre
:class : dropdown
Il faut contrôler si le `caractère` est présent dans l'`alphabet`.
Nous allons implémenter cela dans la fonction `isLetter()`.

```python
# TODO 2
```
````

````{admonition} Tâche 3 - Rechercher l'index des lettres
:class : dropdown
Trouver l'index des `caractères` dans la liste `alphabet`.
Nous allons implémenter cela dans la fonction `idxOfLetter()`.

```python
# TODO 3
```
````

````{admonition} Tâche 4 - Incrémenter ou décrémenter l'index
:class : dropdown
La valeur `k` peut être positive ou négative. Les cas spéciaux `<0` et `>25` doivent aussi être pris en compte.
Nous allons l'implémenter dans la fonction `incrementIndex()`.

```python
# TODO 4
```
````

````{admonition} Tâche 5 - Chiffrage de César
:class : dropdown
Implémenter l'encodage dans la fonction `cesarEncoding()` et la tester.

```python
# TODO 5
```
````

```{important}
Félicitations vous venez de créer une machine de chiffrement César
```

## théorie Enigma

### Désignations

* **Panneau de connexion** - le panneau de connexion devant la machine, peut relier deux lettres différentes. Il s'agit d'un niveau de confusion supplémentaire
**Rotors** - entre la planche à fiches et le réflecteur, les trois rotors à gauche, au centre et à droite peuvent être placés dans une certaine position afin d'obtenir un mélange différent.
* **Réflecteur** - le réflecteur reçoit les signaux du rotor gauche et les lui renvoie, le codage du réflecteur ne peut pas être modifié. Il permet à la machine d'encoder et de décoder sans modifier aucun paramètre.

### Algorithme

La machine Enigma fonctionne de la même manière que l'algorithme Cesar mais avec une structure plus complexe.

```{figure} ./resources/01-enigma_diagram.jpg
---
width: 80%
name: Diagramme Enigma 2ß
---
Diagramme Enigma Source : Louise Dade
```

### Paramètre

Pour décoder ce qu'une autre machine a encodé, il faut que les conditions suivantes soient remplies :
* La même machine avec le même nombre et les mêmes types de rotors et de réflecteurs.
* Les réglages du plugboard doivent être les mêmes.
* Même position de départ des rotors.

Toutes ces informations étaient modifiées quotidiennement, les réglages exacts se trouvaient dans une "feuille de code" publiée chaque mois.

```{figure} ./resources/01-enigma_codesheet.jpg
---
width: 80%
name: Feuille de code Enigma
---
Feuille de code WWII Source : Nazis
```

**Types de rotor et de réflecteur**.

Pendant la période d'utilisation d'Enigma, il existait de nombreuses versions différentes avec des rotors et des réflecteurs différents. Sur un total de 5 rotors possibles, 3 différents devaient être utilisés chaque matin. En principe, les réflecteurs ne changeaient pas.

| clé       | type | dispositif | utilisation |
|-----------|------------------|----------------------------|-------------------------------|
| `etw`     | rotor ETW        | ABCDEFGHIJKLMNOPQRSTUVWXYZ | Enigma I |
| `i`       | Rotor I          | EKMFLGDQVZNTOWYHXUSPAIBRCJ | 1930 Enigma I |
| `ii`      | Rotor II         | AJDKSIRUXBLHWTMCQGZNPYFVOE | 1930 Enigma I |
| `iii`     | Rotor III        | BDFHJLCPRTXVZNYEIWGAKMUSQO | 1930 Enigma I |
| `iv`      | Rotor IV         | ESOVPZJAYQUIRHXLNFTGKDCMWB | Décembre 1938 M3 Army |
| `v`       | Rotor V          | VZBRGITYUPSDNHLXAWMJQOFECK | Décembre 1938 M3 Army |
| `vi`      | Rotor VI         | JPGVOUMFYQBENHZRDKASXLICTW | 1939 M3 & M4 Naval (FEB 1942) |
| `vii`     | Rotor VII        | NZJHGRCXMYSWBOUFAIVLPEKQDT | 1939 M3 & M4 Naval (FEB 1942) |
| `viii`    | Rotor VIII       | FKQHTLXOCBJSPDZRAMEWNIUYGV | 1939 M3 & M4 Naval (FEB 1942) |
| `a`       | Reflector A      | EJMZALYXVBWFCRQUONTSPIKHGD | |
| `b`       | Réflecteur B     | YRUHQSLDPXNGOKMIEBFZCWVJAT | |
| `c`       | Réflecteur C     | FVPJIAOYEDRZXWGCTKUQSBNMHL | |
| `custom`  | Personnalisé     | tel que donné par l'utilisateur | |

### Taille du code

La taille du code indique le nombre de possibilités de cryptage.

La formule du nombre total de possibilités de code est la suivante :

$$(5*4*3)*26^3*\frac{26!}{6!*10!*2^{10}} = 158 962 555 247 826 360 000$$

Cette formule est décomposée et expliquée ci-dessous.

**Sélection des rouleaux**.

Parmi 5 rouleaux, on en choisit 3 et on les place comme on le souhaite.

$5*4*3 = 60$ Combinaisons de rouleaux possibles

**Position de départ des rouleaux**.

3 rouleaux de 26 positions possibles chacun

$26^3 = 17576$ positions de départ des rouleaux

**Combinaisons de planches à fiches**.

Ici, 2 lettres peuvent être reliées entre elles. Au total, 10 combinaisons de connecteurs étaient possibles. 6 étaient donc inutilisées.

* $26!$ - Combinaisons possibles de l'alphabet
* $6!$ - 6 connexions sont restées inutilisées.
* $10!$ - Il n'y a que 10 connexions à effectuer.
* $2^{10}$ - Connecter A <=> Z est la même chose que Z <=> A

$$ \frac{26!}{6!*10!*2^{10}} = 150 738 274 937 250$$

### Démonstration

Comme démonstration, vous pouvez regarder la vidéo Youtube suivante.

[Démonstration Enigma](https://www.youtube.com/watch?v=5Tqc71iy8jA)

### Préparation

Avant même d'écrire du code, un diagramme de classes a été créé. L'idée est de créer une classe de `EnigmaMaschine` qui possède plusieurs objets `Scrambler`. Un panneau de connexion, les rotors mais aussi le réflecteur fonctionnent en principe en reliant ou en mélangeant différentes lettres (scramble). Bien que leur structure mécanique soit différente, leur fonctionnement est le même.

```{figure} resources/01-enigma-flow.svg
---
width: 90%
name: Enigma Flow
---

Flux de données EnigmaMachine
```

Le diagramme de classe de l'application :

```{figure} resources/01-enigma_classdiagram.svg
---
width: 70%
name: Diagramme de classes Enigma
---
Diagramme de classes Enigma
```

### Brouilleur

Tout d'abord, nous allons écrire la classe Scrambler.

```{figure} resources/01-enigma_scrambler_classdiagram.svg
---
width: 35%
name: Scrambler Classdiagram
---
Diagramme de classe du brouilleur
```

```{important}
Avec l'aide de la commande `print()`, vous devez déboguer votre code vous-même.
```

````{admonition} Tâche 6 - Types de clés
:class : dropdown
La clé de type est indiquée sous forme de chaîne de caractères. Les valeurs possibles sont : `"etw", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii"` pour les rotors et `"a", "b", "c"` pour les réflecteurs. Le brouilleur devrait également pouvoir reconnaître les valeurs suivantes comme étant valables.

* Lettres majuscules - `"I", "II", ViIi`.
* Trait d'union - `"v-iii", e-t-w`.
* Espaces - `"v iii", "e t w"`
* Soulignement - `"v_iii", e_t_w`.
* Combinaisons des erreurs ci-dessus.

`self.type_key` devrait contenir une chaîne nettoyée

```python
# TODO 6
```
````

````{admonition} Tâche 7 - Chaîne vers tableau
:class : dropdown
La configuration est exprimée par une chaîne de caractères sous la forme suivante :

```python
str_config = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
```
Cette chaîne doit être modifiée sous la forme d'un tableau.

```python
config = ["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"]
```

```python
# TODO 7
```
````

````{admonition} Tâche 8 - Chaîne tournante
:class : dropdown
A chaque étape d'un rotary, la chaîne doit être tournée vers la gauche.

* Le `"test"` devient `"estT"` s'il doit être déplacé de `n=1`.
* `"Test"` devient `"stTe"` si l'on veut déplacer de `n=2`.

```python
# TODO 8
```
````

### Enigma Machine

Le brouilleur de classe est maintenant écrit et testé.

```{figure} resources/01-enigma_enigmamachine_classdiagram.svg
---
width: 35%
name: EnigmaMachine Classdiagram
---
Diagramme de classes EnigmaMachine
```

`````{admonition} Exercice 9 - Planche de connecteurs
:class : dropdown
La configuration du panneau de prises est donnée de la manière suivante.
```python
self.plugboard_config = ["AZ", "BY", "CX", "DW", "EV", "FU", "GT", "HS", "IR", "JQ", "KP", "LO", "MN"]
```

Cette configuration doit être transférée sous la forme `type_key`. Dans l'exemple ci-dessus :
```python
ZYXWVUTSRQPONMLKJIHGFEDCBA
```

Pour qu'à l'alphabet `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"` dans l'exemple ci-dessus corresponde `A <-> Z` ainsi que `B <-> Y` etc.

````{important}
Une chaîne Python ne peut pas être modifiée, la chaîne doit être recréée.
```python
chaîne = "ABC"
string[0] = "D" # Ne fonctionne pas
chaîne = "D" + chaîne[1 :] # "DBC"
```
````

```python
# TODO 9
```
`````

````{admonition} Tâche 10 - Configuration d'Enigma
:class : dropdown
La configuration d'Enigma doit pouvoir être affichée afin de pouvoir la partager.

La fonction `printEnigmaSetup()` devrait donner le résultat suivant ou quelque chose de similaire. Il est important de mentionner que notre machine Enigma peut présenter un nombre quelconque de rotors.

```texte
Configuration Enigma
============

* Rotor 0
  - Type : i
  - Clé : USPAIBRCJEKMFLGDQVZNTOWYHX
  - StartPos : 17
* Rotor 1
  - Type : iii
  - Clé : SQOBDFHJLCPRTXVZNYEIWGAKMU
  - StartPos : 23
* Rotor 2
  - Type : iv
  - Clé : RHXLNFTGKDCMWBESOVPZJAYQUI
  - StartPos : 12
* Reflector
  - Type : a
* Plugboard
  - Key : ['AZ', 'BY', 'CX', 'DW', 'EV', 'FU', 'GT', 'HS', 'IR', 'JQ', 'KP', 'LO', 'MN']
```

Utilise pour cela les variables suivantes des objets scrambler :
```python
self.nb_rotors
self.rotors[i].type_key
self.rotors[i].key
self.rotors[i].startpos
self.reflector.type_key
self.reflector.key
self.reflector.startpos
self.plugboard_config
```

```python
# TODO 10
```
````

````{admonition} Tâche 11 - Encodage du caractère
:class : dropdown

Chaque personnage doit passer par tous les brouilleurs. Le caractère a déjà été décodé comme position dans l'alphabet `num`. A l'aide de l'exemple existant, cette valeur doit maintenant passer par chaque brouilleur, par ex. le panneau de connexion :

```python
 num = self.plugboard.passthrough(num)
 ```

Il faut noter que pour passer dans une direction, il faut utiliser la fonction `passthrough()` et dans l'autre direction `passthroughRev()`.

```python
# TODO 11
```
````

## Transmettre des messages cryptés

La dernière tâche consiste à envoyer un message crypté à vos camarades de classe. Pour cela, vous devez leur transmettre le message crypté mais aussi la configuration.

1. préparez un message et une configuration Enigma.
2. cryptez le message
3. donnez à votre collègue le message et les paramètres de configuration
Décodez le message que vous avez reçu de votre collègue.