---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Hello World

La première chose à faire est de se familiariser avec la forme et le ressenti du code Python, car nous ne pouvons pas vraiment discuter des fonctions de Python sans quelques exemples. Voici donc une petite introduction...

```{admonition} Note marginale
Le nom Python est dérivé de *Monty Python's Flying Circus*, ce qui signifie que vous devriez être alerté à la mention d'un [Phrase Book](https://www.youtube.com/watch?v=C1Sw0PDgHU4).
```

## Programme obligatoire de Hello World

```python
# Mon premier programme Hello World
print("Hello World")
```
---
```
Hello World
```

Pour exécuter cet exemple simple, aucune préparation n'est nécessaire, car la commande `print` est intégrée dans Python.
Elle est en fait implémentée comme une *fonction* qui affiche son argument à l'écran. Vous savez maintenant à quoi ressemblent les fonctions Python ! Vous pouvez aussi voir comment écrire un commentaire.

Voici quelques autres façons de faire la même chose.

```python
hello_world_string = "Hello World"
print(hello_world_string)

# Le formatage de la sortie est également possible
print("Mon {:s} programme".format(hello_world_string))
```
---
```
Hello World
Hello World
```

Nous pouvons assigner le message à une variable et l'imprimer directement. Il n'est pas nécessaire de dire à la fonction `print` que `hello_world_string` est une chaîne de caractères. Les noms de variables peuvent contenir des traits de soulignement, des lettres et des chiffres (à l'exception du premier caractère, qui ne peut pas être un chiffre). Les traits de soulignement au début d'une variable sont généralement *"cachés "*, ce qui signifie en fait qu'ils sont un peu plus difficiles à trouver dans un environnement interactif.

```{note}
En fait, string est un objet Python qui comprend qu'il doit être imprimé et réagit en conséquence à l'appel de la fonction print. La fonction "format" fait également partie du répertoire de l'objet string, et nous verrons très souvent ce type d'accès aux "méthodes" d'un objet avec "object.function".
```

## Indentation et structure de bloc

`python` utilise des indentations pour définir des blocs de code, si l'indentation est interrompue, l'interpréteur se plaint. Ceci est important pour la définition de fonctions, d'instructions conditionnelles, de boucles, etc :

```{important}
Le nombre d'indentations est par défaut de `4` espaces, mais il peut théoriquement être choisi librement. Dans un fichier, il faut cependant toujours utiliser le même nombre d'espaces par indentation.
```

### Exemple d'indentation

Nous avons opté pour `2` espaces par indentation.

```python
for i in range(0,5) :
  print("La valeur de i est {} ".format(i), end=" ")
  if i%2 :
    print("qui est un nombre impair")
  else :
    print("qui est un nombre pair")
```

Ceci a la présentation d'un code Python typique - les blocs qui composent une boucle ou les branchements de conditions sont définis par l'indentation.

## Fonctions

```python
def my_first_function(argument1, argument2) :
  """Ceci est la description de la fonction. On l'appelle aussi Docstring.
     Cette fonction renvoie l'argument 1

  Args :
      argument1 (_type_) : _description_
      argument2 (_type_) : _description_

  Retour :
      (_type_) : _description
  """
  return(argument1)
```

```python
print(ma_première_fonction(1,2))
print(my_first_function("Hello world", 0))
help(ma_première_fonction)
```
---
```
1
Hello World

Aide sur la fonction ma_première_fonction dans le module __main__ :

ma_première_fonction(argument1, argument2)
    Ceci est la description de la fonction. Elle s'appelle aussi Docstring.

  Args :
      argument1 (_type_) : _description_
      argument2 (_type_) : _description_

  Retours :
      (_type_) : _description
```

Autre exemple de fonction avec plusieurs valeurs de retour.

```python
def my_second_function(argument1, argument2) :
  """Ceci est la description de la fonction. On l'appelle aussi Docstring.
     Cette fonction renvoie l'argument 1

  Args :
      argument1 (_type_) : _description_
      argument2 (_type_) : _description_

  Retours :
      (_type_) : _description
  """
  return(argument1, argument2)
```
```python
print(my_second_function(1,2))
print(my_second_function("Hello world", 0))
help(my_second_function)

a,b = my_second_function(1,2)
print(a)
print(b)
```
---
```
(1, 2)
('Hello world', 0)
Aide sur la fonction mon_second_function dans le module __main__ :

"""Ceci est la description de la fonction. Elle s'appelle aussi Docstring.
     This function returns argument 1

  Args :
      argument1 (_type_) : _description_
      argument2 (_type_) : _description_

  Retours :
      (_type_) : _description
  """

1
2
```

Les fonctions peuvent renvoyer de nombreux arguments qui reviennent sous forme de `tuple`. Il est facile de *déballer* les valeurs renvoyées.

```{note}
Comme "Python" est un langage interprété, il faut définir les fonctions avant qu'elles n'apparaissent dans le code.
```

## Modules

La force de `python` réside probablement dans la manière dont il favorise le partage et crée une communauté d'utilisateurs. Avant de pouvoir faire beaucoup de choses avec `python`, nous devons en général importer les *modules* contenant les fonctions supplémentaires dont nous avons besoin.

Par exemple, la bibliothèque Python standard contient des modules pour les opérations de base du système de fichiers, la manipulation de chaînes de caractères, les fonctions mathématiques, la création de processus, et bien plus encore. La liste complète est disponible dans la [documentation python](https://docs.python.org/3/py-modindex.html).

### `import` exemples

Importation d'un module complet

```python
import math

print(math.sin(math.pi/2))
print(math.cos(math.pi/2))
```
---
```
1.0
6.123233995736766e-17
```
---

Cette `importation` importe un module entier. Parfois, nous voulons seulement importer des parties pour gagner du temps ou pour éviter des violations de noms.

```python
from math import sin, pi

print(sin(pi/2)) # importé
print(cos(pi/2)) # non importé
```
---
```
1.0
---------------------------------------------------------------------------
NameError Traceback (dernier appel récent)
<ipython-input-7-2b3c4d0b7471> dans <module>
      4
      5 #
----> 6 print(cos(pi/2))

NameError : le nom 'cos' n'est pas défini
```

Pour éviter les violations de noms, il est possible d'attribuer des noms différents à des fonctions de modules différents, mais qui ont le même nom.y.

```python
from math import sin, pi
from cmath import sin as csin

print(sin(pi/2))
print(csin(pi/2))
```
---
```
1.0
(1+0j)
```
---

Dans l'exemple ci-dessus, les modules `math` et `cmath` possèdent la fonction `sin`. C'est pourquoi la fonction du module `cmath` est renommée en `csin`.