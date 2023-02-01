# GitHub

```{figure} resources/icons/github-icon.svg
---
width: 30%
name: GitHub icon 2
---
GitHub Icon
```

Wir werden nun eine Kopie des Repos auf [GitHub](https://github.com) erstellen. Erstellen Sie zunächst ein Konto auf der Plattform GitHub.com, falls Sie noch keines haben.

```{figure} resources/github-signup.png
---
width: 80%
name: GitHub signup
---
Erstellen eines GitHub Accounts
```

```{important}
**Optional** Um die Sicherheit Ihrer Kommunikation zwischen git auf Ihrem Rechner und der Github-Plattform zu gewährleisten können sie `SSH` Schlüssel benutzten:
* [Erzeugen Sie einen SSH-Schlüssel auf Ihrem Rechner](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
* [Füge diesen Schlüssel dann zu deinem GitHub-Konto hinzu](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
* [Schliesslich können Sie die SSH-Verbindung testen](https://help.github.com/articles/testing-your-ssh-connection/)
```

## Erstellen eines GitHub Repository
Erstellen Sie ein neues privates Repo direkt über das GitHub-Webinterface.

```{figure} resources/github-repo.png
---
width: 80%
name: Github new repo
---
Erstellen eines git repos
```

Initialisieren Sie das Repo weder mit einem `README`, einer `.gitignore`-Datei oder einer `Lizenz`, damit ist sicher das Ihr Repo komplett leer ist.

Führen Sie vom Git Bash Editor aus den folgenden Befehl aus, um das GitHub Repo als neues Remote Repo (namens `origin) hinzuzufügen, das mit dem lokalen Repo auf Ihrem Maschine verknüpft ist.

```bash
git remote add origin git@github.com:<username>/<reponame>.git
```

Führen Sie im Git Bash-Editor den folgenden Befehl aus, um eine vollständige Kopie Ihres Repos in das auf GitHub enthaltene Repo zu pushen:

```bash
git push origin master
```

Was können sie im GitHub Webinterface beobachten?

```{note}
Schreiben Sie die Antwort auf!
```