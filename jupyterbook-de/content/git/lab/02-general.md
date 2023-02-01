# Basis Operationen

## Erstellen eines git Repositories

Erstellen Sie mithilfe der Git Bash Konsole ein leeres Verzeichnis auf Ihrem Computer, z.B. `C:\temp\gitRepo`. Dieses Verzeichnis wird Ihr Git-Repository sein.

Du kannst die Unix/Linux-Befehle `ls` `cd` `pwd` und `mkdir` verwenden, um dieses Verzeichnis zu erstellen.

```bash
mkdir -p c:\temp\gitRepo
cd c:\temp\gitRepo
```

## Initialisieren

Sobald du in diesem Verzeichnis bist, initialisiere es als Git Repo mit dem Befehl :

```bash
git init
```

Was hat sich in dem Verzeichnis geändert, nachdem du es als Git-Repo initialisiert hast?

```{note}
Schreiben Sie die Antwort auf!
```

## Status abfragen

Erhalten Sie Informationen über Ihr Repo mit den folgenden Befehlen:

```bash
git status
git log --oneline
```

## Datei hinzufügen

Erstellen Sie nun eine leere Datei mit dem Namen `README.md` im Hauptverzeichnis Ihres Repos.
Verwenden Sie den vorherigen Befehl, um erneut die Informationen über Ihr Repo abzurufen. Was hat sich geändert?

```{note}
Schreiben Sie die Antwort auf!
```

Ihr lokales Git-Repo besteht aus drei Bereichen, die von `git` gepflegt werden:
* Das `Working directory` ist ein Verzeichnis, das die aktuelle Version deiner Dateien enthält (in den Augen deines Betriebssystems ein normales Dateiverzeichnis) ;
* `Stage` enthält die Änderungen, die in den nächsten Commit aufgenommen werden sollen;
* Der `Head` zeigt auf den Ort im Git-Repo-Baum, an dem der nächste Commit durchgeführt werden soll.

```{figure} resources/git-stages-local.svg
---
width: 60%
name: git stages local
---
Arten von lokalen Git Operationen
```

Ein einfaches Git-Repo, das aus fünf Commits besteht, kann folgendermassen dargestellt werden. Die Position `Head` ist ein Verweis auf einen Commit, der den aktuellen Status/die aktuelle Ansicht des Repos darstellt, hier die letzte Änderung.

```{figure} resources/gitgraph-history.png
---
width: 80%
name: git local repo 1
---
Fünf commits auf dem lokalen Repo, jeder `commit` besitzt seine eigene identifikation
```

## Datei in Repo aufnehmen
Fügen Sie die zuvor erstellte Datei `README.md` zur Stage hinzu, mit dem Befehl:

```bash
git add README.md
```

Rufen Sie erneut die Informationen über Ihr Repo ab, was stellen Sie fest?

```{note}
Schreiben Sie die Antwort auf!
```

Bearbeiten Sie die Datei `README.md`mit einem texteditor und fügen Sie den folgenden Text ein (Markdown-Syntax):

````markdown
# Titel meines Readme
Text und noch mehr Text, gefolgt von einer kleinen Liste :
  * Item 1
  * Item 2
  * Item 3
Und schliesslich ein wenig Code:
```sh
$ cd myDir
$ git init
$ git status
$ ls -al
```
````

Erhalte erneut die Informationen über dein Repo, was stellst du fest?

```{note}
Schreiben Sie die Antwort  auf!
```

## Neue Änderungen hinzufügen
Fügen Sie die neueste Version der Datei `README.md` zum Stage hinzu.

```bash
git add README.md
```

## Commit ausführen

Führen Sie nun einen Commit mit folgendem Befehl durch:

```bash
git commit -m "Initial commit. Add README file."
```

```{important}
Die Option `-m` erlaubt es, die Nachricht des Commits direkt anzugeben.
Diese Nachricht muss selbsterklärend sein. Sie entspricht der Beschreibung der Änderungen. Es ist möglich, einen Textblock z. B. über einen Texteditor einzufügen, ohne die Option "-m" zu verwenden.
```

## Mehr informationen
Welche Informationen erhalten Sie nun mit dem Befehl

```bash
git log -oneline
```

Erläutern Sie alle Informationen in dieser Zeile deutlich.

```{note}
Schreiben Sie die Antwort auf!
```

## Weitere commits
Ihre Änderungen werden nun in Ihrem lokalen Git-Repo veröffentlicht. Bravo!

Führen Sie einen weiteren Commit durch, um eine neue (leere) `hello_world.py` Datei in Ihr Repo aufzunehmen.

Welche neuen Informationen liefert Ihnen nun der Befehl

```bash
git log
```

```{note}
Schreiben Sie die Antwort auf!
```

Beachten Sie, dass jeder Commit mit einem "Hash" oder einer "Prüfsumme" (vom Typ sha1) versehen wird. Die mit dem Befehl:

```bash
git log --oneline
```

angezeigten Hashes sind nur die ersten paar Zeichen dieser sogenannten "_short hashes_".

## Checkout commit
Führen Sie nun einen Checkout mit dem folgenden Befehl durch und verwenden Sie dabei den "short hash" , der Ihrem **ersten** Commit entspricht.

```bash
git checkout <SHA1> -b inspectingPrev
```


Was stellen Sie nun fest, wenn Sie den Inhalt des Working Directory aufrufen?

```{note}
Schreiben Sie die Antwort auf!
```

## Checkout `master`
Führen Sie nun einen Checkout mit dem folgenden Befehl durch:

```
git checkout master
```

Was stellen Sie nun fest, wenn Sie den Inhalt des working directory?

```{note}
Schreiben Sie die Antwort auf!
```