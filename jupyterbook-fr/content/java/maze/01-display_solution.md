# Partie 1 - Afficher et sortir du labyrinthe

Dans cette première partie, vous allez découvrir le code source que nous avons préparé pour vous, ainsi que la structure du code Java. A la fin de cette partie, vous disposerez des outils nécessaires pour afficher un labyrinthe sous forme de texte et d'image. Vous serez également en mesure de représenter le chemin d'un point quelconque vers la sortie sur l'image.

## Tâche 0 - Importer le projet

Nous avons préparé pour vous un projet Eclipse qui contient les éléments de base du projet. Pour l'importer, suivez les étapes suivantes :
1. démarrez Eclipse et exécutez ensuite _File->Import->General-> Projects from Folder or Archive_.
2. cliquez sur l'option _Archive_, sélectionnez le fichier
[maze version étudiante](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook-de/content/java/maze/resources/mazegame_studentVersion.zip) depuis la clé USB et cliquez sur _Finish_. Le projet Maze existe maintenant dans votre liste de projets.

````{important}
Vous pouvez télécharger le zip ici :

[maze version étudiante](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook-de/content/java/maze/resources/mazegame_studentVersion.zip)
````



## Tâche 1 - Dessiner le labyrinthe sous forme de texte

Cette première tâche vous montrera comment le labyrinthe est codé dans le projet, en vous demandant de l'afficher sous forme de texte dans la console. Cela vous sera utile tout au long de la journée, car nous utiliserons toujours la même structure de données.

1. ouvrez le fichier `TextDisplay.java`, qui se trouve dans `maze/display`, et observez le fichier.
2. remarquez qu'il y a un `main` dans le fichier. Comme en C/C++, `main` représente un point d'entrée dans le programme.
3. dans le `main`, on crée un `MazeContainer`. Cette classe crée le labyrinthe et vous permet d'y accéder sous la forme d'un tableau bidimensionnel de `MazeElem`. Dans la classe se trouvent également les informations sur les dimensions du labyrinthe (champs `nCellsX` et `nCellsY`).
4. ouvrez la classe `MazeElem` et analysez-la. Cette dernière classe contient déjà toutes les informations sur ce qui se trouve dans une case du labyrinthe (murs, joueurs, sortie ...).
5. le diagramme de classes UML, c'est-à-dire la manière dont les classes sont organisées, se présente comme suit :

   ```{figure} resources/maze-class-diagram-1.svg
   ---
   width: 70%
   name: Diagramme de classes Maze 1
   ---
   Diagramme de classe Maze `MazeContainer` et `MazeElem`.
   ```

6. lancez le programme correspondant (clic droit sur la classe `TextDisplay` => `Run As` => `Java Application`).
7. modifiez le programme de manière à ce qu'il affiche un labyrinthe de 5x5.
8 Comme vous pouvez le constater, le labyrinthe n'est pas affiché en entier, mais seulement les intersections et les murs tout en bas et tout à droite. Complétez le code aux endroits indiqués par `TODO tâche 1` pour que le labyrinthe s'affiche correctement comme ci-dessous (`p1` représente la position du premier joueur et `e` la sortie). Leur affichage doit être le suivant :

```Texte
*---*---*---*---*---*
| p1|               |
*   *   *---*---*   *
|   |   |       |   |
*   *---*   *   *   *
|           |       |
*---*---*---*---*   *
|       |           |
*   *---*   *---*---*
|         e         |
*---*---*---*---*---*
```


## Tâche 2 - Dessiner le labyrinthe en tant qu'image

Maintenant que nous sommes en mesure d'afficher correctement un labyrinthe sous forme de texte, il est temps d'ajouter un peu de graphisme à notre programme. Vous trouverez une classe qui fonctionne de manière similaire à `TextDisplay` dans le fichier `GraphicDisplay.java`.

1. ouvrez le fichier `GraphicDisplay.java`.
2. observez la méthode `main` de cette classe et exécutez-la.
3. modifiez le code de manière à afficher un labyrinthe 10x10.
4. vous pouvez modifier la taille de chaque petit carré en changeant un paramètre dans le constructeur de `GraphicDisplay`. Essayez avec d'autres valeurs plus grandes ou plus petites.
5. il est possible d'afficher le labyrinthe sans les bords de la fenêtre. Trouvez comment faire et exécutez votre programme. Vous obtiendrez quelque chose de similaire à ce que vous voyez à droite dans l'illustration ci-contre. Vous pouvez décider d'utiliser plutôt cette méthode ou l'autre, selon ce que vous préférez. Essayez également de rendre la grille d'arrière-plan visible (vous pouvez modifier une variable à cet effet).

   ```{figure} resources/maze-mini.png
   ---
   width: 10%
   name: Mini Maze
   ---
   Mini Maze
   ```

6. pour s'assurer que l'affichage est correct, afficher aussi une version texte du même labyrinthe à partir du `main`.

## Tâche 3 - L'algorithme de propagation de Lee

Dans cette phase, vous allez implémenter un moyen de trouver automatiquement la sortie du labyrinthe à l'aide d'un algorithme de routage.

1. ouvrez la classe `AStar.java` qui contient le squelette de la classe de solveur pour le labyrinthe selon la méthode de Lee qui a été présentée. La phase de propagation de l'algorithme (lorsque le chemin croît dans toutes les directions à partir du point de départ) peut être formellement décrite comme suit :

   ```text
   Algorithme 1 - Propagation de Lee (algorithme A*)
   Marquez le point de départ avec 1
   m <= 1
   // Propagation ondulatoire
   répéter
     Marque toutes les cellules voisines non marquées à partir des points marqués m avec m+1
     m <= m+1
   jusqu'à la cible trouvée ou il n'y a pas d'autres points à marquer.
   ```
2. pour tester votre méthode, un `main` a également été créé ici. Vous pouvez l'utiliser pour déboguer plus facilement votre code.
3. observez la méthode `solve`. Elle commence par créer une solution vide (qui est en fait un tableau d'entiers). Elle continue en effectuant la propagation de Lee, puis le backtracking. Le but de tout l'algorithme est de mettre un `1` partout où la solution se trouve entre le point donné en argument et la sortie. Par exemple, le labyrinthe :

   ```text
   *---*---*---*---*
   | p1|           |
   *   *   *---*   *
   |   |   |       |                          1 - 0 - 0 - 0
   *   *---*   *   *     donnera au final     1 - 0 - 1 - 1
   |           |   |                          1 - 1 - 1 - 1
   *---*---*---*   *                          0 - 1 - 1 - 1
   |     e         |
   *---*---*---*---*
   ```

4. si nous supprimons le backtracking (en commentant la méthode `backtrace()` dans `solve`), nous pouvons voir les étapes de la propagation, ce qui est très pratique pour déboguer le code. Dans le cas ci-dessus, cela ressemble à ceci :

   ```text
   01 - 10 - 09 - 08
   02 - 11 - 06 - 07
   03 - 04 - 05 - 08
   00 - 11 - 10 - 09
   ```

5. pour obtenir ce résultat, il faut implémenter la méthode `expansion`. Celle-ci est appelée par `solve` tant qu'elle ne renvoie pas `true` (c'est-à-dire tant que la propagation de la vague n'a pas encore atteint la cible). Notez également qu'à chaque appel, la méthode reçoit le statut de `m`, qui est le numéro de l'étape en cours. C'est à vous de trouver comment vous y prendre (avec notre aide) ! N'hésitez pas à utiliser la méthode `access_solution()` (en comprenant à quoi elle sert...).

## Tâche 4 - Affichage de la solution dans la fenêtre graphique

Votre implémentation du point précédent vous fournit un tableau contenant une solution à partir d'un point donné. Vous avez la possibilité de l'afficher directement dans la représentation graphique du labyrinthe. C'est ce que vous allez mettre en œuvre dans cette tâche.
1. inspirez-vous de la procédure précédente et affichez la version graphique du labyrinthe à partir de la classe `main` `AStar`.
2. l'objet de la classe `GraphicDisplay` que vous avez créé dispose d'une méthode `setSolution()` qui prend comme argument un tableau d'entiers correspondant à une solution à partir d'un point. Utilisez cette méthode pour afficher la solution calculée par l'algorithme de Lee créé à l'étape précédente. Si vous souhaitez supprimer la solution de l'affichage, utilisez la méthode `clearSolution()`.

## Tâches optionnelles

1. changer la façon dont le joueur est dessiné (autre forme comme une flèche indiquant le dernier coup, couleurs, ...).
2. afficher un autre dessin pour la sortie (par exemple une flèche qui pointe vers l'extérieur).