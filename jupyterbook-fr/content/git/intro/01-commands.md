# Commandes

Une liste des commandes les plus utilisées peut être consultée [ici](https://training.github.com/downloads/de/github-git-cheat-sheet/).

Un guide interactif étape par étape des différentes commandes `git` est disponible [ici](https://gitflow.smessina.com/#/).


## Vérifier les changements et faire un `commit`.

```bash
git status
```
Répertorie tous les fichiers nouveaux ou modifiés prêts à être validés.

```bash
git diff
```

Affiche les modifications de fichiers qui n'ont pas encore été indexées.

```bash
git add [file]
```

Indique l'état actuel du fichier pour le versionnage.

```bash
git diff --staged
```

Affiche les différences entre l'index ("staging area") et la version actuelle du fichier.

```bash
git reset [file]
```

Enlève le fichier de l'index, mais conserve son contenu.

```bash
git commit -m "[descriptive message]"
```

Inclut en permanence tous les fichiers actuellement indexés dans l'historique des versions.

## Synchroniser les modifications

Enregistre un référentiel externe (URL) et échange l'historique du référentiel.

```bash
git fetch [remote]
```

Télécharge l'historique complet d'un référentiel externe.

```bash
git merge [remote]/[branch]
```

Intègre la branche externe dans la branche actuellement extraite localement.

```bash
git push [remote] [branch]
```

Pousse tous les commits de la branche locale vers GitHub.

```bash
git pull
```

Extrait l'historique du référentiel externe et intègre les modifications.

## Commandes Git les plus utilisées

| commande | description |
|:----------:|--------------|
| **Démarrer un espace de travail** |
| `clone` | Cloner un dépôt dans un nouveau répertoire |
| `init` | Créer un référentiel Git vide ou réinitialiser un référentiel existant |
| **Travailler sur la modification en cours** ||
| `add` | Ajouter le contenu des fichiers à l'index |
| `mv` | déplacer ou renommer un fichier, un répertoire ou un lien symbolique |
| `reset` | Réinitialiser le HEAD actuel à l'état spécifié |
| `rm` | supprimer des fichiers de l'arborescence de travail et de l'index |
| **Examiner l'historique et l'état** |
| `log` | Afficher les journaux de transfert |
| `show` | Afficher différents types d'objets |
| `status` | Afficher l'état de l'arbre de travail |
| **Croître, marquer et optimiser votre histoire commune** ||
| `branch` | Lister, créer ou supprimer des branches |
| `checkout` | changer de branche ou restaurer les fichiers de l'arbre de travail |
| `commit` | Enregistrer les modifications apportées à l'archive du projet |
| `diff` | afficher les changements entre les commits, les commits et l'arbre de travail, etc. |
| `merge` | Fusionner deux ou plusieurs historiques de développement |
| `rebase` | Recréer des commits sur une autre branche |
| `tag` | Créer, lister, supprimer ou vérifier un objet tag signé GPG |
| **Collaborer** |
| `fetch` | Télécharger des objets et des références depuis un autre référentiel |
| `pull` | récupération d'un autre référentiel ou d'une branche locale et intégration dans celui-ci |
| `push` | Mettre à jour les références distantes ainsi que les objets associés |

**Version anglaise**

| Command    | Description |
|:----------:|--------------|
| **Start a working area** ||
| `clone`    | Clone a repository into a new directory |
| `init`     | Create an empty Git repository or reinitialize an existing one |
| **Work on the current change**||
| `add`      | Add file contents to the index |
| `mv`       | Move or rename a file, a directory, or a symlink |
| `reset`    | Reset current HEAD to the specified state |
| `rm`       | Remove files from the working tree and from the index |
| **Examine the history and state**||
| `log`      | Show commit logs |
| `show`     | Show various types of objects |
| `status`   | Show the working tree status |
| **Grow, mark and tweak your common history**||
| `branch`   | List, create, or delete branches |
| `checkout` | Switch branches or restore working tree files |
| `commit`   | Record changes to the repository |
| `diff`     | Show changes between commits, commit and working tree, etc |
| `merge`    | Join two or more development histories together |
| `rebase`   | Reapply commits on top of another base tip |
| `tag`      | Create, list, delete or verify a tag object signed with GPG |
| **Collaborate**||
| `fetch`    | Download objects and refs from another repository |
| `pull`     | Fetch from and integrate with another repository or a local branch |
| `push`     | Update remote refs along with associated objects |
