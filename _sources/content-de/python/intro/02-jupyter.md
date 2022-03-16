---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.9'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"deletable": true, "editable": true}

(section:jupyter_notebook)=
# Jupyter Notebooks

Wir werden in all unseren Beispielen das Notizbuchsystem `jupyter` verwenden und in den Notizbüchern selbst eine Version von Python, bekannt als `ipython`.

Das Notizbuch ist ein __lebendiges__ Dokument, das eine Reihe verschiedener Arten von Inhalten enthalten kann. Dies können Textelemente formatiert in Markdown oder Programfragemente sein welche auch ausgeführt werden können. Aktuell betrachten Sie die statische Webseite worin der Code nicht ausgeührt werden kann. Hierzu müssen die Im Racktensymbol die Seite als interaktives Noritzbuch auf Binder starten.


```{figure} img/rocket-icon.png
---
width: 80%
name: Rocket icon
---
Starten des Jupyter Notebooks
```

Sie können die Notizbücher als Notizblock verwenden, um Code zu schreiben und diesen gleichzeitig zu dokumentieren.
Es ist wie ein Labornotizbuch, aber für Datenmanipulation und Programmierung.
Sie können das erstellte Dokument auch als PDF exportieren, um einen Laborbericht zu erstellen.

Beachten Sie das das Notizbuch auf Binder nicht gespeichert wird, sobald Sie die Webseite schliessen werden Ihre Modifikationen verloren sein. Vergessen Sie nicht das Dokument auf Ihrem Computer zu speichern falls Sie es behalten möchten.

+++

Ein Notizbuch besteht aus verschiedenen __Zellen__ (Cells), die verschiedene Arten von Inhalten enthalten und die _ausgeführt_ werden können, indem man die Zelle auswählt und sie _ausführt_ durch Betätigen des _Run_ Knopfes oder durch Eingabe von "Shift + Enter".
Die Ergebnisse der Ausführung einer Zelle hängen vom Inhalt der Zelle ab. Sie kann eine darunter liegende Ausgabezelle mit Ergebnissen erzeugen oder sich selbst neu formatieren.

(section:markdowncells)=
## Markdown Zellen
Eine Markdown Zusammenfassung finden Sie [hier](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Die Formatierung in Markdown sieht folgendermassen aus:

````md
### Formatierter Text

Hier wird eine fast fertig formatierte Version von Text verwendet, die als "Markdown" bekannt ist, um Inhalte zu erstellen, die so formatiert werden können, dass sie einem Word-Dokument ähneln, aber auch die beabsichtigte Formatierung hervorheben, selbst wenn sie nicht verarbeitet werden. Es ist eine recht nützliche Form, die man lernen kann, um Notizen zu machen.

Wenn Sie sich den Rohinhalt ansehen, werden Sie sehen, wie man

* Aufzählungspunkte
  * verschachtelte Aufzählungspunkte sowie
  * Text in __fett__
  * Text in _Kursivschrift_ (oder hervorgehoben)

```sh
echo "Code, der für verschiedene Sprachen hervorgehoben werden kann"
ls -l
```

```python
print("einschließlich Python, Unix-Shell-Skripte, Fortran")

for i in range(0,100):
    print(i)
```

Mathematische Symbole und Formeln, können innerhalb eines Textes $2\pi r$ oder als Gleichung erscheinen:

$$
    A = \pi r^2
$$

ABER Sie müssen in der Lage sein, die Formeln in der Sprache $\LaTeX$ zu beschreiben.

Sie können Links wie diese hinzufügen: [siehe auch das Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Und Bilder wie dieses:

![Python Course](./../img/python-course.svg)

````
---
Dies ergibt der folgender Paragraph:

### Formatierter Text

Hier wird eine fast fertig formatierte Version von Text verwendet, die als "Markdown" bekannt ist, um Inhalte zu erstellen, die so formatiert werden können, dass sie einem Word-Dokument ähneln, aber auch die beabsichtigte Formatierung hervorheben, selbst wenn sie nicht verarbeitet werden. Es ist eine recht nützliche Form, die man lernen kann, um Notizen zu machen.

Wenn Sie sich den Rohinhalt ansehen, werden Sie sehen, wie man

* Aufzählungspunkte
  * verschachtelte Aufzählungspunkte sowie
  * Text in __fett__
  * Text in _Kursivschrift_ (oder hervorgehoben)

```sh
echo "Code, der für verschiedene Sprachen hervorgehoben werden kann"
ls -l
```

```python
print("einschließlich Python, Unix-Shell-Skripte, Fortran")

for i in range(0,100):
    print(i)
```

Mathematische Symbole und Formeln, können innerhalb eines Textes $2\pi r$ oder als Gleichung erscheinen:

$$
    A = \pi r^2
$$

ABER Sie müssen in der Lage sein, die Formeln in der Sprache $\LaTeX$ zu beschreiben.

Sie können Links wie diese hinzufügen: [siehe auch das Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Und Bilder wie dieses:

![Python Course](img/python-course.svg)

```{note}
Wenn Sie Zellen mit formatiertem Code ausführen, wird die Zelle durch die formatierte Version ersetzt. So können Sie eine gut formatierte Seite mit verschachteltem Code schreiben, der auch ausgeführt werden kann.
```
---

(section:pythoncells)=
## Python-Code

Zellen, die als Codezellen definiert sind, enthalten Python-Anweisungen, die ausgeführt werden, wenn die Zelle ausgeführt wird. Wenn mehrere Zellen Code enthalten, werden sie in der von Ihnen gewählten Reihenfolge ausgeführt (oder wenn Sie "run all" oder "run all above" wählen, werden sie in der Reihenfolge ausgeführt, in der sie aufgelistet sind).

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
solution: hidden
---
## Beispiel für eine einfache Python-Code-Zelle

print("Hallo kleine Welt")
a = 1
```

+++ {"deletable": true, "editable": true}

Wenn Sie eine Code-Zelle ausführen, ist es dasselbe, als wenn Sie den gesamten Code in den Interpreter eingeben. Wenn Sie eine Zelle zweimal ausführen, ist es dasselbe, als hätten Sie alles zweimal eingegeben ... das Notizbuch merkt sich das! Sie können einen Teil des Notizbuchs oder das gesamte Notizbuch ausführen, und Sie können Zellen auch in anderer Reihenfolge ausführen. Das ist großartig, um zu experimentieren, aber seien Sie vorsichtig, das kann auch teilweise verwirrend sein.

## Beispiel
Hierzu ein kleines Beispiel. Wiso funktioniert die untenstehende Zelle aber die nächste nicht?

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
---
print("Zähler {}".format(a))
a += 1
```

+++ {"deletable": true, "editable": true}

Warum funktioniert das nicht?

```python
print("Zähler {}".format(b))
b += 1
```

und, was noch wichtiger ist, wie würden Sie das Problem beheben?

Starten Sie das Notebook und editieren Sie die untenstehende Zelle. Die Zelle kann mit <kbd>Shift</kbd>+<kbd>&#9166;</kbd> ausgeführt werden.

```{code-cell} ipython3
---
jupyter:
  outputs_hidden: false
Solution: hidden
---
# Versuchen Sie es!
```

```{code-cell} ipython3
:tags: [hide-cell]

## Weil b noch nicht definiert wurde, a aber in der davorgegangenen Zelle schon.

try:
    print("Zähler {}".format(c))
except:
    print("Zähler")
    c = 1

c += 1
```

## Jupyter benutzten

In diesem Kurs werden wir die Aufgaben interaktiv auf einem Jupyter Server lösen. Das starten des Notebookes auf [Binder](https://jupyter.org/binder) mit hilfe des Rocket Icons habt Ihr [zu beginn der Seite](section:jupyter_notebook) bereits gelernt. Dank diesem Server könnt Ihr den Code hinzufügen, löschen und ergänzen um Ihn danach auszuführen.

Jupyternotebook ist wie beretis erwähnt auf Zellen basiert. Die Zellen können entweder [Formatierter Text im Markdown Format](section:markdowncells) oder [Python Code](section:pythoncells) sein. Jede Zelle kann separat ausgeführt werden.

Der aktuelle Zellentyp kann in der Dropbox ausgewählt werden

```{figure} img/jupyter_command_bar_celltype.png
---
width: 80%
name: jupyter celltype
---
Auswahl bzw. Änderung eines Zelltyps
```

Neue Zellen können über das `Insert` Menü eingefügt werden.

```{figure} img/jupyter_command_bar_insert.png
---
width: 80%
name: jupyter cellinsert
---
Hinzufügen einer Zelle
```

Eine Zelle kann entweder mit dem `Run` Knopf oder mit <kbd>Shift</kbd>+<kbd>&#9166;</kbd> ausgeführt werden. Alternative können auch über das `Cell` Menu alle obenstehenden oder untenstehenden Zellen ausgeführt werden.

```{figure} img/jupyter_command_bar_run.png
---
width: 80%
name: jupyter cellrun
---
Ausführen einer Zelle
```

Sobald eine Zelle ausgeführt wird ist die über einen gefüllten Kreis oben rechts sichtbar. Dieser Punkt teils mit ob der Python Kernel aktiv ist oder nicht

```{figure} img/jupyter_command_bar_running.png
---
width: 80%
name: jupyter cellrunning
---
Python Kernel ist aktiv
```

Zusätzlich steht rechts neben der Zelle die eine Bemerkung `ln[<x>]`.

Diese zeigt an ob eine Zelle aktuell ausgeführt wird `In [*]:`. Oder wann die Zelle seit dem Python Kernel start ausgeführt wurde `In [3]:`. Die Nummer wird bei jeder aufgeführten Zelle inkrementiert.

Falls eine Zelle gestoppt werden soll, z.B. falls die Berechnung zuviel Zeit beansprucht kann dies über den `Stop` Knopf geschehen.

```{figure} img/jupyter_command_bar_stop.png
---
width: 80%
name: jupyter cellstop
---
Stoppen einer Ausführung
```

Direkt unterhalb der Zelle befindet sich das Fenster der Ausgabe der jeweiligen Zelle.

```{note}
Ihr solltet nun alle benötigten Informationen haben um Jupter Notebooks auszuführen.
```