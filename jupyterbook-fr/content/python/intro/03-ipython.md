---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"deletable": true, "editable": true}

# ipython 

[ipython](https://ipython.org) est une version _interactive_ de l'interpréteur Python. Il offre un certain nombre d'extras qui sont utiles pour l'écriture de code. Le code "ipython" est presque toujours du code "Python", et les différences n'ont généralement d'importance que si l'on travaille sur le code dans un environnement interactif.

## ipython et Jupyternotebook

Le bloc-notes "Jupyter" est un bon exemple d'environnement interactif - vous modifiez le code pendant qu'il s'exécute et vérifiez les réponses pendant que vous exécutez des cellules. Comme vous pouvez avoir beaucoup de résultats à moitié terminés dans un script interactif, vous voulez probablement faire le moins d'erreurs possible. C'est le but de `ipython`.

`ipython` donne accès au système d'aide/documentation, offre la complétion par tabulation des noms de variables et de fonctions, vous permet de voir quelles méthodes sont présentes dans un module ...

```{code-cell} ipython3
---
deletable : true
editable : true
jupyter :
  outputs_hidden : true
---
## Essayer l'autocomplétion ... il fonctionne sur les fonctions qui sont dans le champ d'application

print

# it also works on variables

long_but_helpful_variable_name = 1

long_but_helpful_variable_name
```

+++ {"deletable" : true, "editable" : true}

---

Cela fonctionne avec des modules pour lister les méthodes et les variables disponibles. Prenez par exemple le module "math" :

```{code-cell} ipython3
---
deletable : true
editable : true
jupyter :
  outputs_hidden : false
tags : []
---
import math

math.isinf # Try completion on this

help(math.isnan)

# try math.isinf() and hit <kbd>Shift</kbd>+<kbd>Tabulator</kbd> while the cursor is between the parentheses
# you should see the same help pop up.

# math.isinf()
```

+++ {"deletable": true, "editable": true}

---

Il fonctionne pour les fonctions qui acceptent des arguments spéciaux et vous dit ce que vous devez spécifier.

Essayez-le et essayez d'ajouter un <kbd>Tabulator</kbd> aux parenthèses si vous utilisez vous-même cette fonction :

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
tags: [raises-exception]
---
import string
string.capwords("the quality of mercy is not strained")

string.capwords()
```

+++ {"deletable": true, "editable": true}

## Commandes en ligne de commande

Il offre également la possibilité d'exécuter des commandes en ligne de commande en utilisant le shell/système de fichiers sous-jacent. Ces erreurs doivent être marquées au début de chaque ligne avec un `!`.. **Ce n'est plus du code Python**.

```{code-cell} ipython3
---
deletable : true
editable : true
jupyter :
  outputs_hidden : false
---
# execute les commandes simples du shell unix

!ls

!echo ""

!pwd
```

+++ {"deletable" : true, "editable" : true}

---

## Magics

Une autre possibilité est d'utiliser la fonctionnalité __cell magic__ pour demander au notebook de changer la cellule en quelque chose d'autre (ici, tout ce qui se trouve dans la cellule est interprété comme un shell Unix). Pour cela, il faut indiquer le **magic** au début de la cellule. Ces commandes commencent par `%%` ou `%`.

```{code-cell} ipython3
---
deletable : true
editable : true
jupyter :
  outputs_hidden : false
---
%%sh

ls -l
echo ""
pwd
```

+++ {"deletable" : true, "editable" : true}

---

  - Un "%" est une fonction magique d'une seule ligne qui peut être placée n'importe où dans la cellule.
  - Un `%%` est une fonction magique à l'échelle de la cellule.

```{code-cell} ipython3
---
deletable : true
editable : true
jupyter :
  outputs_hidden : true
---
%magic # pour voir EVERYTHING dans le système magique !
```

+++ {"deletable" : true, "editable" : true}

Fonctions magiques utiles :

   - `%matplotlib inline` fait en sorte que les tracés apparaissent dans le bloc-notes et non dans une fenêtre externe.
   - `%run FILE` exécute le contenu du fichier à la place de la cellule indiquée
   - `%%timeit` mesure le temps que met la cellule à s'exécuter

---

+++ {"deletable" : true, "editable" : true}

Vous pouvez également exécuter ipython dans le terminal/shell de votre ordinateur. Vous verrez qu'une partie de l'interactivité fonctionne également dans un environnement texte, mais que les aides contextuelles ne sont pas toutes aussi utiles que dans les carnets de notes.