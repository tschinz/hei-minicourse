# GitHub

```{figure} resources/icons/github-icon.svg
---
width: 30%
name: icône GitHub 2
---
Icône GitHub
```

Nous allons maintenant créer une copie du dépôt sur [GitHub](https://github.com). Créez d'abord un compte sur la plateforme GitHub.com si vous n'en avez pas encore.

```{figure} resources/github-signup.png
---
width: 80%
name: GitHub signup
---
Création d'un compte GitHub
```

```{important}
**Optionnel** Pour assurer la sécurité de vos communications entre git sur votre machine et la plateforme Github, vous pouvez utiliser des clés `SSH` :
* [Créez une clé SSH sur votre ordinateur](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
* [Ajoutez ensuite cette clé à votre compte GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
* [Enfin, vous pouvez tester la connexion SSH](https://help.github.com/articles/testing-your-ssh-connection/)
```

## Créer un référentiel GitHub
Créez un nouveau dépôt privé directement via l'interface web GitHub.

```{figure} resources/github-repo.png
---
width: 80%
name: Github nouveau repo
---
Créer un repos git
```

N'initialisez pas le repo avec un `README`, un fichier `.gitignore` ou une `licence`, vous êtes ainsi sûr que votre repo est complètement vide.

Exécutez la commande suivante à partir de l'éditeur Git Bash pour ajouter le repo GitHub en tant que nouveau repo distant (nommé `origin) qui est lié au repo local sur votre machine.

```bash
git remote add origin git@github.com:<username>/<reponame>.git
```

Dans l'éditeur Git Bash, exécutez la commande suivante pour pousser une copie complète de votre dépôt dans le dépôt contenu sur GitHub :

```bash
git push origin master
```

Que peuvent-ils observer dans l'interface web GitHub ?

```{note}
Écrivez la réponse !
```