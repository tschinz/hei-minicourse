# Configuration

La première étape est l'installation de Git. Tu peux télécharger la dernière version sur le site officiel https://git-scm.com/. Git est disponible pour Linux, Mac et Windows. Pour ce laboratoire, git ≥ 2.27 est nécessaire.

## Ligne de commande

Lancez "Git Bash". Il s'agit d'un éditeur de commandes de type Unix/Linux qui permet d'exécuter des commandes Git en mode console. C'est l'interface que nous utiliserons dans ce laboratoire.

```{figure} resources/git-terminal.png
---
width: 80%
name: Terminal Git
---
terminal git
```

```{important}
Notez que pour toutes les commandes dans Git Bash, vous pouvez obtenir de l'aide en insérant `--help` après la commande.
```

## Configuration globale

Un grand nombre de paramètres peuvent être configurés dans Git. Il est possible de modifier les réglages globalement sur votre ordinateur (indicateur `--global`) ou seulement pour un dépôt particulier. Vous allez effectuer la configuration minimale.
Configurez maintenant votre identité. Utilise les commandes suivantes pour configurer ton identité dans Git globalement sur le système. Utilise ton nom et ton adresse électronique. Ces informations sont visibles publiquement pour identifier ton travail (tes commits).

```bash
git config --global user.name "premier nom nom de charge".
git config --global user.email first.last@email.ch
```

Vous pouvez vérifier la configuration avec la commande suivante :

```bash
git config --list
```

Vous pouvez également vérifier une configuration spécifique :

```bash
git config user.name
 ```