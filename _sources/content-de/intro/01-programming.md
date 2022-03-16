# Moderne Ansätze zur Programmierung

Die moderne Programmierung hat einen organischen, vielschichtigen Charakter, der Sie vielleicht überraschen wird. In diesem Kurs werden wir lernen, wie man diese Schichten durchschaut, um zu verstehen, wie Programme aufgebaut sind und wie wir unsere eigenen Programme erstellen können. Beginnen wir mit einigen sehr grundlegenden Fragen.

## Was ist ein Computer?

Ein klassischer Computer ist eine Art Maschine zur Verarbeitung reiner Informationen. Um dies zu ermöglichen, sind verschiedene Komponenten erforderlich, darunter Mittel zur Initialisierung und Speicherung der Informationen vor und nach ihrer Verarbeitung sowie ein Mechanismus zur Verarbeitung von Informationen (einschliesslich des Falles, dass die Verarbeitung von den Informationen selbst abhängt). Viele verschiedene Maschinen können diese Kriterien erfüllen, aber wir fügen in der Regel mindestens eine weitere Anforderung hinzu: Die Computer, an denen wir interessiert sind, sind *programmierbar*, d. h. sie können mit verschiedenen Anweisungen versehen werden, die beschreiben, welche Verarbeitung durchgeführt wird.

Die ursprüngliche **Analytische Maschine**, die von Babbage und Lovelace in den 1830er Jahren entwickelt wurde (siehe {cite}`babbage_babbages_2010`), erfüllt diese Kriterien, ebenso wie die meisten modernen Digitalcomputer. Einer der Pioniere der Informationstheorie, John von Neumann, beschreibt die notwendigen Voraussetzungen für einen echten Computer und stellt in seinem letzten Buch *Computing and the Brain* viele sehr interessante Vergleiche zwischen den digitalen Computern seiner Zeit (den 1950er Jahren) und dem menschlichen Gehirn an
{cite}`von_neumann_computer_2012`.

```{figure} img/baggages-analytical-engine.jpg
---
width: 40%
name: Baggage's Analytical Engine
---
Baggae's Analytical Engine (Bild quelle: Wikipedia)
```

Es gibt viele Arten von Computern, auf die wir nicht eingehen werden, wie z. B. eingebettete Systeme in Steuerungen, Motoren, Autos, Flugzeugen usw. Einige von ihnen verwenden vielleicht eine vergleichbare Programmierung, aber viele sind stark Optimiert, damit sie schnell, mit geringem Overhead und ohne Gefahr eines Absturzes erledigen Ihre Aufgabe erledigen können, da sie wichtige Informationen in Echtzeit verarbeiten. Diese Systeme haben vielleicht mehr mit den frühen elektronischen Computern gemeinsam, denn Komplexität kann der Feind der Zuverlässigkeit sein.

Wir gehen auch davon aus, dass wir jeweils nur eine einzige Informationsverarbeitungsmaschine programmieren. Bei den meisten Computern handelt es sich in Wirklichkeit um mehrere Verarbeitungsmaschinen, die gleichzeitig entweder an verschiedenen Aufgaben arbeiten, die nicht miteinander interagieren, oder an Teilmengen der Informationen, die voneinander isoliert sind. Echte Parallelprogrammierung erfordert fast immer, dass wir verstehen und kontrollieren, wie diese Daten- oder Aufgabeninterdependenzen funktionieren, und das ist ein Thema für sich.

## Was ist eine Programmiersprache?

Allgemein gesprochen ist eine Programmiersprache eine Methode, um einem Computer mitzuteilen, wie er Informationen für uns beschaffen und verarbeiten soll. In der Programmierung gibt es zwei verschiedene Paradigmen, die Probleme auf ganz unterschiedliche Weise angehen.

Das erste ist der **deklarative** Ansatz, der angibt, was getan werden muss, aber nicht viel darüber sagt, wie es getan werden muss. Einige Beispiele dafür sind "Hey Siri ..." oder "Hey Google ...", gefolgt von einer Frage wie "Wird es heute heiss?" und wir erwarten darauf eine vernünftige Antwort ohne weitere Erklärung. Ein weiteres Beispiel ist eine Tabellenkalkulation, in der Berechnungen meist einfach durchgeführt werden, ohne dass im Detail erklärt werden muss, wie man eine Spalte summiert oder zwei Spalten multipliziert. Dies ist auch die Art und Weise, wie wir normalerweise mit menschlichen Experten interagieren!

Das zweite Paradigma ist uns im Alltag meist weniger vertraut. Beim **imperativen** Programmieren legt man dem Computer jeden Schritt im Detail vor, und diese Schritte werden *genau* befolgt, ganz gleich, welche Fehler man bei der Erteilung der Anweisungen macht. Wir geben Leuten auf dieser Ebene keine Anweisungen, es sei denn, sie haben keinerlei Erfahrung auf einem bestimmten Gebiet. Aus "Würden Sie mir bitte eine Tasse Tee machen?" wird "Gehen Sie von Ihrer jetzigen Position in die Küche und suchen Sie den Wasserkocher, stellen Sie den An/Aus-Schalter auf "An" ... " und so weiter. Jeder dieser Schritte ist anfällig für Fehlinterpretationen und Missverständnisse. Woher wissen Sie also, wann Sie aufhören sollten, weitere Details hinzuzufügen?

Die meisten wissenschaftlichen Probleme werden wir mit Hilfe der imperativen Programmierung angehen, aber wir werden auch viele Bibliotheken und Module nutzen, die die grundlegenden Anweisungen für die Art von Aufgaben, die wir erledigen wollen, bereits *kodiert* haben. Unsere Aufgabe besteht oft nur darin, unser Bestes zu geben, um diese Bibliotheken zu finden, sie zu testen und herauszufinden, was sie alles tun können. Die vielen Abstraktionsschichten sind eine Möglichkeit, den angemessenen Detaillierungsgrad bei der Beschreibung einer Aufgabe zu finden.

Eine Programmiersprache ist lediglich eine Möglichkeit, das Schreiben und Ausführen dieser Anweisungen so einfach und wiederverwendbar zu machen, wie es für die jeweilige Aufgabe sinnvoll ist. Einige sind sehr einfach, um einzelne Chips zu programmieren, und andere sind sehr anspruchsvoll, wenn wir zum Beispiel eine interaktive Website schnell und grösstenteils nach einem bereits vorhandenen Rezept erstellen wollen. Einige Programmiersprachen tauschen Benutzerfreundlichkeit gegen Geschwindigkeit (Sprachen wie `C` und `Fortran` sind so), und andere sind sehr flexibel, müssen aber beim Ausführen eine Menge Prüfungen durchführen, um sicherzustellen, dass alle Ideen konsistent zusammenpassen (`Python` ist so, sowie auch `Perl`). Einige Programmiersprachen sind nur Anordnungen von logischen Blöcken, in denen wir die Operationen und ihre Wechselwirkungen spezifizieren, diese aber nicht in Textform beschreiben (z. B. `scratch`), aber sie erklären immer noch auf einer gewissen Ebene, was zu tun ist, in welcher Reihenfolge und mit welchen Teilen von Daten.

Wir werden uns auf `Python konzentrieren, eine flexible Sprache, die in der wissenschaftlichen Gemeinschaft weit verbreitet ist. Sie hat mit dem Englischen insofern einiges gemeinsam, als sie Konzepte aus anderen Sprachen sehr gut aufnehmen kann und es immer viele verschiedene Möglichkeiten gibt, etwas zu beschreiben. Python ermöglicht es, Abstraktionsebenen zu schaffen, die unwichtige Details verbergen, aber diese Details sind nicht besonders gut versteckt und es ist immer möglich, tiefer zu graben und mehr herauszufinden.

## Wie sieht ein gut geschriebenes Programm oder eine gut geschriebene Bibliothek aus?

Eine der ersten Fragen, die man sich stellen sollte, bevor man mit dem Schreiben von Code beginnt, ist: "Hat das schon jemand geschrieben?", und wenn die Antwort ja lautet, können Sie schnell herausfinden, welche der folgenden Optionen am besten ist:

* Das vorhandene Programm oder die vorhandene Bibliothek verwenden
* Ändern Sie das vorhandene Programm oder die vorhandene Bibliothek
* Neu anfangen

Wenn Sie sich dafür entscheiden, den Code eines anderen zu verwenden, müssen Sie verstehen, wie er funktioniert, und überprüfen, ob er auch wirklich so funktioniert, wie er angekündigt wurde. Wenn Sie den Code ändern müssen, sollten Sie überlegen, ob Sie diese Verbesserungen dem Autor oder der Gemeinschaft zur Verfügung stellen wollen.

Diesen Prozess für den Code eines anderen zu durchlaufen, ist auch eine sehr gute Idee, bevor Sie Ihren eigenen Code schreiben, denn ehrlich gesagt, hilft es Ihnen, Ihre eigene Arbeit genauso kritisch zu sehen wie die anderer. Die folgende Checkliste wirkt viel einschüchternder, wenn Sie sich vorstellen, dass Sie Ihre eigenen Programme prüfen und nicht die von jemand anderem:

* Kann ich den Quellcode finden?
* Ist der Quellcode klar, lesbar und kommentiert?
* Gibt es eine Reihe von Tests mit einer guten Abdeckung des Codes?
* Gibt es Benchmarks oder Überprüfungen von Eingaben und Ausgaben?
* Gibt es eine klare Dokumentation für einen typischen Benutzer oder einen typischen Entwickler?
* Ist klar, wie Fehlerbehebungen und Verbesserungen angenommen werden?
* Ist der Code für die neuesten Betriebssysteme aktuell?

Die bisherige Diskussion hat uns an einen Punkt gebracht, an dem wir wissen, wie wir beschreiben können, was wir von einer Software wollen, auch wenn wir nicht wissen, wie wir sie selbst bauen können! Wir werden Sie ermutigen, jede Aufgabe von dieser hohen Ebene aus anzugehen. Wir werden immer mit der Frage beginnen - hat das schon jemand gemacht?

## Wie arbeiten wir in einer Welt der wiederverwendbaren Datenverarbeitung?

Unser Ziel ist es, nicht nur zu lernen, wie man einen Computer programmiert, sondern auch, wie man Software schreibt, die funktioniert und mit allen Tests versehen ist, die beweisen, dass sie funktioniert; Dies bedeutet Software, die andere Menschen hilfreich sein kann und diese ermutigt, sie zu benutzen.
Das heisst, Software, die nach den gerade besprochenen Kriterien "gut geschrieben" ist.

Wir werden uns mit *literatem Programmieren* befassen, das eine Möglichkeit darstellt, eine umfangreiche Dokumentation (mit vollständigem Text, Gleichungen, Bildern usw.) in den Code zu integrieren, so dass dieser automatisch gut erklärt und ordnungsgemäss dokumentiert wird, und auch sicherzustellen, dass die Dokumentation und der Code nicht auseinanderdriften, wenn Änderungen vorgenommen werden.

Wir werden die Vorteile von Open-Source-Codes und deren Bereitstellung in einem öffentlichen Repository erörtern, so dass sie leicht auffindbar sind. Wir werden die Versionskontrolle und das Testen besprechen und die Vorteile der Zusammenführung dieser beiden Dinge in einen Prozess, so dass Sie sicher sein können, dass jede Änderung, die Sie am Code vornehmen, keine Fehler in andere Teile des Codes hervorruft.
