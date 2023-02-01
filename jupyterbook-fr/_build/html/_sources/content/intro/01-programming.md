# Approches modernes de la programmation

La programmation moderne a un caractère organique et multi-couches qui pourrait vous surprendre. Dans ce cours, nous allons apprendre à voir à travers ces couches pour comprendre comment les programmes sont construits et comment nous pouvons créer nos propres programmes. Commençons par quelques questions très basiques.

## Qu'est-ce qu'un ordinateur ?

Un ordinateur classique est une sorte de machine destinée à traiter des informations pures. Pour que cela soit possible, différents composants sont nécessaires, notamment des moyens d'initialisation et de stockage des informations avant et après leur traitement, ainsi qu'un mécanisme de traitement des informations (y compris dans le cas où le traitement dépend des informations elles-mêmes). De nombreuses machines différentes peuvent répondre à ces critères, mais nous y ajoutons généralement au moins une exigence supplémentaire : les ordinateurs qui nous intéressent sont *programmables*, c'est-à-dire qu'ils peuvent être dotés de différentes instructions décrivant quel traitement est effectué.

La **machine analytique** originale, développée par Babbage et Lovelace dans les années 1830 (voir {cite}`babbage_babbages_2010`), répond à ces critères, tout comme la plupart des ordinateurs numériques modernes. L'un des pionniers de la théorie de l'information, John von Neumann, décrit les conditions nécessaires à un véritable ordinateur et fait de nombreuses comparaisons très intéressantes entre les ordinateurs numériques de son époque (les années 1950) et le cerveau humain dans son dernier livre *Computing and the Brain*.
{cite}`von_neumann_computer_2012`.

```{figure} img/baggages-analytical-engine.jpg
---
width: 40%
name: Moteur analytique de Baggage
---
Baggae's Analytical Engine (image source : Wikipedia)
```

Il existe de nombreux types d'ordinateurs que nous n'aborderons pas, comme les systèmes embarqués dans les commandes, les moteurs, les voitures, les avions, etc. Certains d'entre eux utilisent peut-être une programmation comparable, mais beaucoup sont fortement optimisés pour accomplir leur tâche rapidement, avec peu de frais généraux et sans risque de crash, car ils traitent des informations importantes en temps réel. Ces systèmes ont peut-être plus en commun avec les premiers ordinateurs électroniques, car la complexité peut être l'ennemi de la fiabilité.

Nous partons également du principe que nous ne programmons qu'une seule machine de traitement de l'information à la fois. En réalité, la plupart des ordinateurs sont des machines de traitement multiples qui travaillent simultanément soit sur des tâches différentes qui n'interagissent pas entre elles, soit sur des sous-ensembles d'informations qui sont isolés les uns des autres. La véritable programmation parallèle exige presque toujours que nous comprenions et contrôlions le fonctionnement de ces interdépendances de données ou de tâches, et c'est un sujet en soi.

## Qu'est-ce qu'un langage de programmation ?

D'une manière générale, un langage de programmation est une méthode permettant d'indiquer à un ordinateur comment obtenir et traiter des informations pour nous. En programmation, il existe deux paradigmes différents qui abordent les problèmes de manière très différente.

Le premier est l'approche **déclarative**, qui indique ce qui doit être fait, mais ne dit pas grand-chose sur la manière de le faire. Quelques exemples sont "Hey Siri ..." ou "Hey Google ...", suivis d'une question comme "Est-ce qu'il va faire chaud aujourd'hui ?" et nous attendons une réponse raisonnable à cette question, sans autre explication. Un autre exemple est celui d'un tableur, dans lequel les calculs sont généralement effectués simplement, sans qu'il soit nécessaire d'expliquer en détail comment additionner une colonne ou multiplier deux colonnes. C'est aussi la manière dont nous interagissons habituellement avec des experts humains !

Le deuxième paradigme nous est généralement moins familier dans la vie quotidienne. Dans la programmation **impérative**, on donne à l'ordinateur le détail de chaque étape, et ces étapes sont suivies *exactement*, quelles que soient les erreurs que l'on commet en donnant les instructions. Nous ne donnons pas d'instructions aux personnes de ce niveau, à moins qu'elles n'aient aucune expérience dans un domaine particulier. Le "Pourriez-vous me préparer une tasse de thé ?" devient "Allez dans la cuisine depuis votre position actuelle et trouvez la bouilloire, mettez l'interrupteur marche/arrêt sur "On" ... " et ainsi de suite. Chacune de ces étapes est sujette à des interprétations erronées et à des malentendus. Alors, comment savoir quand arrêter d'ajouter des détails ?

Nous aborderons la plupart des problèmes scientifiques à l'aide de la programmation impérative, mais nous utiliserons également de nombreuses bibliothèques et modules qui ont déjà *encodé* les instructions de base pour le type de tâches que nous voulons accomplir. Notre tâche consiste souvent simplement à faire de notre mieux pour trouver ces bibliothèques, les tester et découvrir tout ce qu'elles peuvent faire. Les nombreuses couches d'abstraction sont un moyen de trouver le niveau de détail approprié pour décrire une tâche.

Un langage de programmation est simplement un moyen de rendre l'écriture et l'exécution de ces instructions aussi simples et réutilisables que possible pour la tâche en question. Certains sont très simples pour programmer des puces individuelles, et d'autres sont très sophistiqués si nous voulons, par exemple, créer un site web interactif rapidement et en grande partie à partir d'une recette déjà existante. Certains langages de programmation échangent la facilité d'utilisation contre la vitesse (c'est le cas de langages tels que C et Fortran), et d'autres sont très flexibles, mais doivent effectuer de nombreuses vérifications lors de l'exécution pour s'assurer que toutes les idées sont cohérentes entre elles (c'est le cas de Python et de Perl). Certains langages de programmation ne sont que des arrangements de blocs logiques dans lesquels nous spécifions les opérations et leurs interactions, mais ne les décrivent pas sous forme de texte (par ex. `scratch`), mais ils expliquent toujours à un certain niveau ce qu'il faut faire, dans quel ordre et avec quelles parties de données.

Nous allons nous concentrer sur Python, un langage flexible largement utilisé dans la communauté scientifique. Il a des points communs avec l'anglais dans la mesure où il peut très bien intégrer des concepts d'autres langues et qu'il y a toujours de nombreuses façons différentes de décrire quelque chose. Python permet de créer des niveaux d'abstraction qui cachent des détails sans importance, mais ces détails ne sont pas particulièrement bien cachés et il est toujours possible de creuser plus profondément et d'en découvrir davantage.

## À quoi ressemble un programme ou une bibliothèque bien écrits ?

L'une des premières questions à se poser avant de commencer à écrire du code est : "Quelqu'un l'a-t-il déjà écrit ?", et si la réponse est oui, vous pouvez rapidement déterminer laquelle des options suivantes est la meilleure :

* Utiliser le programme ou la bibliothèque existante.
* Modifier le programme ou la bibliothèque existante
* Recommencer à zéro

Si vous décidez d'utiliser le code de quelqu'un d'autre, vous devez comprendre comment il fonctionne et vérifier qu'il fonctionne comme il a été annoncé. Si vous devez modifier le code, vous devez vous demander si vous souhaitez mettre ces améliorations à la disposition de l'auteur ou de la communauté.

Passer par ce processus pour le code de quelqu'un d'autre est également une très bonne idée avant d'écrire votre propre code, car honnêtement, cela vous aide à voir votre propre travail de manière aussi critique que celui des autres. La liste de contrôle suivante semble beaucoup plus intimidante si vous imaginez que vous examinez vos propres programmes et non ceux de quelqu'un d'autre :

* Puis-je trouver le code source ?
* Le code source est-il clair, lisible et commenté ?
* Y a-t-il une série de tests avec une bonne couverture du code ?
* Y a-t-il des benchmarks ou des vérifications des entrées et des sorties ?
* Y a-t-il une documentation claire pour un utilisateur ou un développeur typique ?
* La façon dont les corrections de bugs et les améliorations sont acceptées est-elle claire ?
* Le code est-il à jour pour les systèmes d'exploitation les plus récents ?

La discussion menée jusqu'à présent nous a permis d'arriver à un point où nous savons comment décrire ce que nous voulons d'un logiciel, même si nous ne savons pas comment le construire nous-mêmes ! Nous vous encouragerons à aborder chaque tâche à partir de ce niveau élevé. Nous commencerons toujours par la question - quelqu'un l'a-t-il déjà fait ?

## Comment travaillons-nous dans un monde de traitement de données réutilisables ?

Notre objectif est d'apprendre non seulement à programmer un ordinateur, mais aussi à écrire des logiciels qui fonctionnent et qui sont accompagnés de tous les tests prouvant qu'ils fonctionnent ; Cela signifie des logiciels qui peuvent être utiles à d'autres personnes et qui les encouragent à les utiliser.
C'est-à-dire un logiciel qui est "bien écrit" selon les critères que nous venons d'aborder.

Nous aborderons la *programmation littérale*, qui est un moyen d'intégrer une documentation complète (avec du texte intégral, des équations, des images, etc.) dans le code, de sorte que celui-ci soit automatiquement bien expliqué et correctement documenté, et de s'assurer également que la documentation et le code ne dérivent pas lorsque des modifications sont apportées.

Nous aborderons les avantages du code open source et de sa mise à disposition dans un référentiel public afin qu'il soit facile à trouver. Nous aborderons le contrôle de version et les tests, ainsi que les avantages de réunir ces deux choses en un seul processus, de sorte que vous puissiez être sûr que toute modification que vous apportez au code n'entraîne pas d'erreurs dans d'autres parties du code.
