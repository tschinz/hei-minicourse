# Opérations de base

## Créer un référentiel git

A l'aide de la console Git Bash, créez un répertoire vide sur votre ordinateur, par exemple `C:\temp\gitRepo`. Ce répertoire sera votre référentiel Git.

Vous pouvez utiliser les commandes Unix/Linux `ls` `cd` `pwd` et `mkdir` pour créer ce répertoire.

```bash
mkdir -p c:\temp\gitRepo
cd c:\temp\gitRepo
```

## Initialiser

Une fois que vous êtes dans ce répertoire, initialisez-le en tant que Git Repo avec la commande :

```bash
git init
```

Qu'est-ce qui a changé dans le répertoire après que tu l'aies initialisé comme Git Repo ?

```{note}
Écrivez la réponse !
```

## Demander le statut

Obtenez des informations sur votre repo en utilisant les commandes suivantes :

```bash
git status
git log --oneline
```

## Ajouter un fichier

Créez maintenant un fichier vide avec le nom `README.md` dans le répertoire principal de votre repos.
Utilisez la commande précédente pour récupérer à nouveau les informations sur votre repo. Qu'est-ce qui a changé ?

```{note}
Écrivez la réponse !
```

Votre Repo Git local se compose de trois zones gérées par `git` :
* Le `Working directory` est un répertoire qui contient la version actuelle de tes fichiers (aux yeux de ton système d'exploitation, c'est un répertoire de fichiers normal) ;
* `Stage` contient les modifications qui doivent être incluses dans le prochain commit ;
* Le `Head` indique l'endroit dans l'arborescence Git Repo où le prochain commit doit être effectué.

```{figure} resources/git-stages-local.svg
---
width: 60%
name: git stages local
---
Types d'opérations Git locales
```

Un simple repo Git, composé de cinq commits, peut être représenté de la manière suivante. La position `Head` est une référence à un commit qui représente l'état/la vue actuelle du repos, ici la dernière modification.

```{figure} resources/gitgraph-history.png
---
width: 80%
name: git local repo 1
---
Cinq commits sur le repo local, chaque `commit` possède son propre identifiant
```

## Ajouter le fichier au repo
Ajouter le fichier `README.md` créé précédemment au stage, avec la commande :

```bash
git add README.md
```

Récupérez à nouveau les informations sur votre repo, que constatez-vous ?

```{note}
Notez la réponse !
```

Modifiez le fichier `README.md` avec un éditeur de texte et insérez le texte suivant (syntaxe Markdown) :

````markdown
# Titre de mon readme
Texte et encore du texte, suivi d'une petite liste :
  * Item 1
  * Item 2
  * Item 3
Et enfin un peu de code :
```sh
$ cd myDir
$ git init
$ git status
$ ls -al
```
````

Obtenez à nouveau les informations sur votre repo, que constatez-vous ?

```{note}
Écrivez la réponse !
```

## Ajouter de nouvelles modifications
Ajoutez la dernière version du fichier `README.md` au stage.

``bash
git add README.md
```

## Exécuter le commit

Exécutez maintenant un commit avec la commande suivante :

```bash
git commit -m "Initial commit. Ajouter un fichier README".
```

```{important}
L'option `-m` permet d'indiquer directement le message du commit.
Ce message doit être auto-explicatif. Il correspond à la description des modifications. Il est possible d'insérer un bloc de texte, par exemple via un éditeur de texte, sans utiliser l'option "-m".
```

## Plus d'informations
Quelles informations obtiendrez-vous maintenant avec la commande

```bash
git log -oneline
```

Expliquez clairement toutes les informations de cette ligne.

```{note}
Écrivez la réponse !
```

## Plus de commits
Vos modifications sont maintenant publiées dans votre dépôt Git local. Bravo !

Effectuez un autre commit pour ajouter un nouveau fichier (vide) `hello_world.py` dans votre repo.

Quelles nouvelles informations vous fournit maintenant la commande

```bash
git log
```

```{note}
Écrivez la réponse !
```

Notez que chaque commit est accompagné d'un "hash" ou d'une "somme de contrôle" (de type sha1). Celle-ci est créée avec la commande :

```bash
git log --oneline
```

affichés ne sont que les premiers caractères de ces fameux "_short hashes_".

## Checkout commit
Effectuez maintenant un checkout avec la commande suivante, en utilisant le "short hash" qui correspond à votre **premier** commit.

```bash
git checkout <SHA1> -b inspectingPrev
```


Que constatez-vous maintenant lorsque vous consultez le contenu du Working Directory ?

```{note}
Écrivez la réponse !
```

## Checkout `master`
Effectuez maintenant un checkout avec la commande suivante :

```
git checkout master
```

Que constatez-vous maintenant lorsque vous regardez le contenu du working directory ?

```{note}
Écrivez la réponse !
```