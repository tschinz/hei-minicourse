# Branch et Merge

Jusqu'à présent, nous avons utilisé les fonctions de base de git. Il existe aussi les fonctions `branch` (branche) et `merge`(fusion), que Git a fortement simplifiées par rapport aux outils existants auparavant.

Par défaut, il existe toujours une branche "master" ou "main" dans git :

```{figure} resources/git-local-repo-1.png
---
width: 30%
name: git local 1
---
Référentiel avec `master` `branch`
```

Git va nous permettre de créer facilement une nouvelle branche :

```bash
git branch dev_branch_1
```

```{figure} resources/git-local-repo-2.png
---
width: 30%
name: git local 2
---
Repository avec `master` et `dev_branch_1` `branch`
```

Git va aussi nous permettre de lister simplement les branches existantes sous forme de liste. Un astérisque (*) devant le nom de la branche indique sur quelle branche tu te trouves actuellement.

```bash
git branche
```

Pour développer sur la branche de développement que nous venons de créer, nous pouvons extraire cette branche (modifier HEAD) :

```bash
git checkout dev_branch_1
```

```{figure} resources/git-local-repo-3.png
---
width: 30%
name: git local 3
---
Référentiel avec `dev_branch_1` sélectionné `branch`
```

Chaque commit sur cette branche peut donc être représenté comme suit :

```{figure} resources/git-local-repo-4.png
---
width: 30%
name: git local 4
---
Référentiel d'un `dev_branch_1` commit
```

Puis le commit suivant :

```{figure} resources/git-local-repo-5.png
---
width: 30%
name: git local 5
---
Référentiel d'un autre `dev_branch_1` commit
```

Git permet également de fusionner facilement cette branche de développement :

```bash
git checkout master
git merge dev_branch_1
```

Notez que lors de l'opération de fusion, on travaille sur la branche dans laquelle on veut fusionner et on fusionne une autre branche dans la branche sur laquelle on travaille.

Dans le cas simple ci-dessus, où aucun autre commit n'a été fait sur la branche `master`, Git sera capable d'effectuer une fusion `fast-forward` et de simplement déplacer le pointeur sur la branche `master`.


```{figure} resources/git-local-repo-6.png
---
width: 30%
name: git local 6
---
Référentiel avec `dev_branch_1` fusionné avec `master` `branch
```

Au cas où d'autres commits auraient été effectués entre temps sur la branche `master` :

```{figure} resources/git-local-repo-7.png
---
width: 30%
name: git local 7
---
Référentiel avec `master` `branch`
```

Git va automatiquement créer un nouveau commit de fusion et faire une `three way merge` :

```{figure} resources/git-local-repo-8.png
---
width: 30%
name: git local 8
---
Référentiel avec `dev_branch_1` fusionné avec `master` modifié `branch`
```

Git va aussi nous permettre de supprimer des branches dont on n'a pas besoin :

```bash
git branch -d dev_branch_1
```

```{figure} resources/git-local-repo-9.png
---
width: 30%
name: git local 9
---
Référentiel avec `three way merge``
```

Notez qu'aucun des commits n'est supprimé, seules les informations de branche sont supprimées.
