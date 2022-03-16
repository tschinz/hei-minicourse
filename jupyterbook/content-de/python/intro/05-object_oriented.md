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

# Objektorientierte Programmierung

Python ist eine objektorientierte Sprache. Wir haben kurz erwähnt, dass Objekte in sich geschlossene Einheiten sind, die Daten und Funktionen bündeln. Wir haben auch besprochen, wie wir mehrere Kopien von Objekten haben können. So gut wie alles in Python ist ein Objekt.

Die Ojektorientierte Programmierung besteht aus 4 Grundpfeilern. Alle 4 Elemente werden mi hilfe von Pokemons unten erläutert.

```{figure} img/pillars-of-oop.svg
---
width: 60%
name: pillars of oop
---
4 Säulen der Objektorientierten Programmierung
```

## Klassen

Zuerst aber was ist eine Klasse, es ist eine Ansammlung von Daten (Attributen) und dazugehörende Funktionen (Methods). Ein Objekt ist eine Instanz einer Klassen.

```{figure} img/pokemon-explanation.svg
---
width: 100%
name: pokemon explanation
---
Pokemon Klasse und Objekt
```

```{code-cell} ipython3
class Pokemon:
  def __init__(self, name=None, type=None, health=None, attack=None, defense=None):
    self.__name    = name
    self.__type    = type
    self.__health  = health
    self.__attack  = attack
    self.__defense = defense
    print(self.speak())

  def speak(self):
    print(self.__name)

  def attack(self):
    return(self.__attack)

  def dodge(self, attack):
    self.__health -= attack - self.__defense
    return((attack - self.__defense) *-1)

  def evolve(self, new_ame):
    self.__name = new_name
    return(self.__name)

pikachu = Pokemon("Pikachu", "Electric", 3, 4, 3)
```

1. `self` ist die Referenz auf sich selber. Mit diesem Pointer kann die Klasse auf eigene Elemente zugreifen.
2. Die Funktion `__init__` ist eine sogenannter Konstruktur. Sobald man die Klasse erstellt mit `Pokemon(...)` wir der Konstruktor aufgerufen.

## Abstaktion (Abstraction)
Abstraktion bedeutet, dem Benutzer nur die notwendigen Details zu zeigen. Um auf unser Beispiel mit dem Pokemon zurückzukommen: Wir müssen nicht wissen, was im Inneren vor sich geht, falls ein `dodge()` ausgeführt wird. Wir wollen einfach nur die Aktion initiieren. Genau das ist Abstraktion: Wir legen nur die notwendigen Details offen und blenden die irrelevanten Informationen aus.

```{code-cell} ipython3
class Pokemon:
  ...

  def dodge(self, attack):
    self.__health -= attack - self.__defense
    return((attack - self.__defense) *-1)

  ...

pikachu = Pokemon("Pikachu", "Electric", 3, 4, 3)
pikachu.dodge(4)
```
---
```
Pikachu
-1
```

## Verkapselung (Encapuslation)
Verkapselung bedeutet, dass Daten und Methoden in einer einzigen Einheit wie einer Klasse zusammengefasst werden. Sie basiert auch auf der Idee des Data Hiding. Die Variablen einer Klasse werden vor anderen Klassen verborgen und können nur über die Methoden ihrer aktuellen Klasse aufgerufen werden. Dies dient vor allem der Sicherheit, damit nicht versehentlich eine Eigenschaft eines Objekts verändert wird. Wir kapseln unsere Eigenschaften innerhalb des Objekts ein, indem wir unsere Eigenschaften auf privat setzen. Wir können öffentliche Setter- und Getter-Methoden bereitstellen, um bestimmte Eigenschaften einer Klasse zu ändern.

Private Variablen werden in Python mit dem Prefix `__` definiert. Alle Variablen in der Pokemon Klasse sind Privat und können nicht von aussen Zugegriffen werden. Die Werte der Variablen werden nur mit Hilfe von Funktionen verändert. In diesem Fall mit den Funktionen `__init__()``, ``dodge()`sowie `evolve()`.

```{code-cell} ipython3
class Pokemon:
  def __init__(self, name=None, type=None, health=None, attack=None, defense=None):
    self.__name    = name
    self.__type    = type
    self.__health  = health
    self.__attack  = attack
    self.__defense = defense
    print(self.speak())

  def dodge(self, attack):
    self.__health -= attack - self.__defense
    return((attack - self.__defense) *-1)

  def evolve(self, new_ame):
    self.__name = new_name
    return(self.__name)

  ...

pikachu = Pokemon("Pikachu", "Electric", 3, 4, 3)
```

## Vererbung (Inheritance)
Vererbung bedeutet, dass Eigenschaften von einer Elternklasse an eine Kindklasse weitergegeben werden. Die übergeordnete Klasse ist die Basisklasse, die über alle grundlegenden Eigenschaften und Methoden verfügt. Die untergeordnete Klasse verfügt über dieselben Eigenschaften und Methoden der übergeordneten Klasse, zusätzlich zu ihren eigenen Eigenschaften oder Methoden. Dies hilft bei der Wiederverwendung, Anpassung und Verbesserung des vorhandenen Codes.

```{figure} img/pokemon-explanation-2.svg
---
width: 100%
name: pokemon explanation 2
---
Pokemon Vererbung
```

```{code-cell} ipython3
class ElectricPokemon(Pokemon):
  def __init__(self, name=None, health=None, attack=None, defense=None, special_attack=None):
    super().__init__(name, "Electric", health, attack, defense)
    self.__special_attack = special_attack
    print(self.speak())

  def speak(self):
    print("Zap " + self.__name)

    def special_attack(self):
    return(self.__special_attack)

class FirePokemon(Pokemon):
  def __init__(self, name=None, health=None, attack=None, defense=None, special_attack=None):
    super().__init__(name, "Fire", health, attack, defense)
    self.__special_attack = special_attack
    print(self.speak())

  def speak(self):
    print("Zisch " + self.__name)

    def special_attack(self):
    return(self.__special_attack)

class WaterPokemon(Pokemon):
  def __init__(self, name=None, health=None, attack=None, defense=None, special_attack=None):
    super().__init__(name, "Water", health, attack, defense)
    self.__special_attack = special_attack
    print(self.speak())

  def speak(self):
    print("Blub " + self.__name)

    def special_attack(self):
    return(self.__special_attack)


pikachu = ElectricPokemon("Pikachu", 3, 4, 3, 3)
charmander = FirePokemon("Charmander", 3, 4, 3, 4)
squirtle = WaterPokemon("Squirtle", 3, 3, 4, 3)
```
---
```
Zap Pikachu
Zisch Charmander
Blub Squirtle
```

## Polymorphismus (Polymorphism)
Polymorphismus bedeutet, dass eine untergeordnete Klasse ihr eigenes, einzigartiges Verhalten definieren und dennoch die gleichen Methoden oder das gleiche Verhalten der übergeordneten Klasse nutzen kann. Denken wir an unsere Elternklasse `Pokemon` und unsere `WaterPokemon`. Diese `Pokemon`-Klasse hat eine `speak()`-Methode, die den Namen des Pokemons ausgiebt. Diese Methode wird an die Klasse `WaterPokemon` vererbt und dort angepasst. Zusätzlich zum Namen blubbert ein `WaterPokemon`? deshalb wird `blub` agnehängt. Ein weiterer Vorteil der Polymorphie besteht darin, dass sich die übergeordnete Klasse durch eine Änderung in der untergeordneten Klasse nicht ändert. Auch wenn wir die `speak()`-Methode des `WaterPokemon`s in `"blub" + self.name"` geändert haben, wird das Pokemon weiterhin nur seinen Namen ausgeben. Polymorphismus ermöglicht ein klassenspezifisches Verhalten und mehr wiederverwendbaren Code.


```
class WaterPokemon(Pokemon):
  ...

  def speak(self):
    print("Blub " + self.__name)

  ...
```
