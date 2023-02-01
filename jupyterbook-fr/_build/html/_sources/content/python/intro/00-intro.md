# Introduction

```{figure} img/python-course.svg
---
width: 30%
name: Python course logo
---
Logo du cours Python
```

Il y a plusieurs choses à savoir sur le langage Python avant de s'y intéresser. La plus importante est peut-être que Python est un langage **interprété** et non un langage *compilé*, de sorte qu'il n'y a pas de traduction en code binaire rapide et exécutable par une machine. Cela place le codage efficace au-dessus de l'exécution rapide et en dit long sur la philosophie de Python en tant que langage : Applicable à une très large classe de problèmes, facile à lire et de haut niveau, de sorte qu'il est facile de réutiliser des logiciels existants et de construire dessus.

Python doit être **simple à utiliser** : vous n'avez pas besoin de spécifier ("déclarer") le type de vos variables ou de vos données avant de les utiliser, et il **convertit automatiquement** d'un type à un autre si cela est possible, lorsque c'est utile. Par exemple, un nombre à virgule flottante `1.0` et un entier `1` sont généralement interchangeables en Python, comme ils le sont dans la vie quotidienne. Si vous n'utilisez plus une variable, vous n'êtes pas obligé de la supprimer explicitement, mais vous pouvez le faire si vous le souhaitez.

Python a un vaste **gestion des exceptions** (Exception handling), ce qui signifie simplement que les erreurs peuvent être gérées par le programme en cours d'exécution et ne conduisent pas toujours à un plantage, qui est géré par le système d'exploitation. En général, c'est une bonne idée d'écrire un code qui comprend ce qui pourrait mal tourner et qui offre une solution élégante si quelque chose tourne mal. Les exceptions conduisent également à une approche *Try it and see* de la programmation. Il peut être plus facile d'écrire un code qui intercepte une erreur que d'essayer d'écrire un code qui prend en compte chaque situation sans erreur.

Python est également un langage **orienté objet**, et il est impossible de lire Python sans comprendre comment il décrit ses objets et y fait ensuite référence. Le principe des langages orientés objet est d'encapsuler des données et des opérations sur ces données dans des "objets" qui peuvent être transmis comme une seule unité et que l'on peut ensuite utiliser sans avoir à connaître toute la structure interne de l'objet. Dans les langages orientés objet, nous décrivons généralement une classe d'objets qui ont certaines propriétés (données, opérations, structure) sans nécessairement connaître les détails de la manière dont ces objets sont implémentés. On peut nous transmettre des classes et nous dire comment les utiliser, les copier, les étendre, etc. sans avoir à les démonter au préalable.

Python est basé sur des **bibliothèques** sous forme de modules que nous `importons` quand nous en avons besoin. Il existe de très nombreux modules dans la bibliothèque Python standard pour presque tout, du niveau du système d'exploitation (créer un répertoire, ouvrir un fichier) à l'accès de haut niveau aux ressources Internet, la manipulation de chaînes de caractères, l'analyse syntaxique d'expressions régulières, les fonctions mathématiques. Dès qu'un module est importé, les fonctions et les classes qui y sont définies sont à la disposition du programme et, pour se simplifier la vie, les noms de toutes ces fonctions et classes sont précédés du nom du module lorsqu'elles sont utilisées. Cela implique certes un peu plus de travail de frappe pour un programmeur, mais cela améliore la lisibilité et rend la vie beaucoup plus facile à toute personne qui développe une bibliothèque.

Lorsque l'on écrit du code utile, il est courant de le regrouper sous la forme d'un **module** et de le distribuer ensuite en téléchargeant un paquet à un emplacement standard celui-ci peut être la bibliothèque [pip](https://pypi.org/project/pip/) ou [conda](https://anaconda.org/conda-forge/repo). Ces paquets sont ensuite distribués aux utilisateurs via ces gestionnaires de paquets, qui sont suffisamment intelligents pour s'assurer que vous installez une version qui fonctionne sur votre machine et (encore plus compliqué) qui correspond à tous les autres paquets installés.

Les deux principaux gestionnaires de paquets pour Python sont [pip](https://pypi.org/project/pip/) et [conda](https://anaconda.org/conda-forge/repo). [pip](https://pypi.org/project/pip/) est un peu plus simple et ne s'occupe vraiment que de l'installation des paquets Python et de leurs dépendances Python.
[conda](https://anaconda.org/conda-forge/repo) est beaucoup plus ambitieux que `pip` - il gère des environnements entiers, qui contiennent aussi des bibliothèques non-Python qui pourraient avoir besoin de paquets. `conda` est plus puissant que pip et tente de remplacer de nombreux autres gestionnaires de paquets qui existent dans le monde non-Python. Si vous choisissez `conda`, vous devriez vraiment tout essayer et essayer de l'utiliser pour gérer tous les paquets. `conda` crée des environnements virtuels qui vous permettent d'avoir plusieurs configurations sur une seule machine - pratique si vous avez des paquets qui nécessitent différentes versions de Python ou qui ont des dépendances incompatibles.

## Lecture de fond

La référence finale pour Python est [www.python.org](https://www.python.org). Cependant, il peut être utile de lire d'abord différents articles sur Wikipedia, en commençant par l'article [Python Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
