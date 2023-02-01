# Teil 2 - Spielerbewegung und Spiellogik

Sie haben nun ein Labyrinth, das Sie anzeigen können und aus dem Sie einen Ausweg finden können. Das Ziel dieses zweiten Teils wird es sein, die Bewegung einer Spielfigur durch das Labyrinth sowie die Anzeige einer Nachricht, wenn der Ausgang erreicht ist, zu realisieren.

## Aufgabe 5 - Bewegung des Spielers

Die Spiellogik für die Anzeige von Meldungen, wenn der Ausgang gefunden wurde, befindet sich in der Klasse `MazeGame`. Die Idee ist relativ einfach: Der Spieler kann seine Spielfigur mithilfe der Tastaturtasten bewegen. Wenn eine Bewegung zum Ausgang führt (dies geschieht in der gleichen Klasse), hat der Spieler gewonnen und ein neues Spiel beginnt.

1. Machen Sie sich mit der Klasse `MazeGame` vertraut.
2. Vervollständigen Sie die Methode `findPlayer(Player p)`, die die Koordinaten eines Spielers auf dem Spielfeld zurückgibt. Die Koordinaten werden in Form eines Punktes zurückgegeben. Wenn der Spieler nicht im Spiel ist, wird `null` zurückgegeben, was ein spezieller Wert ist, der "nichts"[^null] bedeutet.
3. Ergänzen Sie die Methode `movePlayer(Richtung d)`, die die Spielfigur in die vorgegebene Richtung bewegt. Beachten Sie, dass Sie die Wände korrekt berücksichtigen müssen. Um diese Methode zu debuggen, verwenden Sie sie direkt im `main`, um zu sehen, ob alles so läuft, wie Sie es sich vorstellen. Wenn Sie denken, dass Ihre Methode funktioniert, versuchen Sie, Ihre Spielfigur in verschiedene Richtungen zu bewegen.
4. Probieren Sie den Code, den Sie geschrieben haben, mit Labyrinthen aus, die nicht quadratisch sind. Warum kann genau dieser Punkt potenziell Probleme verursachen?

[^null]: Dies ist nicht die eleganteste Art, dies zu tun. Was passiert nämlich, wenn Sie die X-Position von Spieler 2 suchen und er nicht da ist? Versuchen Sie es, wenn Sie Zeit haben. Angesichts der heute verfügbaren Zeit ist dies jedoch ein vernünftiger Weg.

## Aufgabe 6 - Tastaturverwaltung

_Ein paar Worte zur Theorie - Umkehrung des Kontrollflusses_

Da Java sehr stark objektorientiert ist, ist es möglich, die einzelnen Schritte klar zu trennen. So findet die Verwaltung der Tasten in der Klasse `KeyboardListener` statt. In dieser Klasse wird der Kontrollfluss umgekehrt. Das bedeutet, dass nicht Sie entscheiden, wann eine Methode aufgerufen wird, sondern die virtuelle Maschine (ähnlich wie bei `Interrupts`). Bei einer grafischen Benutzeroberfläche weiss man beispielsweise nie, wann der Benutzer einen Knopf oder eine Taste drücken wird. Anstatt aktiv zu warten, ermöglicht diese Art der Kontrollumkehr, dass man reagieren kann, wenn es nötig ist.

Konkret bedeutet dies, dass Methoden von der Java Virtual Machine aufgerufen werden, wenn der Benutzer eine Taste gedrückt hat. Wenn der Benutzer beispielsweise eine Taste drückt und wieder loslässt, wird die Methode `keyPressed()` aufgerufen, mit dem die gedrückte Taste als Argument abgerufen werden kann. Wir empfehlen Ihnen, sich das Skelett anzusehen, das in der Klasse `KeyboardListener` bereitgestellt wird, um weitere Informationen zu erhalten.

1. Beobachten Sie die Klasse, insbesondere wie es möglich ist, auf spezielle Tasten der Tastatur wie die Funktionstasten (`HOME`, `F1`-`F12`...) zu reagieren.
2. Beachten Sie, dass eine Instanz des Spiels und eine Instanz des Labyrinths in der Klasse vorhanden sind. Wozu dienen sie Ihrer Meinung nach?
3. Stellen Sie sicher, dass Sie den Spieler mithilfe der Tasten bewegen können.
4. Sorgen Sie dafür, dass es möglich ist, die Lösung einzublenden. Dazu müssen Sie eine Taste mit der Ihnen zur Verfügung gestellten Methode `displaySolution`verknüpfen.

```{note}
Das folgende Klassendiagramm kann Ihnen helfen, wenn Sie sich über die Beziehungen zwischen den Klassen im Unklaren sind:
```


```{figure} resources/maze-class-diagram-2.svg
---
width: 90%
name: Maze Class Diagram 2
---
Maze Klassendiagram `MazeContainer`, `MazeGame`, `GraphicDisplay`, `KeyboardListener`
```

## Aufgabe 7 - Ausgang aus dem Labyrinth

Nachdem die Tastatur nun korrekt funktioniert, muss es möglich sein, eine Meldung anzuzeigen, wenn der Benutzer den Ausgang gefunden hat. Das ist der Zweck der Methode `checkWinner`, die Sie implementieren müssen. Um eine Nachricht in einem neuen Fenster anzuzeigen, können Sie die folgende [^example] Technik verwenden:

[^example]: Dieses Beispiel befindet sich als Kommentar am Ende von `MazeGame`, so dass Sie diesen direkt kopieren können.

```java
JOptionPane.showMessageDialog(null, "Titel des Fensters", "Text des Fensters! ", ,JOptionPane.INFORMATION_MESSAGE);
```

was zu einem Fenster wie unten führt:

```{figure} resources/maze-popup.png
---
width: 30%
name: Maze Popup
---
Popup
```

```{figure} resources/maze-game.png
---
width: 70%
name: Maze Game Final
---
Final Maze Game
```

```{important}
Wir wünschen Ihnen viel Spass bei der Umsetzung dieses Projekts!
```

```{admonition} Solution
:class: dropdown
Falls gewünscht kann eine Musterlösung hier heruntergeladen werden
[maze Masterversion](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook/content-de/java/maze/resources/mazegame_masterVersion.zip).
```
