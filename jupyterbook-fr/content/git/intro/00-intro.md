# Introduction

```{figure} resources/icons/git-logo.svg
---
width: 40%
name: Logo Git
---
```

```{figure} resources/git-graph.svg
---
width: 70%
name: Git graph
---
Git Graph inspiré de [Atlassian](https://www.atlassian.com/de/git/tutorials/making-a-pull-request)
```

## Qu'est-ce que le contrôle de version ?

Le contrôle de version consiste à enregistrer la fréquence à laquelle vous modifiez un fichier, les modifications que vous apportez et l'objectif de ces modifications. Il s'agit d'une forme de contrôle de version :

```text
$ ls

    mon_fichier_v0_0.md
    mon_fichier_v1_0.md
    mon_fichier_fini_v1_1.md
    mon_fichier_v1_0+Commentaires_du_superviseur.md
    mon_fichier_v1_0+commentaires_du_conseiller_v1_1_résumé.md
    mon_fichier_v1_2.md

$ diff mon_fichier_v1.md mon_fichier_v1_2.md

    ... (toutes les modifications apparaissent)
```

C'est génial parce que vous avez un enregistrement de toutes vos modifications, mais vous pouvez déjà voir qu'il y a des problèmes si vous faites plusieurs ensembles de modifications à la fois. Les systèmes logiciels de contrôle de version sont censés y remédier. Ils formalisent des pratiques courantes telles que le marquage des noms de fichiers (l'exemple ci-dessus) et ajoutent toute une série d'outils supplémentaires pour faciliter la collaboration.

L'autre forme de contrôle de version que vous avez peut-être déjà rencontrée est *Suivre les modifications* dans Microsoft Word ou le système de version *Time Machine* que vous pouvez trouver sur le Mac.

Ce type de contrôle de version basé sur les copies de sauvegarde est bon, mais il est très linéaire dans la manière dont les modifications sont gérées. Comme vous pouvez le voir ci-dessus, il peut y avoir de réels problèmes lorsque deux personnes travaillent sur un même fichier. Pendant que vous attendez que votre directeur de thèse commente le projet de la version 1.0 de votre thèse, vous voulez certainement commencer à travailler sur la version 1.1. Si votre directeur de thèse vous suggère d'apporter des modifications à la version 1.0, vous devez d'abord déterminer quelles modifications vous devez apporter à la version 1.1 pour créer une nouvelle version avant de pouvoir commencer la version 1.2.

Imaginez à quel point cela devient plus compliqué lorsque de nombreuses personnes travaillent sur un projet et qu'elles éditent peut-être toutes ensemble un seul fichier.

### Wiso Contrôle de version

Le contrôle de version a de nombreuses fonctions utiles, **chaque** développeur devrait maîtriser au moins un outil pour :

* annuler les erreurs (revenir aux versions précédentes)
* développer et tester de nouvelles fonctionnalités de manière indépendante
* Exécuter et tester avec des versions plus anciennes
* conserver et passer d'une version à l'autre du code
* Travail d'équipe : fusion automatique des traitements effectués par différentes personnes.
* Distribuer et publier des analyses, du code et des flux de travail.
* Archiver ou sauvegarder votre travail afin qu'il ne soit pas perdu si votre ordinateur ne fonctionne plus.

## Les outils existent-ils ?

Il existe un certain nombre de paquets différents que vous pouvez utiliser, et ils ont tous leurs avantages et leurs inconvénients. Voici quelques exemples que vous pourriez rencontrer :

   - git : (`git`)
   - Subversion : (`svn`)
   - mercurial : (`hg`)

Ils sont tous à peu près équivalents et diffèrent légèrement dans la manière dont ils distribuent le référentiel (la base de données contenant toute l'histoire du projet). `git` dépose l'historique complet de tous les fichiers sur chaque ordinateur, ce qui assure une sécurité supplémentaire. Dans ce cours, nous ne travaillerons qu'avec git, car il est devenu la norme de facto dans l'industrie au cours des dernières années.

## Qu'est-ce que `git` ?

`git` est un système de gestion de versions *distribué* et *non linéaire* qui est fortement axé sur le travail d'équipe. Il a été développé par [Linux Torvald] (https://en.wikipedia.org/wiki/Linus_Torvalds) et publié pour la première fois en 2005. Le code source est ouvert (open source) et est devenu l'outil de gestion de versions le plus populaire en 2013.
Vous pouvez utiliser le logiciel vous-même sur votre propre ordinateur pour gérer le contrôle de version d'un projet. Toutefois, les véritables avantages d'un outil comme `git` apparaissent lorsque vous utilisez un **référentiel** en réseau de vos documents, auquel vous pouvez accéder depuis plusieurs ordinateurs et que vous pouvez synchroniser d'un ordinateur à l'autre lorsque vous êtes prêt. Vous n'êtes pas le seul à pouvoir le faire, vos collaborateurs peuvent également accéder aux fichiers et les modifier, et vous pouvez ensuite fusionner les modifications de manière organisée.

## Qu'est-ce que github, gitlab et bitbucket ?

Github, Gitlab et Bitbucket sont trois plates-formes cloud qui mettent à disposition des serveurs de dépôts Git gratuits et payants.
Nous avons un espace commun sur `github` et nous utiliserons ensemble les dépôts gérés dans le cadre de ce cours. Github offre également une variété d'outils de gestion de projet qui peuvent être très utiles pour les équipes ou les classes. On peut citer par exemple le contrôle d'accès, le suivi des bugs, les demandes de fonctionnalités, la gestion de projet.

````{list-table}

   * - ```{figure} resources/icons/bitbucket-icon.svg
       ---
       width: 100%
       name: Logo Bitbucket
       ---
       Logo de Bitbucket

     - ```{figure} resources/icons/github-logo.svg
       ---
       width: 100%
       name: Logo Github
       ---
       Logo de Github
       ```

     - ```{figure} resources/icons/gitlab-logo.svg
       ---
       width: 100%
       name: Logo Gitlab
       ---
       Logo de Gitlab
       ```
````
### Comment fonctionne `git` ?

#### Commits

Un dépôt `git` contient l'histoire complète d'un projet. Chaque point de l'histoire est un **commit**.

```{figure} resources/gitgraph-history.png
---
width: 80%
name: historique git
---
exemple d'historique de git
```

#### Branches

L'histoire du dépôt ne peut pas être linéaire, car il y a différentes branches appelées **branches**.

```{figure} resources/gitgraph-history-nonlinear.png
---
width: 80%
name: git history non linear
---
git non linear history exemple
```

#### Distribué

Le dépôt n'existe pas dans un endroit central mais est distribué, chaque personne qui travaille avec lui possède sa copie et son historique. Ces dépôts distribués sont synchronisés vers un dépôt central (appelé **origin** dans l'image).

```{figure} resources/gitflow-centralize-decentralize.png
---
width: 60%
name: distributed git
---
Source distribuée : [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

## Opérations

Pour effectuer des changements sur le dépôt local (**local**) ou distant (**remote**), différentes actions sont nécessaires.

**working directory** contient les fichiers qui se trouvent actuellement dans le dossier, ces fichiers sont en principe non suivis (**untracked**), sauf si une version a déjà été **commandée** dans le dépôt.
**staging area** contient les fichiers et les changements qui sont prévus pour être inclus dans le dépôt (**tracked**).
* Le dépôt local git contient les fichiers sauvegardés et leurs modifications (**committed**).
* Le

```{figure} resources/git-stages.svg
---
width : 100%
name: git stages
---
opérations de git
```

### Outils pour `git`.

Par défaut, git est utilisé en ligne de commande, mais il existe aussi diverses interfaces graphiques qui facilitent le travail avec `git`. Mais si l'on veut savoir exactement ce qui se passe, la ligne de commande est le meilleur outil.

````{list-table}
   * - ```{figure} resources/icons/git-logo.svg
       ---
       width: 50%
       name: Ligne de commande Git
       ---
       [Ligne de commande Git](https://git-scm.com)
       ```
     - ```{figure} resources/icons/sublimemerge-icon.svg
       ---
       width: 50%
       name: Sublime Merge
       ---
       [Sublime Merge](https://www.sublimemerge.com)
       ```
     - ```{figure} resources/icons/fork-icon.webp
       ---
       width: 50%
       name: Fork
       ---
        [Fork](https://git-fork.com)
       ```
   * - ```{figure} resources/icons/tower-icon.svg
       ---
       width: 50%
       name: Tour
       ---
       [Tour](https://www.git-tower.com/mac)
       ```
     - ```{figure} resources/icons/git-cola-icon.svg
       ---
       width: 50%
       name: git cola
       ---
       [Git Cola](https://git-cola.github.io)
       ```
     - ```{figure} resources/icons/gitkraken-icon.svg
       ---
       width: 50%
       name: gitkraken
       ---
       [Git Kraken](https://www.gitkraken.com)
       ```
````
