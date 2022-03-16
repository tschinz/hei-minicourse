# Gitflow

Git fördert also stark die Erstellung von Branches, lässt den Entwicklern aber völlige Freiheit bei der Verwendung. Es ist also ein mächtiges Werkzeug, das bei falscher Anwendung kontraproduktiv werden kann. Entwicklungsteams entscheiden daher typischerweise einen Entwicklungsplan ("Workflow") mit Git, der ihre Richtlinien für das Erstellen von Branches und Merges festlegt.

Dieser Abschnitt beschreibt Git-flow ([A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)), einen Workflow, der aus einer Reihe von Regeln besteht, die das Zweigmodell von Git verwenden. Hier sind die grundlegenden Prinzipien:

Das Reposetup des Entwicklungsteams behält ein zentrales Repo (z. B. bei einem Webhoster von Git-Servern wie "GitHub" "Bitbucket" oder "Gitlab"). Wir nennen dieses zentrale Repo `origin`. Beachten Sie, dass dieses Repo nur willkürlich zentral ist, da Git ein dezentrales Quellverwaltungssystem ist und ohne ein einziges zentrales Repo auskommt.

```{figure} resources/gitflow-centralize-decentralize.png
---
width: 60%
name: distributed git 2
---
Verteiltes Git Repository Quelle: [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

Jedes Projekt wird auf zwei Hauptzweigen basieren: `master` und `develop. Diese beiden Zweige sind für Entwickler strengstens verboten zu schreiben.

```{figure} resources/gitflow-main-branches.png
---
width: 40%
name: git main branch
---
Git Zeige `master` und `develop` Quelle: [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

Der Master Branch ist der Spiegel unserer Produktion (das an die Benutzer gelieferte Produkt). Daher ist es logisch, dass wir unsere Änderungen nicht direkt dorthin schieben können. Der `origin/master`-Zweig wird daher als der Hauptzweig des Quellcodes betrachtet, in dem sich der `HEAD` immer in einem für den Kunden bereiten Zustand befindet.

Im `origin/develop`-Zweig werden alle neuen Funktionen zentralisiert, die in der nächsten Version enthalten sein werden (manchmal auch als Integration bezeichnet). In diesem Zweig können auch keine Änderungen direkt vorgenommen werden. Der `HEAD` von `origin/develop` zeigt also den Status der letzten abgeschlossenen Entwicklungen an. Dies ist typischerweise der Zweig, an dem jede Nacht automatisierte Tests durchgeführt werden. Sobald der `develop`-Zweig als stabil gilt, wird er in den `master` gemerged, um eine stabile Version (ein Deliverable) unserer Software zu erstellen.

Drei weitere Arten von Branches werden es uns dann ermöglichen, im Team und parallel zu arbeiten. Im Gegensatz zu den zuvor besprochenen Zweigen haben diese eine kurzlebige Lebensdauer.

* `feature`
* `release`
* `hotfix`

Diese drei Arten von Zweigen haben einen ganz bestimmten Zweck:

Zweige vom Typ `feature` werden verwendet, um neue Funktionen zu implementieren. Sie werden daher aus dem `develop`-Zweig gebildet. (z. B. `feature/new-button-on-front-screen`). Sie ermöglichen es, jede neue Funktion zu isolieren und erleichtern die parallele Arbeit.
Sobald ein Feature vom Team als "done" (fertig) akzeptiert wurde, wird es in den `develop`-Zweig eingegliedert, wie in der folgenden Abbildung dargestellt:

```{figure} resources/gitflow-merge-without-ff.png
---
width: 60%
name: git feature branch
---
Git Zeige `feature` und `develop Quelle: [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

Release-Zweige werden verwendet, um die Freigabe einer neuen Version vorzubereiten. Sie werden von `develop` aus erstellt (z. B. `release/january-general-update`). Sie ermöglichen es anderen Entwicklern, den `develop`-Zweig parallel zur Vorbereitung der neuen Freigabe weiter zu füttern. Sobald alle Tests erfolgreich bestanden sind und die Freigabe als "done" gilt, wird sie in `master` eingemischt. Wenn Korrekturen am `release`-Zweig vorgenommen wurden, werden diese ebenfalls in den `develop`-Zweig eingemischt.

Zweige vom Typ `hotfix` werden verwendet, um Fehler in der Produktion zu beheben. Wir werden diese Art von Zweigen also direkt aus dem Master erstellen, da wir nicht alle in `develop` verfügbaren Funktionen einbeziehen wollen (z. B. `hotfix/crash-when-button2-pressed`). Typischerweise muss ein Fehler, der in einem Produkt in der Produktion auftritt, zuerst mit einem automatischen Test reproduziert werden (um sicherzustellen, dass er in Zukunft nicht mehr auftritt), dann wird er auf dem `hotfix`-Zweig behoben. Schliesslich wird der `hotfix`-Zweig sowohl in den `master`- als auch in den `develop`-Zweig eingemischt.

```{figure} resources/gitflow-hotfix-branches.png
---
width: 30%
name: git hotfix model
---
Git hotfix merging Quelle: [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

Ein komplettes Beispiel eines Gitflow Projektes kann in der untenstehenden Abbildung betrachtet werden.

```{figure} resources/gitflow-model.png
---
width: 60%
name: git flow model
---
Komplettes GitFlow Model Quelle: [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
```

[Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
[Learn Git Branching](https://learngitbranching.js.org/)
