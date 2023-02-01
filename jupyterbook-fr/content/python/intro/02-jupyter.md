---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.9'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"deletable": true, "editable": true}

(section:jupyter_notebook)=
# Jupyter Notebooks

Dans tous nos exemples, nous utiliserons le système de bloc-notes `jupyter` et dans les blocs-notes eux-mêmes une version de Python, connue sous le nom de `ipython`.

Le carnet de notes est un document __vivant__ qui peut contenir plusieurs types de contenus différents. Il peut s'agir d'éléments de texte formatés en Markdown ou de questions de programme qui peuvent également être exécutées. Actuellement, nous considérons la page web statique dans laquelle le code ne peut pas être exécuté. Pour cela, il faut lancer la page en tant que livre interactif de Noritz sur Binder dans l'icône de raquette.

```{figure} img/rocket-icon.png
---
width: 80%
name: Rocket icon
---
Démarrage du Jupyter Notebook
```

Vous pouvez utiliser les carnets comme bloc-notes pour écrire du code et le documenter en même temps.
C'est comme un carnet de laboratoire, mais pour la manipulation de données et la programmation.
Vous pouvez également exporter le document créé au format PDF pour créer un rapport de laboratoire.

Notez que le carnet de notes n'est pas enregistré sur Binder, dès que vous fermez le site, vos modifications sont perdues. N'oubliez pas de sauvegarder le document sur votre ordinateur si vous souhaitez le conserver.

+++

Un carnet de notes est composé de plusieurs __cellules__ (Cells) qui contiennent différents types de contenus et qui peuvent être _exécutés_ en sélectionnant la cellule et en l'_exécutant_ en appuyant sur le bouton _Run_ ou en tapant "Shift + Enter".
Les résultats de l'exécution d'une cellule dépendent de son contenu. Elle peut générer une cellule de sortie sous-jacente avec des résultats ou se reformater elle-même.

(section:markdowncells)=
## Cellules de Markdown
Vous trouverez un résumé Markdown [ici](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Le formatage en Markdown se présente comme suit :

````md
### Texte formaté

Nous utilisons ici une version presque prête du texte formaté, connue sous le nom de "Markdown", pour créer un contenu qui peut être formaté de manière à ressembler à un document Word, mais qui met également en évidence le formatage prévu, même s'il n'est pas traité. C'est une forme assez utile que l'on peut apprendre à utiliser pour prendre des notes.

Si vous regardez le contenu brut, vous verrez comment on peut

* des puces
  * des puces imbriquées ainsi que
  * du texte en __gras__
  * du texte en _italique_ (ou en surbrillance)


```sh
echo "Code pouvant être mis en évidence pour différentes langues"
ls -l
```

```python
print("y compris Python, les scripts shell Unix, Fortran")

for i in range(0,100):
    print(i)
```

Les symboles et formules mathématiques, peuvent apparaître à l'intérieur d'un texte $2\pi r$ ou sous forme d'équation :

$$
    A = \pi r^2
$$

MAIS vous devez être en mesure de décrire les formules dans le langage $\LaTeX$.

Vous pouvez ajouter des liens comme ceux-ci : [voir aussi la feuille de contrôle Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Et des images comme celle-ci :

![Python Course](./../img/python-course.svg)

````
---
C'est ce qui ressort du paragraphe suivant :

### Texte formaté

Nous utilisons ici une version presque prête à l'emploi du texte, connue sous le nom de "Markdown", pour créer un contenu qui peut être formaté de manière à ressembler à un document Word, mais qui met également en évidence le formatage prévu, même s'il n'est pas traité. C'est une forme assez utile que l'on peut apprendre à utiliser pour prendre des notes.

Si vous regardez le contenu brut, vous verrez comment on peut

* des puces
  * des puces imbriquées ainsi que
  * du texte en __gras__
  * du texte en _cursivité_ (ou en surbrillance).

```sh
echo "Code pouvant être mis en surbrillance pour différentes langues"
ls -l
```

```python
print("y compris Python, scripts shell Unix, Fortran")

for i in range(0,100) :
    print(i)
```

Les symboles et formules mathématiques, peuvent apparaître à l'intérieur d'un texte $2\pi r$ ou sous forme d'équation :

$$
    A = \pi r^2
$$

MAIS vous devez être en mesure de décrire les formules dans le langage $\LaTeX$.

Vous pouvez ajouter des liens comme ceux-ci : [voir aussi la feuille de contrôle Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Et des images comme celle-ci :

![Python Course](img/python-course.svg)

```{note}
Lorsque vous exécutez des cellules avec du code formaté, la cellule est remplacée par la version formatée. Vous pouvez ainsi écrire une page bien formatée avec du code imbriqué qui peut également être exécuté.
```

---

(section:pythoncells)=
## Python-Code

Les cellules définies comme cellules de code contiennent des instructions Python qui sont exécutées lorsque la cellule est exécutée. Si plusieurs cellules contiennent du code, elles seront exécutées dans l'ordre que vous avez choisi (ou si vous choisissez "run all" ou "run all above", elles seront exécutées dans l'ordre dans lequel elles sont listées).

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
solution: hidden
---
## Exemple d'une cellule de code Python simple

print("Bonjour, petit monde")
a = 1
```

+++ {"deletable": true, "editable": true}

Si vous exécutez une cellule de code, c'est la même chose que si vous aviez saisi tout le code dans l'interpréteur. Si vous exécutez une cellule deux fois, c'est comme si vous aviez tout saisi deux fois... le bloc-notes s'en souvient ! Vous pouvez exécuter une partie ou la totalité du bloc-notes, et vous pouvez aussi exécuter les cellules dans un ordre différent. C'est une excellente façon d'expérimenter, mais attention, cela peut aussi être partiellement déroutant.

## Exemple
Voici un petit exemple. Pourquoi la cellule ci-dessous fonctionne-t-elle mais pas la suivante ?

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
print("Compteur {}".format(a))
a += 1
```

+++ {"deletable": true, "editable": true}

Pourquoi cela ne fonctionne-t-il pas ?

```python
print("Compteur {}".format(b))
b += 1
```

et, plus important encore, comment régleriez-vous le problème ?

Démarrez le notebook et éditez la cellule ci-dessous. La cellule peut être modifiée avec <kbd>Shift</kbd>+<kbd>&#9166;</kbd> être exécutés.

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
Solution: hidden
---
# Essayez !
```

```{code-cell} ipython3
:tags: [hide-cell]

## Parce que b n'a pas encore été défini, mais a l'a été dans la cellule précédente.

try:
    print("Compteur {}".format(c))
except:
    print("Compteur")
    c = 1

c += 1
```

## Utiliser Jupyter

Dans ce cours, nous allons résoudre les problèmes de manière interactive sur un serveur Jupyter. Vous avez déjà appris à démarrer le notebook sur [Binder](https://jupyter.org/binder) à l'aide de l'icône Rocket [en début de page](section:jupyter_notebook). Grâce à ce serveur, vous pouvez ajouter, supprimer et compléter le code pour l'exécuter ensuite.

Jupyternotebook est basé sur des cellules, comme nous l'avons déjà mentionné. Les cellules peuvent être soit [texte formaté au format Markdown](section:markdowncells) soit [code Python](section:pythoncells). Chaque cellule peut être exécutée séparément.

Le type de cellule actuel peut être sélectionné dans la Dropbox.

```{figure} img/jupyter_command_bar_celltype.png
---
width: 80%
name: jupyter celltype
---
Sélection ou modification d'un type de cellule
```

De nouvelles cellules peuvent être insérées via le menu `Insert`.

```{figure} img/jupyter_command_bar_insert.png
---
width: 80%
name: jupyter cellinsert
---
Ajouter une cellule
```

Une cellule peut être exécutée soit avec le bouton `Run` soit avec <kbd>Shift</kbd>+<kbd>&#9166;</kbd> peuvent être exécutées. Il est également possible d'exécuter toutes les cellules supérieures ou inférieures via le menu `Cell`.

```{figure} img/jupyter_command_bar_run.png
---
width: 80%
name: jupyter cellrun
---
Exécuter une cellule
```

Dès qu'une cellule est exécutée, elle est visible via un cercle plein en haut à droite. Ce point indique si le noyau Python est actif ou non.

```{figure} img/jupyter_command_bar_running.png
---
largeur : 80%
nom : jupyter cellrunning
---
Le noyau Python est actif
```

De plus, à droite de la cellule se trouve une remarque `ln[<x>]`.

Celle-ci indique si une cellule est actuellement en cours d'exécution `In [*]:`. Ou quand la cellule a été exécutée depuis le démarrage du noyau Python `In [3]:`. Le numéro est incrémenté pour chaque cellule listée.

Si une cellule doit être arrêtée, par exemple si le calcul prend trop de temps, cela peut se faire avec le bouton `Stop`.

```{figure} img/jupyter_command_bar_stop.png
---
largeur : 80%
nom : jupyter cellstop
---
Arrêter une exécution
```

Juste en dessous de la cellule se trouve la fenêtre de l'édition de la cellule en question.

```{note}
Vous devriez maintenant avoir toutes les informations nécessaires pour exécuter Jupter Notebooks.
```
