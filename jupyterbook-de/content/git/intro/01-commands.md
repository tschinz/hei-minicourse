# Kommandos

Eine Liste mit wichtigen viel benutzten Kommandos kann [hier](https://training.github.com/downloads/de/github-git-cheat-sheet/) besichtigt werden.

Eine interaktive Schrittweise Führung durch die verschiednen `git` Kommandos findet Ihr [hier](https://gitflow.smessina.com/#/)


## Änderungen überprüfen und ein `commit` durchführen

```bash
git status
```
Listet alle zum Commit bereiten neuen oder geänderten Dateien auf.

```bash
git diff
```

Zeigt noch nicht indizierte Dateiänderungen an.

```bash
git add [file]
```

Indiziert den derzeitigen Stand der Datei für die Versionierung.

```bash
git diff --staged
```

Zeigt die Unterschiede zwischen dem Index (“staging area”) und der aktuellen Dateiversion.

```bash
git reset [file]
```

Nimmt die Datei vom Index, erhält jedoch ihren Inhalt.

```bash
git commit -m "[descriptive message]"
```

Nimmt alle derzeit indizierten Dateien permanent in die Versionshistorie auf.

## Änderungen synchronisieren

Registrieren eines externen Repositories (URL) und Tauschen der Repository-Historie.

```bash
git fetch [remote]
```

Lädt die gesamte Historie eines externen Repositories herunter.

```bash
git merge [remote]/[branch]
```

Integriert den externen Branch in den aktuell lokal ausgecheckten Branch.

```bash
git push [remote] [branch]
```

Pusht alle Commits auf dem lokalen Branch zu GitHub.

```bash
git pull
```

Pullt die Historie vom externen Repository und integriert die Änderungen.

## Meistgebrauchten Git Befehle

| Befehl     | Beschreibung |
|:----------:|--------------|
| **Starten Sie einen Arbeitsbereich** ||
| `clone`    | Klonen eines Repositorys in ein neues Verzeichnis |
| `init`     | Erstellen eines leeren Git-Repositorys oder Reinitialisieren eines vorhandenen Repositorys |
| **Arbeit an der aktuellen Änderung** ||
| `add`      | Dateiinhalte in den Index aufnehmen |
| `mv`       | Verschieben oder Umbenennen einer Datei, eines Verzeichnisses oder eines Symlinks |
| `reset`    | Zurücksetzen des aktuellen HEAD auf den angegebenen Zustand |
| `rm`       | Dateien aus dem Arbeitsbaum und aus dem Index entfernen |
| **Untersuchen Sie die Geschichte und den Zustand** ||
| `log`      | Übergabeprotokolle anzeigen |
| `show`     | Verschiedene Arten von Objekten anzeigen |
| `status`   | Den Status des Arbeitsbaums anzeigen |
| **Wachsen, markieren und optimieren Sie Ihre gemeinsame Geschichte** ||
| `branch`   | Zweige auflisten, erstellen oder löschen |
| `checkout` | Zweige wechseln oder Arbeitsbaumdateien wiederherstellen |
| `commit`   | Änderungen am Projektarchiv aufzeichnen |
| `diff`     | Änderungen zwischen Commits, Commit und Arbeitsbaum anzeigen, etc. |
| `merge`    | Zwei oder mehr Entwicklungsgeschichten zusammenführen |
| `rebase`   | Commits auf einen anderen Zweigebereich neu aufsetzen |
| `tag`      | Ein mit GPG signiertes Tag-Objekt erstellen, auflisten, löschen oder verifizieren |
| **Zusammenarbeiten** ||
| `fetch`    | Herunterladen von Objekten und Verweisen aus einem anderen Repository |
| `pull`     | Abruf aus einem anderen Repository oder einem lokalen Zweig und Integration in dieses |
| `push`     | Aktualisieren Sie entfernte Referenzen zusammen mit den zugehörigen Objekten |

**Englische Version**

| Command    | Description |
|:----------:|--------------|
| **Start a working area** ||
| `clone`    | Clone a repository into a new directory |
| `init`     | Create an empty Git repository or reinitialize an existing one |
| **Work on the current change** ||
| `add`      | Add file contents to the index |
| `mv`       | Move or rename a file, a directory, or a symlink |
| `reset`    | Reset current HEAD to the specified state |
| `rm`       | Remove files from the working tree and from the index |
| **Examine the history and state** ||
| `log`      | Show commit logs |
| `show`     | Show various types of objects |
| `status`   | Show the working tree status |
| **Grow, mark and tweak your common history** ||
| `branch`   | List, create, or delete branches |
| `checkout` | Switch branches or restore working tree files |
| `commit`   | Record changes to the repository |
| `diff`     | Show changes between commits, commit and working tree, etc |
| `merge`    | Join two or more development histories together |
| `rebase`   | Reapply commits on top of another base tip |
| `tag`      | Create, list, delete or verify a tag object signed with GPG |
| **Collaborate** ||
| `fetch`    | Download objects and refs from another repository |
| `pull`     | Fetch from and integrate with another repository or a local branch |
| `push`     | Update remote refs along with associated objects |
