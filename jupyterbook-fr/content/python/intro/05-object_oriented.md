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

# Programmation orientée objet

Python est un langage orienté objet. Nous avons brièvement mentionné que les objets sont des unités autonomes qui regroupent des données et des fonctions. Nous avons également abordé la manière dont nous pouvons avoir plusieurs copies d'objets. Presque tout en Python est un objet.

La programmation orientée objet se compose de 4 éléments de base. Les 4 éléments sont expliqués ci-dessous à l'aide de pokémons.

```{figure} img/pillars-of-oop.svg
---
width: 60%
name: piliers de l'oop
---
4 piliers de la programmation orientée objet
```

## Classes

Tout d'abord, qu'est-ce qu'une classe ? C'est un ensemble de données (attributs) et de fonctions (méthodes) associées. Un objet est une instance d'une classe.

```{figure} img/pokemon-explanation.svg
---
width: 100%
nom: pokemon explanation
---
Classe et objet Pokemon
```

```{code-cell} ipython3
class Pokemon :
  def __init__(self, name=None, type=None, health=None, attack=None, defense=None) :
    self.__name = nom
    self.__type = type
    self.__health = santé
    self.__attack = attaque
    self.__defense = defense
    print(self.speak())

  def speak(self) :
    print(self.__name)

  def attack(self) :
    return(self.__attack)

  def dodge(self, attack) :
    self.__health -= attaque - self.__defense
    return((attack - self.__defense) *-1)

  def evolve(self, new_ame) :
    self.__name = new_name
    return(self.__nom)

pikachu = Pokemon("Pikachu", "Electric", 3, 4, 3)
```

1. `self` est la référence à soi-même. Avec ce pointeur, la classe peut accéder à ses propres éléments.
2. la fonction `__init__` est ce qu'on appelle une contructure. Dès que l'on crée la classe avec `Pokemon(...)`, le constructeur est appelé.

## Abstraction (Abstraction)
L'abstraction consiste à ne montrer à l'utilisateur que les détails nécessaires. Pour revenir à notre exemple avec le pokemon : Nous n'avons pas besoin de savoir ce qui se passe à l'intérieur si un `dodge()` est exécuté. Nous voulons simplement initier l'action. C'est exactement cela l'abstraction : nous ne révélons que les détails nécessaires et masquons les informations non pertinentes.

```{code-cell} ipython3
class Pokemon :
  ...

  def dodge(self, attack) :
    self.__health -= attaque - self.__defense
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

## Encapsulation (Encapuslation)
L'encapsulation consiste à regrouper les données et les méthodes dans une seule unité, comme une classe. Elle est également basée sur l'idée du data hiding. Les variables d'une classe sont cachées aux autres classes et ne peuvent être appelées que par les méthodes de leur classe actuelle. Cela sert avant tout à la sécurité, afin d'éviter de modifier par inadvertance une propriété d'un objet. Nous encapsulons nos propriétés au sein de l'objet en rendant nos propriétés privées. Nous pouvons fournir des méthodes Setter et Getter publiques pour modifier certaines propriétés d'une classe.

Les variables privées sont définies en Python avec le préfixe `__`. Toutes les variables de la classe Pokemon sont privées et ne peuvent pas être accédées de l'extérieur. Les valeurs des variables ne peuvent être modifiées qu'à l'aide de fonctions. Dans ce cas, avec les fonctions `__init__()``, ``dodge()`et `evolve()`.

```{code-cell} ipython3
class Pokemon :
  def __init__(self, name=None, type=None, health=None, attack=None, defense=None) :
    self.__name = nom
    self.__type = type
    self.__health = santé
    self.__attack = attaque
    self.__defense = defense
    print(self.speak())

  def dodge(self, attack) :
    self.__health -= attaque - self.__defense
    return((attack - self.__defense) *-1)

  def evolve(self, new_ame) :
    self.__name = new_name
    return(self.__nom)

  ...

pikachu = Pokemon("Pikachu", "Electric", 3, 4, 3)
```

## Héritage (Inheritance)
L'héritage signifie que les propriétés sont transmises d'une classe parente à une classe enfant. La classe parente est la classe de base, qui dispose de toutes les propriétés et méthodes de base. La classe enfant dispose des mêmes propriétés et méthodes de la classe parente, en plus de ses propres propriétés ou méthodes. Cela permet de réutiliser, d'adapter et d'améliorer le code existant.

```{figure} img/pokemon-explanation-2.svg
---
width: 100%
name: pokemon explanation 2
---
Héritage Pokemon
```

```{code-cell} ipython3
class ElectricPokemon(Pokemon) :
  def __init__(self, name=None, health=None, attack=None, defense=None, special_attack=None) :
    super().__init__(nom, "Electric", health, attack, defense)
    self.__attaque_spéciale = attaque_spéciale
    print(self.speak())

  def speak(self) :
    print("Zap " + self.__name)

    def special_attack(self) :
    return(self.__special_attack)

class FirePokemon(Pokemon) :
  def __init__(self, name=None, health=None, attack=None, defense=None, special_attack=None) :
    super().__init__(nom, "Fire", health, attack, defense)
    self.__attaque_spéciale = attaque_spéciale
    print(self.speak())

  def speak(self) :
    print("Siffler " + self.__nom)

    def special_attack(self) :
    return(self.__attaque_spéciale)

class WaterPokemon(Pokemon) :
  def __init__(self, name=None, health=None, attack=None, defense=None, special_attack=None) :
    super().__init__(nom, "Water", health, attack, defense)
    self.__attaque_spéciale = attaque_spéciale
    print(self.speak())

  def speak(self) :
    print("Blub " + self.__name)

    def special_attack(self) :
    return(self.__attaque_spéciale)


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

## Polymorphisme (Polymorphism)
Le polymorphisme signifie qu'une classe subordonnée peut définir son propre comportement unique tout en utilisant les mêmes méthodes ou le même comportement que sa classe parente. Pensons à notre classe parente `Pokemon` et à nos `Pokemon de l'eau`. Cette classe `Pokemon` a une méthode `speak()` qui donne le nom du Pokemon. Cette méthode est héritée de la classe `PokemonEau` et y est adaptée. En plus du nom, un `WaterPokemon` fait des bulles ? c'est pourquoi `blub` est ajouté. Un autre avantage du polymorphisme est que la classe parente ne change pas en cas de modification dans la classe subordonnée. Même si nous avons modifié la méthode `speak()` du `PokemonEau` en `"blub" + self.name"`, le Pokemon continuera à n'afficher que son nom. Le polymorphisme permet un comportement spécifique à la classe et davantage de code réutilisable.


```
class WaterPokemon(Pokemon) :
  ...

  def speak(self) :
    print("Blub " + self.__name)

  ...
```
