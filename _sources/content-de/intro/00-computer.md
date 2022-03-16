# Computer Entwicklung

In der Geschichte der Informatik hat sich das Konzept des "Programmierens eines Computers" in Verbindung mit einer rasanten Entwicklung der Rechenleistung, der Speicherkapazität und der Kommunikationsgeschwindigkeit schnell entwickelt. Es ist hilfreich, auf diese Entwicklung zurückzublicken und über die Aspekte der Computerprogrammierung nachzudenken, die bei all diesen Veränderungen bestehen bleiben.

Die rasanten Verbesserungen in der Computertechnologie, die dazu führen, dass sich die Rechenleistung fast jedes Jahr verdoppelt, sind für uns selbstverständlich (dies ist als Moore's Law {cite}`moore_cramming_2006` bekannt geworden). Diese Tatsache hat mehr als alles andere den Weg zu mehr und mehr High-Level-Denken bei der Erstellung von Computerprogrammen diktiert.

```{figure} img/moores-law.png
---
width: 100%
name: Moores Law
---
Das mooresche Gesetz besagt, dass sich die Komplexität integrierter Schaltkreise regelmäßig verdoppelt; je nach Quelle werden 12, 18 oder 24 Monate als Zeitraum genannt.
```

Die frühen elektronischen Computer waren teuer und nicht besonders leistungsfähig. Sie verstanden nur einen rudimentären Satz von Anweisungen, und es war eine sehr spezielle Aufgabe, die Anweisungen für eine komplexe Aufgabe zu schreiben, die mit den begrenzten Ressourcen solcher Maschinen ein nützliches Problem lösen konnte. Einfallsreichtum war eine wichtige Voraussetzung für einen Programmierer. Die menschliche Anstrengung, ein Programm sorgfältig zu entwerfen, zahlte sich durch schnelle, fehlerfreie Berechnungen aus.

```{figure} img/turing-bombe.jpg
---
width: 50%
name: Turing Bombe
---
Die Bombe ahmte die Funktionsweise mehrerer miteinander verkabelter Enigma-Maschinen nach. Jede der schnell rotierenden Trommeln, die oben in einer Nachbildung des Bletchley Park Museums abgebildet sind, simulierte die Funktion eines Enigma-Rotors.
```


Mit zunehmender Rechenleistung konnten die Anweisungen, die ein Computer verstand, erweitert werden. Es war keine Zeit- und Geldverschwendung mehr, Computerprogramme in einer für Menschen lesbaren Form zu schreiben und sie später vom Computer in seine eigenen, einfacheren Anweisungen übersetzen zu lassen. Echte Programmierung beginnt auf diese Weise: mit der Beschreibung der auszuführenden Operationen, ohne dass man die zugrundeliegenden Details der Maschine kennen muss, die die Berechnungen durchführt.

Es versteht sich wohl von selbst, dass dieser erste abstrakte Schritt zu immer weiterführenden Abstraktionen führte. Programme werden komplexer, und es kann hilfreich sein, einen Schritt weiterzugehen, bis wir eine Ebene erreichen, die sich nicht mit den Details innerhalb eines Programms befasst, sondern es einfach als eine Sammlung von Operationen behandelt, die die Informationen auf vorhersehbare Weise verarbeiten.  Eine *Bibliothek*, *Library* oder auch *Modul* ist eine Sammlung von Operationen, die eine kleine Anzahl von Aufgaben für mehrere andere Programme erledigen.

Die fortschreitende Computerleistung bedeutet, dass der Computer einen größeren Teil der Arbeit übernimmt und es einem Programmierer ermöglicht, das zu lösende Problem auf einer viel höheren Ebene zu betrachten. Außerdem können sehr allgemeine Bibliotheken erstellt und wiederverwendet werden, die bereits gründlich getestet wurden. In der Regel ist es kein Problem, dass Bibliotheken mehr leisten, als wir brauchen, und das bedeutet, dass wir keinen Code in einer Bibliothek ändern müssen auf die Gefahr hin, dass er kaputt geht.

Zumindest können wir davon ausgehen, dass Software (Programme) im Laufe der Zeit immer zuverlässiger werden und an Funktionalität gewinnen, wenn sie von Menschen korrigiert und verbessert werden, weil sie immer wiederverwendet werden können. Die Verbesserungen der Hardware machen dies möglich.

```{figure} img/apple-m1.jpg
---
width: 30%
name: M1
---
Der M1-Chip von Apple hat 16 Milliarden Transistoren, die im 5-nm-Maßstab erstellt werden. Er führt mehrere verschiedene Threads auf einem Chip aus und besitzt viele der Subsysteme, die früher auf separaten Chips untergebracht waren. Er ist nicht mit der vorherigen Chipgeneration kompatibel (er verwendet einen anderen Befehlssatz auf binärer Ebene), kann diese Chips aber bei Bedarf emulieren und hat dennoch einen gewissen Geschwindigkeitsvorteil. Dank der hohen Leistung und des großen Speicherplatzes können Sie sich auf das Schreiben robuster, flexibler Codes konzentrieren und müssen sich nicht mit cleveren Algorithmen herumschlagen, die speziell auf eine bestimmte Architektur abgestimmt sind. Fortschritt!  (Bild copyright: Apple, 2020)
```

Wenn die Computersprache, in der unsere Software geschrieben wurde, nicht diejenige ist, die wir verwenden, macht das nichts, wir können einfach eine Art Übersetzer schreiben und die zusätzlichen Kosten durch die fortschreitende Hardwaregeschwindigkeit und Speicherkapazität ausgleichen. Es ist sogar möglich, Software-Äquivalente der Computer-Hardware selbst zu erstellen. Einen soganannten *Emulator*, dieser ermöglicht es, das ein Program überall lauffähig ist und sogar von Maschine zu Maschine springen kann. Dies ist eine andere Art der Wiederverwendung: Es ist möglich, ein laufendes Gerät jederzeit neu zu erstellen oder zu klonen und jedes Mal identische Ergebnisse zu erhalten.