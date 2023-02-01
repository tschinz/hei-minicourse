# Partie 2 - Mouvement du joueur et logique du jeu

Vous disposez maintenant d'un labyrinthe que vous pouvez afficher et dont vous pouvez trouver la sortie. L'objectif de cette deuxième partie sera de réaliser le déplacement d'un personnage dans le labyrinthe ainsi que l'affichage d'un message lorsque la sortie est atteinte.

## Tâche 5 - Déplacement du joueur

La logique de jeu permettant d'afficher un message lorsque la sortie a été trouvée se trouve dans la classe `MazeGame`. L'idée est relativement simple : le joueur peut déplacer son personnage à l'aide des touches du clavier. Si un mouvement mène à la sortie (cela se produit dans la même classe), le joueur a gagné et une nouvelle partie commence.

1) Familiarisez-vous avec la classe `MazeGame`.
2. complétez la méthode `findPlayer(Player p)` qui renvoie les coordonnées d'un joueur sur le terrain. Les coordonnées sont renvoyées sous la forme d'un point. Si le joueur n'est pas en jeu, `null` est renvoyé, ce qui est une valeur spéciale qui signifie "rien"[^null].
3. complétez la méthode `movePlayer(direction d)` qui déplace le pion dans la direction indiquée. Notez que vous devez tenir compte correctement des murs. Pour déboguer cette méthode, utilisez-la directement dans `main` pour voir si tout se passe comme vous le souhaitez. Si vous pensez que votre méthode fonctionne, essayez de déplacer votre personnage dans différentes directions.
4) Essayez le code que vous avez écrit avec des labyrinthes qui ne sont pas carrés. Pourquoi ce point précis peut-il potentiellement poser problème ?

[^null] : Ce n'est pas la manière la plus élégante de le faire. En effet, que se passe-t-il si vous cherchez la position X du joueur 2 et qu'il n'est pas là ? Essayez si vous avez le temps. Cependant, compte tenu du temps disponible aujourd'hui, il s'agit d'une méthode raisonnable.

## Tâche 6 - Gestion du clavier

_Quelques mots sur la théorie - Inversion du flux de contrôle_

Java étant très fortement orienté objet, il est possible de séparer clairement les différentes étapes. Ainsi, la gestion des touches se fait dans la classe `KeyboardListener`. Dans cette classe, le flux de contrôle est inversé. Cela signifie que ce n'est pas vous qui décidez quand une méthode doit être appelée, mais la machine virtuelle (comme pour les `interruptions`). Dans une interface utilisateur graphique, par exemple, on ne sait jamais quand l'utilisateur va appuyer sur un bouton ou une touche. Au lieu d'attendre activement, ce type d'inversion de contrôle permet de réagir quand c'est nécessaire.

Concrètement, cela signifie que les méthodes sont appelées par la machine virtuelle Java lorsque l'utilisateur a appuyé sur une touche. Par exemple, si l'utilisateur appuie sur une touche puis la relâche, la méthode `keyPressed()` est appelée, ce qui permet de récupérer la touche enfoncée comme argument. Nous vous recommandons d'observer le squelette fourni dans la classe `KeyboardListener` pour obtenir plus d'informations.

1. observez la classe, en particulier comment il est possible de réagir à des touches spéciales du clavier comme les touches de fonction (`HOME`, `F1`-`F12`...).
2. notez qu'une instance du jeu et une instance du labyrinthe sont présentes dans la classe. Selon vous, à quoi servent-elles ?
3) Assurez-vous que vous pouvez déplacer le joueur à l'aide des boutons.
4) Faites en sorte qu'il soit possible d'afficher la solution. Pour cela, vous devez associer une touche à la méthode `displaySolution` mise à votre disposition.

```{note}
Le diagramme de classes suivant peut vous aider si vous n'êtes pas sûr des relations entre les classes :
```


```{figure} resources/maze-class-diagram-2.svg
---
width: 90%
name : Diagramme de classes Maze 2
---
Diagramme de classe Maze `MazeContainer`, `MazeGame`, `GraphicDisplay`, `KeyboardListener`.
```

## Tâche 7 - Sortir du labyrinthe

Maintenant que le clavier fonctionne correctement, il doit être possible d'afficher un message lorsque l'utilisateur a trouvé la sortie. C'est le but de la méthode `checkWinner` que vous devez implémenter. Pour afficher un message dans une nouvelle fenêtre, vous pouvez utiliser la technique suivante [^example] :

[^example] : Cet exemple se trouve en tant que commentaire à la fin de `MazeGame`, vous pouvez donc le copier directement.

```java
JOptionPane.showMessageDialog(null, "Titre de la fenêtre", "Texte de la fenêtre ! ", ,JOptionPane.INFORMATION_MESSAGE) ;
```

ce qui donne une fenêtre comme ci-dessous :

```{figure} resources/maze-popup.png
---
width: 30%
name : Maze Popup
---
Popup
```

```{figure} resources/maze-game.png
---
width: 70%
name : Maze Game Final
---
Jeu de maze final
```

```{important}
Nous vous souhaitons beaucoup de plaisir dans la réalisation de ce projet !
```

```{admonition} Solution
:class : dropdown
Si vous le souhaitez, vous pouvez télécharger une solution type ici.
[maze Masterversion](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook/content-de/java/maze/resources/mazegame_masterVersion.zip).
```
