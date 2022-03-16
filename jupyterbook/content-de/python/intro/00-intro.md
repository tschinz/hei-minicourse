# Einführung

```{figure} img/python-course.svg
---
width: 30%
name: Python course logo
---
Python Kurs Logo
```

Es gibt einige Dinge, die man über die Sprache Python wissen sollte, bevor man sich damit beschäftigt. Das Wichtigste ist vielleicht, dass Python eine **interpretierte** Sprache und keine *kompilierte* Sprache ist, so dass es keine Übersetzung in schnellen, maschinenausführbaren Binärcode gibt. Dies stellt die effiziente Kodierung über die schnelle Ausführung und sagt viel über die Philosophie von Python als Sprache aus: Anwendbar auf eine sehr breite Klasse von Problemen, leicht zu lesen und auf hohem Niveau, so dass es einfach ist, bestehende Software wiederzuverwenden und darauf aufzubauen.

Python soll **einfach zu benutzen** sein: Sie müssen den Typ Ihrer Variablen oder Daten nicht angeben ("deklarieren"), bevor Sie sie verwenden, und sie **konvertiert automatisch** von einem Typ in einen anderen falls dies möglich ist, wenn dies sinnvoll ist. Zum Beispiel sind eine Fließkommazahl `1.0` und eine Ganzzahl `1` in Python meist austauschbar, so wie sie es auch im täglichen Leben sind. Wenn Sie eine Variable nicht mehr verwenden, müssen Sie sie nicht explizit löschen, Sie können es aber tun, wenn Sie möchten.

Python hat eine umfangreiche **Ausnahmebehandlung** (Exception handling), was einfach bedeutet, dass Fehler vom laufenden Programm behandelt werden können und nicht immer zu einem Absturz führen, der vom Betriebssystem behandelt wird. Im Allgemeinen ist es eine gute Idee, Code zu schreiben, der versteht, was schief gehen könnte und eine elegante Lösung bietet, wenn etwas schief geht. Ausnahmen führen auch zu einem *Try it and see* Ansatz bei der Programmierung. Es kann einfacher sein, einen Code zu schreiben, der einen Fehler abfängt, als zu versuchen, einen Code zu schreiben, der jede Situation ohne Fehler berücksichtigt.

Python ist auch eine **objektorientierte** Sprache, und es ist unmöglich, Python zu lesen, ohne zu verstehen, wie es seine Objekte beschreibt und dann auf sie verweist. Das Prinzip objektorientierter Sprachen besteht darin, Daten und Operationen mit diesen Daten in "Objekten" zu kapseln, die als eine Einheit weitergegeben werden können und die man dann verwenden kann, ohne die gesamte interne Struktur des Objekts kennen zu müssen. In objektorientierten Sprachen beschreiben wir in der Regel eine Klasse von Objekten, die bestimmte Eigenschaften haben (Daten, Operationen, Struktur), ohne notwendigerweise die Details zu kennen, wie diese Objekte implementiert werden. Man kann uns Klassen übergeben und uns sagen, wie wir sie verwenden, kopieren, erweitern usw., ohne sie erst auseinandernehmen zu müssen.

Python basiert auf **Bibliotheken** in Form von Modulen, die wir `importieren`, wenn wir sie brauchen. Es gibt sehr viele Module in der Standard-Python-Bibliothek für fast alles, von der Betriebssystemebene (ein Verzeichnis erstellen, eine Datei öffnen) bis zum High-Level-Zugriff auf Internet-Ressourcen, String-Manipulationen, Parsing regulärer Ausdrücke, mathematische Funktionen. Sobald ein Modul importiert wurde, stehen die darin definierten Funktionen und Klassen dem Programm zur Verfügung, und um das Leben einfacher zu machen, wird den Namen all dieser Funktionen und Klassen der Modulname vorangestellt, wenn sie verwendet werden. Was zwar etwas mehr Tipparbeit für einen Programmierer bedeutet, aber die Lesbarkeit verbessert und das Leben für jeden, der eine Bibliothek entwickelt, viel einfacher macht.

Wenn man nützlichen Code schreibt, ist es üblich, ihn in Form eines **Moduls** zu bündeln und dann zu verteilen, indem man ein Paket an einem Standardort hochlädt diese kann die Bibliothek [pip](https://pypi.org/project/pip/) oder [conda](https://anaconda.org/conda-forge/repo) sein. Diese Pakete werden dann über diese Paketmanager an die Benutzer verteilt, der intelligent genug ist, um sicherzustellen, dass Sie eine Version installieren, die auf Ihrem Rechner funktioniert und (noch komplizierter) mit allen anderen installierten Paketen übereinstimmt.

Die beiden wichtigsten Paketmanager für Python sind [pip](https://pypi.org/project/pip/) und [conda](https://anaconda.org/conda-forge/repo). [pip](https://pypi.org/project/pip/) ist ein wenig einfacher und kümmert sich wirklich nur um die Installation von Python-Paketen und deren Python-Abhängigkeiten.
[conda](https://anaconda.org/conda-forge/repo) ist sehr viel ehrgeiziger als `pip` - es verwaltet ganze Umgebungen, die auch Nicht-Python-Bibliotheken enthalten, die Pakete benötigen könnten. `conda` ist mächtiger als pip und versucht, viele andere Paketmanager zu ersetzen, die in der Nicht-Python-Welt existieren. Wenn Sie sich für `conda` entscheiden, sollten Sie wirklich alles ausprobieren und versuchen, es für die Verwaltung aller Pakete zu verwenden. `conda` erstellt virtuelle Umgebungen, die es Ihnen erlauben, mehrere Setups auf einer einzigen Maschine zu haben - praktisch, wenn Sie Pakete haben, die verschiedene Python-Versionen benötigen oder inkompatible Abhängigkeiten haben.

## Hintergrundlektüre

Die endgültige Referenz für Python ist [www.python.org](https://www.python.org). Es könnte jedoch hilfreich sein, zunächst verschiedene Artikel auf Wikipedia zu lesen, beginnend mit dem [Python Wikipedia Artikel](https://en.wikipedia.org/wiki/Python_(programming_language))
