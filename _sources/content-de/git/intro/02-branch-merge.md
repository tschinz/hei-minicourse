# Branch und Merge

Bisher haben wir die grundlegenden Funktionen von git verwendet. Es gibt auch die Funktionen `branch` (Zweig) und `merge`(zusammenführen), die Git im Vergleich zu den früher existierenden Tools stark vereinfacht hat.

Standardmässig existiert in git immer ein "master"- oder "main"-Zweig:

```{figure} resources/git-local-repo-1.png
---
width: 30%
name: git local 1
---
Repository mit `master` `branch`
```

Git wird es uns ermöglichen, ganz einfach einen neuen Zweig zu erstellen:

```bash
git branch dev_branch_1
```

```{figure} resources/git-local-repo-2.png
---
width: 30%
name: git local 2
---
Repository mit `master` und `dev_branch_1` `branch`
```

Git wird uns auch erlauben, die vorhandenen Zweige einfach in Form einer Liste aufzulisten. Ein Stern (*) vor dem Namen des Zweigs zeigt an, auf welchem Zweig du dich gerade befindest.

```bash
git branch
```

Um auf dem Entwicklungszweig, den wir gerade erstellt haben, zu entwickeln, können wir diesen Zweig auschecken (HEAD ändern):

```bash
git checkout dev_branch_1
```

```{figure} resources/git-local-repo-3.png
---
width: 30%
name: git local 3
---
Repository mit selektierem `dev_branch_1` `branch`
```

Jeder Commit auf diesem Zweig kann daher wie folgt dargestellt werden:

```{figure} resources/git-local-repo-4.png
---
width: 30%
name: git local 4
---
Repository einem `dev_branch_1` commit
```

Dann den nächsten Commit:

```{figure} resources/git-local-repo-5.png
---
width: 30%
name: git local 5
---
Repository einem weiterm `dev_branch_1` commit
```

Git ermöglicht auch das einfache Mergen (Zusammenführen) dieses Entwicklungszweiges:

```bash
git checkout master
git merge dev_branch_1
```

Beachte, dass man bei der Merge-Operation an dem Branch arbeitet, in dem man mergen will, und einen anderen Branch in den Branch mergt, an dem man arbeitet.

In dem obigen einfachen Fall, in dem keine weiteren Commits auf dem `master`-Zweig gemacht wurden, wird Git in der Lage sein, ein `fast-forward` merge durchzuführen und einfach den Zeiger auf den `master`-Zweig zu verschieben.


```{figure} resources/git-local-repo-6.png
---
width: 30%
name: git local 6
---
Repository mit `dev_branch_1` merged mit `master` `branch
```

Für den Fall, dass in der Zwischenzeit weitere Commits auf dem `master` branch durchgeführt wurden:

```{figure} resources/git-local-repo-7.png
---
width: 30%
name: git local 7
---
Repository mit `master` `branch`
```

Git wird automatisch einen neuen Merge-Commit erstellen und einen `three way merge` durchführen:

```{figure} resources/git-local-repo-8.png
---
width: 30%
name: git local 8
---
Repository mit `dev_branch_1` merged mit modifiziertem `master` `branch`
```

Git wird uns auch erlauben, Zweige zu löschen, die wir nicht brauchen:

```bash
git branch -d dev_branch_1
```

```{figure} resources/git-local-repo-9.png
---
width: 30%
name: git local 9
---
Repository mit `three way merge`
```

Beachten Sie, dass keiner der Commits gelöscht wird, nur die Zweiginformationen werden gelöscht.

