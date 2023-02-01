# Développement de l'ordinateur

Dans l'histoire de l'informatique, le concept de "programmation d'un ordinateur" a évolué rapidement, en liaison avec un développement rapide de la puissance de calcul, de la capacité de stockage et de la vitesse de communication. Il est utile de revenir sur cette évolution et de réfléchir aux aspects de la programmation informatique qui subsistent malgré tous ces changements.

Les améliorations rapides de la technologie informatique, qui font que la puissance de calcul double presque chaque année, nous semblent évidentes (cela est devenu connu sous le nom de loi de Moore {cite}`moore_cramming_2006`). Ce fait, plus que tout autre, a dicté la voie vers une pensée de plus en plus de haut niveau dans la création de programmes informatiques.

```{figure} img/moores-law.png
---
width: 100%.
nom : Loi de Moore
---
La loi de Moore stipule que la complexité des circuits intégrés double régulièrement ; selon les sources, la période mentionnée est de 12, 18 ou 24 mois.
```

Les premiers ordinateurs électroniques étaient chers et peu performants. Ils ne comprenaient qu'un ensemble rudimentaire d'instructions, et c'était une tâche très spécifique que d'écrire les instructions d'une tâche complexe qui pouvait résoudre un problème utile avec les ressources limitées de telles machines. L'ingéniosité était une condition importante pour un programmeur. L'effort humain pour concevoir soigneusement un programme était récompensé par des calculs rapides et sans erreur.

```{figure} img/turing-bombe.jpg
---
width: 50%
name: Bombe de Turing
---
La bombe imitait le fonctionnement de plusieurs machines Enigma reliées entre elles. Chacun des tambours tournant à grande vitesse, illustrés ci-dessus dans une réplique du musée de Bletchley Park, simulait le fonctionnement d'un rotor d'Enigma.
```


Au fur et à mesure que la puissance de calcul augmentait, les instructions qu'un ordinateur comprenait pouvaient être étendues. Ce n'était plus une perte de temps et d'argent que d'écrire des programmes informatiques sous une forme lisible par l'homme et de les faire traduire plus tard par l'ordinateur dans ses propres instructions, plus simples. La véritable programmation commence de cette manière : par la description des opérations à effectuer, sans qu'il soit nécessaire de connaître les détails sous-jacents de la machine qui effectue les calculs.

Il va sans dire que cette première étape abstraite a conduit à des abstractions de plus en plus poussées. Les programmes deviennent plus complexes et il peut être utile de faire un pas de plus jusqu'à ce que nous atteignions un niveau qui ne s'occupe pas des détails au sein d'un programme, mais qui le traite simplement comme un ensemble d'opérations qui traitent les informations de manière prévisible.  Une *bibliothèque*, *librairie* ou même *module* est une collection d'opérations qui effectuent un petit nombre de tâches pour plusieurs autres programmes.

La progression de la puissance des ordinateurs signifie que l'ordinateur prend en charge une plus grande partie du travail et permet à un programmeur d'envisager le problème à résoudre à un niveau beaucoup plus élevé. En outre, il est possible de créer et de réutiliser des bibliothèques très générales qui ont déjà été testées de manière approfondie. En règle générale, les bibliothèques ne posent pas de problème si elles font plus que ce dont nous avons besoin, ce qui signifie que nous ne devons pas modifier le code d'une bibliothèque au risque de le casser.

Nous pouvons au moins partir du principe que les logiciels (programmes) deviennent de plus en plus fiables et gagnent en fonctionnalité au fil du temps lorsqu'ils sont corrigés et améliorés par des humains, car ils peuvent toujours être réutilisés. Les améliorations du matériel rendent cela possible.

```{figure} img/apple-m1.jpg
---
width: 30%
name: M1
---
La puce M1 d'Apple possède 16 milliards de transistors fabriqués à l'échelle 5 nm. Elle exécute plusieurs threads différents sur une seule puce et possède de nombreux sous-systèmes qui étaient auparavant placés sur des puces séparées. Il n'est pas compatible avec les puces de la génération précédente (il utilise un jeu d'instructions différent au niveau binaire), mais il peut émuler ces puces si nécessaire, tout en conservant un certain avantage en termes de vitesse. Grâce à ses performances élevées et à sa grande capacité de mémoire, vous pouvez vous concentrer sur l'écriture de codes robustes et flexibles, sans avoir à vous soucier d'algorithmes intelligents spécialement conçus pour une architecture particulière. C'est le progrès !  (Image copyright : Apple, 2020)
```

Si le langage informatique dans lequel notre logiciel a été écrit n'est pas celui que nous utilisons, ce n'est pas grave, nous pouvons simplement écrire une sorte de traducteur et compenser les coûts supplémentaires liés à la progression de la vitesse du matériel et de la capacité de stockage. Il est même possible de créer soi-même des équivalents logiciels du matériel informatique. Ce qu'on appelle un *émulateur* permet à un programme de fonctionner partout et même de passer d'une machine à l'autre. C'est une autre forme de réutilisation : il est possible de recréer ou de cloner à tout moment une machine en fonctionnement et d'obtenir à chaque fois des résultats identiques.