# Branch et Merge

Jusqu'à présent, nous avons utilisé les fonctions de base de git. Il y a aussi les fonctions `branch` (branche) et `merge` (fusion) que Git a fortement simplifiées par rapport aux outils qui existaient auparavant.

Pour ce travail pratique, vous pouvez vous aider de la commande `gitk`, qui vous fournit une représentation graphique et un historique visuel des commits dans votre repo.

1. créez une branche de développement `dev01` dans votre repo local.
2. créez deux commits sur cette branche :
   * Un pour créer un fichier `hello_world.py`.
   * Un pour remplir ce fichier `hello_world.py`.
3. à partir de la branche `master`, créez une nouvelle branche de développement `dev02`.
4. créer un commit sur la branche `dev02` :
   * Modifier le fichier `README.md`.
5. fusionnez la branche `dev02` en `master`.
6. fusionnez la branche `dev01` en `master`.
7. poussez votre dépôt local sur votre GitHub distant.
