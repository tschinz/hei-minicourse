# Gitflow

Git encourage donc fortement la création de branches, tout en laissant aux développeurs une liberté totale dans leur utilisation. C'est donc un outil puissant qui peut devenir contre-productif s'il est mal utilisé. Les équipes de développement décident donc typiquement d'un plan de développement ("workflow") avec Git, qui définit leurs directives pour la création de branches et de fusions.

Cette section décrit Git-flow ([A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)), un workflow composé d'un ensemble de règles utilisant le modèle de branche de Git. En voici les principes de base :

La configuration du dépôt de l'équipe de développement conserve un dépôt central (par exemple chez un hébergeur web de serveurs Git comme "GitHub" "Bitbucket" ou "Gitlab"). Nous appelons ce repo central `origin`. Notez que ce repo n'est centralisé que de manière arbitraire, car Git est un système de gestion des sources décentralisé et peut se passer d'un seul repo central.

```{figure} resources/gitflow-centralize-decentralize.png
---
width: 60%
name: distributed git 2
---
Référentiel Git distribué Source : [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

Chaque projet sera basé sur deux branches principales : `master` et `develop. Ces deux branches sont strictement interdites d'écriture pour les développeurs.

```{figure} resources/gitflow-main-branches.png
---
width: 40%
name: branche principale de git
---
Git Afficher `master` et `develop` Source : [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

La branche principale est le miroir de notre production (le produit livré aux utilisateurs). Il est donc logique que nous ne puissions pas y pousser directement nos modifications. La branche `origin/master` est donc considérée comme la branche principale du code source, dans laquelle le `HEAD` se trouve toujours dans un état prêt pour le client.

Dans la branche `origin/develop` sont centralisées toutes les nouvelles fonctions qui seront incluses dans la prochaine version (parfois aussi appelée intégration). Dans cette branche, il n'est pas non plus possible de faire des modifications directement. Le `HEAD` de `origin/develop` indique donc l'état des derniers développements terminés. Il s'agit typiquement de la branche sur laquelle des tests automatisés sont effectués chaque nuit. Dès que la branche `develop` est considérée comme stable, elle est mergée dans `master` pour créer une version stable (un livrable) de notre logiciel.

Trois autres types de branches nous permettront ensuite de travailler en équipe et en parallèle. Contrairement aux branches dont nous avons parlé précédemment, celles-ci ont une durée de vie éphémère.

* `feature`.
* `release` (version)
* `hotfix`.

Ces trois types de branches ont un but bien précis :

Les branches de type `feature` sont utilisées pour implémenter de nouvelles fonctions. Elles sont donc formées à partir de la branche `develop`. (par exemple `feature/new-button-on-front-screen`). Elles permettent d'isoler chaque nouvelle fonction et facilitent le travail en parallèle.
Dès qu'une fonctionnalité est acceptée comme "done" (terminée) par l'équipe, elle est intégrée dans la branche `develop`, comme le montre l'illustration suivante :

```{figure} resources/gitflow-merge-without-ff.png
---
width: 60%
name: branche git feature
---
Git Afficher `feature` et `develop Source : [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

Les branches de release sont utilisées pour préparer la sortie d'une nouvelle version. Elles sont créées à partir de `develop` (par exemple `release/january-general-update`). Ils permettent à d'autres développeurs de continuer à alimenter la branche `develop` parallèlement à la préparation de la nouvelle version. Une fois que tous les tests ont été passés avec succès et que la release est considérée comme "done", elle est fusionnée dans `master`. Si des corrections ont été apportées à la branche `release`, elles sont également fusionnées dans la branche `develop`.

Les branches de type `hotfix` sont utilisées pour corriger les erreurs en production. Nous allons donc créer ce type de branche directement à partir du master, car nous ne voulons pas inclure toutes les fonctions disponibles dans `develop` (par exemple `hotfix/crash-when-button2-pressed`). Typiquement, une erreur qui se produit dans un produit en production doit d'abord être reproduite par un test automatique (pour s'assurer qu'elle ne se reproduira pas à l'avenir), puis elle est corrigée sur la branche `hotfix`. Enfin, la branche `hotfix` est mélangée à la fois à la branche `master` et à la branche `develop`.

```{figure} resources/gitflow-hotfix-branches.png
---
width: 30%
name: modèle de hotfix git
---
Git hotfix merging Source : [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

Un exemple complet d'un projet Gitflow peut être observé dans l'illustration ci-dessous.

```{figure} resources/gitflow-model.png
---
width: 60%
name: modèle git flow
---
GitFlow M complet
