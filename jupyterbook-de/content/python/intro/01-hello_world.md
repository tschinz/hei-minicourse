---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Hello World

Das erste, was wir tun sollten, ist, uns mit der Form und dem Gefühl von Python-Code vertraut zu machen, denn wir können die Funktionen von Python nicht wirklich ohne ein paar Beispiele diskutieren. Hier ist also eine kleine Einführung...

```{admonition} Randnotiz
Der Name Python leitet sich von *Monty Python's Flying Circus* ab, was bedeutet, dass Sie bei der Erwähnung eines [Phrase Book](https://www.youtube.com/watch?v=C1Sw0PDgHU4) alarmiert sein sollten.
```

## Obligatorisches Hell Worls Programm

```python
# Mein erstes Hello World Program
print("Hello World")
```
---
```
Hello World
```

Um dieses einfache Beispiel auszuführen, sind keine Vorbereitungen nötig, da der Befehl `print` in Python eingebaut ist.
Er ist eigentlich als *Funktion* implementiert, die ihr Argument auf dem Bildschirm ausgibt. Jetzt wissen Sie, wie Python-Funktionen aussehen! Du kannst auch sehen, wie man einen Kommentar schreibt.

Here are a couple of other ways to do the same thing

```python
hello_world_string = "Hello World"
print(hello_world_string)

# Formatting output is also possible
print("Mein {:s} Program".format(hello_world_string))
```
---
```
Hello World
Hello World
```

Wir können die Nachricht einer Variablen zuweisen und diese direkt ausdrucken. Der Funktion `print` muss nicht gesagt werden, dass `hello_world_string` eine Zeichenkette ist. Variablennamen dürfen Unterstriche, Buchstaben und Zahlen enthalten (mit Ausnahme des ersten Zeichens, das keine Zahl sein darf). Unterstriche am Anfang einer Variable werden üblicherweise *"versteckt"*, was eigentlich nur bedeutet, dass sie in einer interaktiven Umgebung etwas schwieriger zu finden sind.

```{note}
Tatsächlich ist string ein Python-Objekt, das versteht, dass es gedruckt werden muss und entsprechend auf den Aufruf der print-Funktion reagiert. Die Funktion "format" ist ebenfalls Teil des Repertoires des String-Objekts, und wir werden diese Art des Zugriffs auf die "Methoden" eines Objekts mit "object.function" sehr oft sehen.
```

## Einrückung und Blockstruktur

`python` verwendet Einrückungen, um Codeblöcke zu definieren, wenn die Einrückung unterbrochen wird beschwert sich der Interpreter. Dies ist wichtig für die Definition von Funktionen, bedingten Anweisungen, Schleifen und so weiter:

```{important}
Die Anzahl der Einrückungen ist standartmässig `4` Leerzeichen, kann aber theoretisch frei gewählt werden. In einer Datei muss aber immer die gleiche Anzahl an Leerzeichen pro Einrückung verwendet werden.
```

### Beispiel von Einrückungen

Wir haben uns für `2` Leerzeichen pro Einrückung entschieden.

```python
for i in range(0,5):
  print("The value of i is {} ".format(i), end=" ")
  if i%2:
    print("which is an odd number")
  else:
    print("which is an even number")
```

Dies hat das Layout eines typischen Python-Codes - die Blöcke, aus denen eine Schleife oder die Verzweigungen von Bedingungen bestehen, werden durch die Einrückung definiert.

## Funktionen

```python
def my_first_function(argument1, argument2):
  """This is the description of the function. Also called Docstring.
     This function returns argument 1

  Args:
      argument1 (_type_): _description_
      argument2 (_type_): _description_

  Returns:
      (_type_): _description
  """
  return(argument1)
```

```python
print(my_first_function(1,2))
print(my_first_function("Hello world", 0))
help(my_first_function)
```
---
```
1
Hello world

Help on function my_first_function in module __main__:

my_first_function(argument1, argument2)
    This is the description of the function. Also called Docstring.

  Args:
      argument1 (_type_): _description_
      argument2 (_type_): _description_

  Returns:
      (_type_): _description
```

Weiteres Beispiel einer Funktion mit mehreren Rückgabewerten.

```python
def my_second_function(argument1, argument2):
  """This is the description of the function. Also called Docstring.
     This function returns argument 1

  Args:
      argument1 (_type_): _description_
      argument2 (_type_): _description_

  Returns:
      (_type_): _description
  """
  return(argument1, argument2)
```
```python
print(my_second_function(1,2))
print(my_second_function("Hello world", 0))
help(my_second_function)

a,b = my_second_function(1,2)
print(a)
print(b)
```
---
```
(1, 2)
('Hello world', 0)
Help on function my_second_function in module __main__:

"""This is the description of the function. Also called Docstring.
     This function returns argument 1

  Args:
      argument1 (_type_): _description_
      argument2 (_type_): _description_

  Returns:
      (_type_): _description
  """

1
2
```

Funktionen können viele Argumente zurückgeben, die als `tuple` zurückkommen. Es ist einfach, die zurückgegebenen Werte zu *entpacken*.

```{note}
Da "Python" eine interpretierte Sprache ist, müssen Sie Funktionen definieren, bevor sie im Code vorkommen.
```

## Module

Die Stärke von `python` liegt wahrscheinlich in der Art und Weise, wie es die gemeinsame Nutzung fördert und eine Gemeinschaft von Nutzern aufbaut. Bevor wir viel mit `python` machen können, müssen wir im Allgemeinen die *Module* mit den zusätzlichen Funktionen, die wir brauchen, importieren.

Zum Beispiel enthält die Standard-Python-Bibliothek Module für grundlegende Dateisystem-Operationen, String-Manipulation, mathematische Funktionen, das Erzeugen von Prozessen, uvm. Die vollständige Liste finden Sie in der [python documentation](https://docs.python.org/3/py-modindex.html).

### `import` Beispiele

Import eines kompleten Moduls

```python
import math

print(math.sin(math.pi/2))
print(math.cos(math.pi/2))
```
---
```
1.0
6.123233995736766e-17
```
---

Dieser `import` importiert ein ganzes Modul. Manchmal möchten wir aber nur Teile importieren un dadurch etwas Zeit sparen oder um Namensverletzungen vorzubeugen.

```python
from math import sin, pi

print(sin(pi/2))  # imported
print(cos(pi/2))  # not imported
```
---
```
1.0
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-2b3c4d0b7471> in <module>
      4
      5 #
----> 6 print(cos(pi/2))

NameError: name 'cos' is not defined
```

Um Namensverletzungen vorzubeugen können verschiedene functionen aus verschieden Modulen welche aber den gleichen Namen besitzten mit unterschiedlichen Namen ausgestattet werden.y.

```python
from math import sin, pi
from cmath import sin as csin

print(sin(pi/2))
print(csin(pi/2))
```
---
```
1.0
(1+0j)
```
---

Im obigen Beispiel besitzten die Module `math`und `cmath`die Function `sin`. Deshalb wird die Funktion vom Modul `cmath`zu `csin` umbenannt.