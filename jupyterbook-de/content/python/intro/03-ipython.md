---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"deletable": true, "editable": true}

# ipython 

[ipython](https://ipython.org) ist eine _interaktive_ Version des Python-Interpreters. Er bietet eine Reihe von Extras, die beim Schreiben von Code hilfreich sind. "ipython"-Code ist fast immer "Python"-Code, und die Unterschiede sind im Allgemeinen nur wichtig, wenn man den Code in einer interaktiven Umgebung bearbeitet.

## ipython und Jupyternotebook

Das "Jupyter"-Notizbuch ist ein gutes Beispiel für eine interaktive Umgebung - Sie ändern den Code, während er läuft, und überprüfen die Antworten, während Sie Zellen ausführen. Da Sie in einem interaktiven Skript viele halbfertige Ergebnisse haben können, wollen Sie wahrscheinlich so wenige Fehler wie möglich machen. Das ist der Zweck von `ipython`.

`ipython` bietet Zugriff auf das Hilfe-/Dokumentationssystem, bietet Tabulatorvervollständigung von Variablen- und Funktionsnamen, erlaubt es Ihnen zu sehen, welche Methoden in einem Modul vorhanden sind ...

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: true
---
## Try the autocomplete ... it works on functions that are in scope

print

# it also works on variables

long_but_helpful_variable_name = 1

long_but_helpful_variable_name
```

+++ {"deletable": true, "editable": true}

---

Es funktioniert mit Modulen, um die verfügbaren Methoden und Variablen aufzulisten. Nehmen Sie zum Beispiel das Modul "math":

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
tags: []
---
import math

math.isinf  # Try completion on this

help(math.isnan)

# try math.isinf() and hit <kbd>Shift</kbd>+<kbd>Tabulator</kbd> while the cursor is between the parentheses
# you should see the same help pop up.

# math.isinf()
```

+++ {"deletable": true, "editable": true}

---

Es funktioniert bei Funktionen, die spezielle Argumente annehmen, und sagt Ihnen, was Sie angeben müssen.

Probieren Sie dies aus und versuchen Sie, die Klammern mit einem <kbd>Tabulator</kbd> zu versehen, wenn Sie diese Funktion selbst verwenden:

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
tags: [raises-exception]
---
import string
string.capwords("the quality of mercy is not strained")

string.capwords()
```

+++ {"deletable": true, "editable": true}

## Kommandozeilen Befehle

Es bietet auch die Möglichkeit Kommandozeilen Komandos auszuführen. hierfür wird die zugrunde liegende Shell / das Dateisystem benutzt. Diese Befehler müssen zubeginn jeder Zeile mit einem `!` markiert werden. **Dies ist kein Python Code mehr**

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
---
# execute simple unix shell commands 

!ls

!echo ""

!pwd
```

+++ {"deletable": true, "editable": true}

---

## Magics

Eine andere Möglichkeit ist, die __cell magic__-Funktionalität zu verwenden, um das Notebook anzuweisen, die Zelle in etwas anderes zu ändern (hier wird alles in der Zelle als Unix-Shell interpretiert). Hierfür muss zubeginn der Zelle das **Magic** angegeben werden. Diese Befehle beginnen mit `%%` oder `%`.

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: false
---
%%sh 

ls -l
echo ""
pwd
```

+++ {"deletable": true, "editable": true}

---

  - Ein "%" ist eine einzeilige magische Funktion, die irgendwo innerhalb der Zelle stehen kann.
  - Ein `%%` ist eine zellenweite magische Funktion.

```{code-cell} ipython3
---
deletable: true
editable: true
jupyter:
  outputs_hidden: true
---
%magic  # to see EVERYTHING in the magic system !
```

+++ {"deletable": true, "editable": true}

Nützliche magische Funktionen:

   - `%matplotlib inline` sorgt dafür, dass Plots im Notizbuch und nicht in einem externen Fenster erscheinen
   - `%run FILE` führt den Inhalt der Datei anstelle der angegebenen Zelle aus
   - `%%timeit` misst, wie lange die Zelle zum Ausführen braucht
   
---

+++ {"deletable": true, "editable": true}

Sie können ipython auch im Terminal/Shell auf Ihrem Rechner ausführen. Sie werden sehen, dass ein Teil der Interaktivität auch in einer Textumgebung funktioniert, aber nicht alle Pop-up-Hilfen sind so hilfreich wie in den Notizbüchern.
