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

# Types de données Python

Python peut être un peu étrange, car il offre de nombreux types de données, une attribution dynamique des types et quelques conversions automatiques.


## Nombres

Les nombres entiers, les nombres à virgule flottante et les nombres complexes sont automatiquement disponibles.

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

### Les nombres comme objets

Pratiquement tout en Python est un objet. Cela signifie que c'est une _chose_ qui peut avoir plusieurs copies et qui sait comment _exécuter_ certaines opérations sur elle-même.

Par exemple, un nombre à virgule flottante connaît certaines choses qu'il peut faire, plutôt que d'être simplement un nombre :

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

En des problèmes des chaînes de caractères en tant que structures de données est toutefois qu'elles sont immuables. Pour modifier quelque chose, nous devons créer des copies des données.

```{code-cell} ipython3
:tags: [raises-exception]

string_3[1] = 'a'  # creates exception
```

---

## Datastructure

### `tuples`

Les `tuples` sont des paquets de données sous forme structurée, et ils sont immuables. Ils sont définis avec des parenthèses `()`.

```{code-cell} ipython3
tuple_1 = (1.0, 2.0, 0.0)
tuple_2 = (3.0, 2.0, 4.0)

tuple_1[1]         # 2.0
tuple_1 + tuple_2  # (1.0, 2.0, 0.0, 3.0, 2.0, 4.0)
2*tuple_1          # (1.0, 2.0, 0.0, 1.0, 2.0, 0.0)
```

Certaines opérations ne peuvent pas être appliquées aux `tuples` **non**.

```{code-cell} ipython3
:tags: [raises-exception]
tuple_1-tuple_2
tuple_1*tuple_2
tuple_1[1] = 2
```

### `lists`

Les "listes" sont plus flexibles que les `tuples`, des éléments peuvent leur être attribués ou retirés. Ce sont donc des `tuples` modifiables. Elles sont définies avec des crochets `[]`. Elles peuvent aussi être imbriquées les unes dans les autres et les types de données qu'elles contiennent peuvent être mélangés.

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

Certaines opérations ne peuvent pas être appliquées aux `lists` **non**.

```{code-cell} ipython3
:tags: [raises-exception]
2.0*list_1
```

### `sets`

Les `sets` sont des collections spéciales d'éléments uniques, semblables à des listes. Notez que les éléments ne sont pas ordonnés (il n'y a pas de "s[1]").

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

Il s'agit de collections de données très utiles dans lesquelles les informations peuvent être recherchées à l'aide du nom plutôt que d'un index numérique. Ceci est très utile en tant que base de données légère et est souvent nécessaire lorsque des modules sont utilisés pour lire les données.

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

Plus utile encore est le fait que le dictionnaire peut avoir comme clé tout ce qui peut être transformé en un nombre unique avec la fonction `hash`. Les chaînes de caractères sinc pratkisch comme clés, mais tout ce qui est invariable peut être haché :


+++ {"solution": "hidden"}

### Tâche : Créer une table de recherche inverse

Supposons que vous disposiez d'un dictionnaire de numéros de téléphone :

```python
phone_book = {"Rick Sanchez":    ("027", "374 92 97"),
              "Morty Smith":     ("079", "566 14 57"),
              "Richard Feynman": ("012", "345 67 89")
             }
```

Pouvez-vous créer un annuaire inversé pour savoir qui appelle à partir de son numéro de téléphone ?

+++ {"solution": "shown", "solution_first": true}

__Solution:__ Voici une solution possible pour la version simple du problème, mais celle-ci pourrait encore inclure un contrôle d'erreur (si l'on saisit un chiffre erroné)

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