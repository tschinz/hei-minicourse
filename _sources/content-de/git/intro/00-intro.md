# Einführung

```{figure} resources/icons/git-logo.svg
---
width: 40%
name: Git Logo
---
```
## Was ist Versionskontrolle?

Bei der Versionskontrolle wird festgehalten, wie oft Sie eine Datei bearbeiten, welche Änderungen Sie vornehmen und was Sie mit diesen Änderungen bezwecken. Dies ist eine Form der Versionskontrolle:

```Text
$ ls

    meine_datei_v0_0.md
    meine_datei_v1_0.md
    meine_fertige_datei_v1_1.md
    meine_datei_v1_0+Betreuer_Kommentare.md
    meine_datei_v1_0+Betreuer_Kommentare_v1_1_zusammengefasst.md
    meine_datei_v1_2.md

$ diff meine_datei_v1.md meine_datei_v1_2.md

    ... (alle Änderungen erscheinen)
```

Dies ist großartig, weil Sie eine Aufzeichnung aller Ihrer Änderungen haben, aber Sie können bereits sehen, dass es Probleme gibt, wenn Sie mehrere Sätze von Änderungen auf einmal machen. Softwaresysteme zur Versionskontrolle sollen hier Abhilfe schaffen. Sie formalisieren gängige Praktiken wie die Kennzeichnung von Dateinamen (das obige Beispiel) und fügen eine ganze Reihe von zusätzlichen Werkzeugen hinzu, um die Zusammenarbeit zu erleichtern.

Die andere Form der Versionskontrolle, die Ihnen vielleicht schon begegnet ist, ist *Änderungen verfolgen* in Microsoft Word oder das Versionssystem *Time Machine*, das Sie auf dem Mac finden können.

Diese Art der Versionskontrolle auf der Grundlage von Sicherungskopien ist gut, aber sie ist sehr linear in der Art und Weise, wie Änderungen verwaltet werden. Wie Sie oben sehen können, kann es zu echten Problemen kommen, wenn zwei Personen an einer Datei arbeiten. Während Sie darauf warten, dass Ihr Betreuer den Entwurf der Version 1.0 Ihrer Dissertation kommentiert, möchten Sie mit Sicherheit mit der Arbeit an Version 1.1 beginnen. Wenn Ihr Betreuer Ihnen Änderungen an Version 1.0 vorschlägt, müssen Sie erst einmal herausfinden, welche Änderungen Sie an Version 1.1 vornehmen müssen, um eine neue Version zu erstellen, bevor Sie mit Version 1.2 beginnen können.

Stellen Sie sich vor, wie viel komplizierter das wird, wenn viele Leute an einem Projekt arbeiten und vielleicht alle zusammen eine einzige Datei bearbeiten.

### Wiso Versionskontrolle

Versionskontrolle hat eine vielzahl von Nützlichen Funktionen, **jeder** Entwickler sollte mindestens ein Tool beherschen um:

* Fehler rückgängig machen (auf frühere Versionen zurückgreifen)
* Neue Funktionen unabhängig entwickeln und testen
* Ausführen und Testen mit älteren Versionen
* Beibehaltung und Wechsel zwischen mehreren Versionen des Codes
* Teamarbeit: automatisches Zusammenführen von Bearbeitungen durch verschiedene Personen
* Verteilen und Veröffentlichen von Analysen, Code und Arbeitsabläufen
* Archivieren oder sichern Sie Ihre Arbeit, damit sie nicht verloren geht, wenn Ihr Computer nicht mehr funktioniert.

## Werkzeuge gibt es?

Es gibt eine Reihe verschiedener Pakete, die Sie verwenden können, und sie alle haben ihre Vor- und Nachteile. Einige Beispiele, auf die Sie stoßen könnten, sind:

   - git: (`git`)
   - Subversion: (`svn`)
   - mercurial: (`hg`)

Sie sind alle annähernd gleichwertig und unterscheiden sich geringfügig in der Art und Weise, wie sie das Repository (die Datenbank mit der gesamten Geschichte des Projekts) verteilen. `git` legt den gesamten Verlauf aller Dateien auf jedem Rechner ab, was für zusätzliche Sicherheit sorgt. Wir werden in diesem Kurs nur mit git arbeiten da dies in den letzten Jahren zum defacto Standart in der Industrie geworden ist.

## Was ist `git`?

`git` ist ein *Verteiltes* und *nicht-lineares* Versionenmanagement welches stark auf Teamarbeit aus gelegt ist. Es wurde von [Linux Torvald](https://en.wikipedia.org/wiki/Linus_Torvalds) entwiuckelt und in 2005 erstmals veröffentlicht. Der Quellcode ist offen (Open Source) und wurde 2013 zum populärsten Versionenmanagement tool.
Sie können die Software selbst auf Ihrem eigenen Computer verwenden, um die Versionskontrolle eines Projekts zu verwalten. Die wirklichen Vorteile eines Tools wie `git` ergeben sich jedoch, wenn Sie ein vernetztes **Repository** Ihrer Dokumente verwenden, auf das Sie von mehreren Rechnern aus zugreifen und von Rechner zu Rechner synchronisieren können, wenn Sie bereit sind. Das können nicht nur *Sie* tun, sondern auch Ihre Mitarbeiter können auf die Dateien zugreifen und sie bearbeiten, und später können Sie dann die Änderungen auf organisierte Weise zusammenführen.

## Was ist github, gitlab und bitbucket?

Github, Gitlab sowie Bitbucket sind 3 Cloudplattformen welche gratis sowie kostenpflichtig verteilte Git Repository Server zur Verfüfugn stellen.
Wir haben einen gemeinsamen Bereich auf `github` und werden im Zuge dieses Kurses dort verwaltete Repositories gemeinsam Nutzen. `github` bietet ausserdem eine Vielzahl von Projektmanagement-Tools, die für Teams oder Klassen sehr hilfreich sein können. Als Beispiel kann hier Zugangskontrolle, Bug Tracking, Feature request, Projektmanagement erwähnt werden.

````{list-table}

   * - ```{figure} resources/icons/bitbucket-icon.svg
       ---
       width: 100%
       name: Bitbucket Logo
       ---
       Bitbucket Logo

     - ```{figure} resources/icons/github-logo.svg
       ---
       width: 100%
       name: Github Logo
       ---
       Github Logo
       ```

     - ```{figure} resources/icons/gitlab-logo.svg
       ---
       width: 100%
       name: Gitlab Logo
       ---
       Gitlab Logo
       ```
````
### Wie funktioniert `git`?

#### Commits

Ein `git` Repository beinhaltet die komplette Geschichte eines Projektes. Jeder Punkt in der Geschichte ist ein **commit**.

```{figure} resources/gitgraph-history.png
---
width: 80%
name: git history
---
git history Beispiel
```

#### Branches

Die Geschichte des Repositories kann nicht linear sein, weil es verschiedenen Zweige sogenante **branches** gibt.

```{figure} resources/gitgraph-history-nonlinear.png
---
width: 80%
name: git history non linear
---
git non linear history Beispiel
```

#### Distributed

Das Repository existiert nicht an einem zentralen Ort sondern ist verteilt, jeder der damit Arbeitet beitzt seine Kopie und hat seine Geschichte. Diese verteilten Repositories werden zu einem zentralen Repository (im Bild genannt **origin**) synchronisiert.

```{figure} resources/gitflow-centralize-decentralize.png
---
width: 60%
name: distributed git
---
Verteiltes Quelle: [Git Branching Modell](https://nvie.com/posts/a-successful-git-branching-model/)
```

## Operationen

Um Veränderungen auf dem lokalem (**local**) oder einem entfernten (**remote**) Repository durchzuführen sind verschiedene Aktionen notwendig.

* **working directory** beinhaltet die Dateien die sich aktuell im Ordner befinden, diese Dateien sind im Prinzip unverfolge (**untracked**), sofern nicht bereits eine Version in der Repository **committed** wurde.
* **staging area** beinhaltet Dateien und Veränderungen welche geplannt sind um ins Repository aufgenommen zu werden (**tracked**).
* Im Lokalen git Repository befinden sich gepspeicherte Dateien sowie deren Veränderungen diese sind beihaltet (**committed**).
* Das

```{figure} resources/git-stages.svg
---
width: 100%
name: git stages
---
git Operationen
```

### Tools für `git`

Standartmässig wird git über die Kommandozeile bedient, es gibt aber auch diverse Grafische Benutzeroberflächen welche das arbeiten mit `git` erleichtern. Falls man aber exakt wissen will was geschieht ist die Kommandozeile das beste Tool.

````{list-table}
   * - ```{figure} resources/icons/git-logo.svg
       ---
       width: 50%
       name: Git Kommandozeile
       ---
       [Git Kommandozeile](https://git-scm.com)
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
       name: Tower
       ---
       [Tower](https://www.git-tower.com/mac)
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
