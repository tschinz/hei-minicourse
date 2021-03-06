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

# Python Datentypen

Python kann ein wenig seltsam sein, da es viele Datentypen, dynamische Typzuweisung und einige Automatishe Konvertierungen bietet.


## Zahlen

Ganzzahlen, Fließkommazahlen und komplexe Zahlen sind automatisch verfügbar.

```{code-cell} ipython3
f = 1.0
i = 1
c = 0.0 + 1.0j

print(f, i, c)
print("Value of f is {}, value of i is {}, the value of c is {}".format(f, i, c))
print("Value of f is {:f}, value of i is {:f}, value of c**2 is {:f}".format(f, i, c**2))
```

---

```{note}
The `math` module needs to be imported before you can use it.
```

```{code-cell} ipython3
import math

math.sqrt(f)   # 1.0
math.sqrt(c)   # can't convert complex to float
math.sqrt(-1)  # math domain error
```

### Zahlen als Objekte

Praktisch alles in Python ist ein Objekt. Das bedeutet, dass es ein _Ding_ ist, das mehrere Kopien haben kann und das weiss, wie man bestimmte Operationen mit sich selbst _ausführt_.

Zum Beispiel kennt eine Fliesskommazahl bestimmte Dinge, die sie tun kann, als einfach nur eine Zahl zu sein:

```{code-cell} ipython3
f
help(f)

f.is_integer()      # True
i.imag              # 0
f.__truediv__(2.0)  # 0.5
```

## Strings

```{code-cell} ipython3
string_1 = "Hello"
string_1[0]          # H
string_1[-1]         # o
string_1[1:]         # ello
string_1[:-2]        # Hel
string_1[3:3]        # ''
len(string_1)        # 5
string_1 + ' World'  # Hello World
```

```{code-cell} ipython3
string_2 = "heLLo w0rlD"
string_2.replace("0", o)  # heLLo world
string_2.lower()          # hello w0rld
string_2.capitalize()     # HeLLo W0rld
```

```{code-cell} ipython3
string_3 = string_2.lower().capitalize().replace("0", "o") # Hello world

# Hello world
# 012345678910

string_3[6:] + " " + string_3[0:5] # World Hello
```

---

Eines der Probleme mit Strings als Datenstrukturen ist jedoch, dass sie unveränderlich sind. Um etwas zu ändern, müssen wir Kopien der Daten erstellen

```{code-cell} ipython3
:tags: [raises-exception]

string_3[1] = 'a'  # creates exception
```

---

## Datastructure

### `tuples`

`tuples` sind Bündel von Daten in strukturierter Form, und sie sind unveränderlich. Sie werden mit Klammern definiert `()`.

```{code-cell} ipython3
tuple_1 = (1.0, 2.0, 0.0)
tuple_2 = (3.0, 2.0, 4.0)

tuple_1[1]         # 2.0
tuple_1 + tuple_2  # (1.0, 2.0, 0.0, 3.0, 2.0, 4.0)
2*tuple_1          # (1.0, 2.0, 0.0, 1.0, 2.0, 0.0)
```

Gewisse Operationen können bei `tuples` **nicht** angewendet werden

```{code-cell} ipython3
:tags: [raises-exception]
tuple_1-tuple_2
tuple_1*tuple_2
tuple_1[1] = 2
```

### `lists`

Listen" sind flexibler als `tuples`, ihnen können Elemente zugewiesen oder entfernt werden. Es sind also veränderliche `tuples`. Sie werden mit Eckigen Klammern definiert `[]`. Sie können auch inneinander verschachtelt werden und die beinhalteten Datentypen können gemischt werden.

```{code-cell} ipython3
list_1 = [1.0, 2.0, 3.0]
list_2 = ['a', 'b', 'c']
list_3 = [1.0, 'a', (1, 2, 3), ['f', 'g', 'h']]
```

```{code-cell} ipython3
list_1[2]      # 3.0
list_2[-1]     # 'c'
list_3[3]      # ['f', 'g', 'h']
list_3[3][0]   # 'f'
```

```{code-cell} ipython3
2*list_1            # [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
list_+[0] = 0.0     #
list_1              # [0.0, 2.0, 3.0]
list_1.append(4.0)  # [0.0, 2.0, 3.0, 4.0]
list_2 += 'b'       # ['a', 'b', 'c', 'b']
list_2.remove('b')  # ['a', 'c', 'b']
```

Gewisse Operationen können bei `lists` **nicht** angewendet werden

```{code-cell} ipython3
:tags: [raises-exception]
2.0*list_1
```

### `sets`

`sets` sind spezielle listenähnliche Sammlungen von eindeutigen Elementen. Beachten Sie, dass die Elemente nicht geordnet sind (es gibt kein "s[1]").

```{code-cell} ipython3
set_1 = set([6, 5, 4, 2, 1, 1, 1, 1])
set_1         # {1, 2, 4, 5, 6}
set_1.add(7)  # {1, 2, 4, 5, 6, 7}
set_1.add(3)  # {1, 2, 3, 4, 5, 6, 7}
set_1.add(1)  # {1, 2, 3, 4, 5, 6, 7}

set_2 = set([5, 6, 7, 8, 9, 10, 11])

set_1.intersection(set_2) # {5, 6, 7}
set_1.union(set_2)        # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
```

### Dictionaries

Dies sind sehr nützliche Datensammlungen, in denen die Informationen anhand des Namens statt eines numerischen Indexes nachgeschlagen werden können. Dies ist als leichtgewichtige Datenbank sehr nützlich und wird häufig benötigt, wenn Module zum Einlesen von Daten verwendet werden.

```{code-cell} ipython3
dict_1 = { "item1": ['a', 'b', 'c'], "item2": ['c', 'd', 'e']}
dict_2 = {"Small Number":1.0, "Tiny Number":0.00000001, "Big Number": 100000000.0}
```

```{code-cell} ipython3
dict_1["item1"]      # ['a', 'b', 'c']
dict_1["item1"][1]   # 'b'

dict_2["Small Number"] + dict_2["Tiny Number"]  # 1.00000001
dict_2["Small Number"] + dict_2["Big Number"]   # 100000001.0

dict_2.keys()  # dict_keys(['Small Number', 'Tiny Number', 'Big Number'])

for k in dict_2.keys():
  print("{:>15s}".format(k), " --> ", dict_2[k])

# Small Number  -->  1.0
#  Tiny Number  -->  1e-08
#   Big Number  -->  100000000.0
```

Noch nützlicher ist die Tatsache, dass das Wörterbuch als Schlüssel alles haben kann, was mit der Funktion `hash` in eine eindeutige Zahl umgewandelt werden kann. Zeichenketten sinc pratkisch als Schlüssel, aber alles, was unveränderlich ist, kann gehasht werden:


+++ {"solution": "hidden"}

### Aufgabe: Erstellen einer Reverse-Lookup-Tabelle

Angenommen, Sie haben ein Wörterbuch mit Telefonnummern:

```python
phone_book = {"Rick Sanchez":    ("027", "374 92 97"),
              "Morty Smith":     ("079", "566 14 57"),
              "Richard Feynman": ("012", "345 67 89")
             }
```

Können Sie ein umgekehrtes Telefonbuch erstellen, um herauszufinden, wer von ihrer Telefonnummer aus anruft?

+++ {"solution": "shown", "solution_first": true}

__Lösung:__ Hier ist eine mögliche Lösung für die einfache Version des Problems, aber diese könnte noch eine Fehlerprüfung beinhalten (wenn man eine falsche Zahl eingibt)

```{code-cell} ipython3
:solution: shown
reverse_phone_book = {}
for key in phone_book.keys():
    reverse_phone_book[phone_book[key]] = key

reverse_phone_book
# {('027', '374 92 97'): 'Rick Sanchez',
#  ('079', '566 14 57'): 'Morty Smith',
#  ('012', '345 67 89'): 'Richard Feynman'}
```