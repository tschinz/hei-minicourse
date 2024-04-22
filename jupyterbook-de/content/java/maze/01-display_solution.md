# Teil 1 - Anzeigen und aus dem Labyrinth herauskommen

In diesem ersten Teil werden Sie den Quellcode, den wir für Sie vorbereitet haben, sowie die Struktur des Java-Codes kennen lernen. Am Ende dieses Teils werden Sie über die nötigen Mittel verfügen, um ein Labyrinth als Text und Bild darzustellen. Sie werden auch in der Lage sein, den Weg von einem beliebigen Punkt zum Ausgang im Bild darzustellen.

## Aufgabe 0 - Importieren des Projektes

Wir haben für Sie ein Eclipse-Projekt vorbereitet, das die grundlegenden Elemente des Projekts enthält. Um es zu importieren führen Sie folgende Schritte aus:
1. Starten Sie Eclipse und führen Sie dann _File->Import->General-> Projects from Folder or Archive_ aus.
2. Klicken Sie auf die Option _Archive_, wählen Sie die Datei
[maze Studentversion](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook-de/content/java/maze/resources/mazegame_studentVersion.zip) aus dem USB-Key und klicken Sie auf _Finish_. Das Maze-Projekt existiert nun in Ihrer Projektliste.

````{important}
Das Zip können Sie hier heruntereladen:

[maze Studentversion](https://github.com/tschinz/hei-minicourse/raw/main/jupyterbook-de/content/java/maze/resources/mazegame_studentVersion.zip)
````



## Aufgabe 1 - Zeichnen des Labyrinths in Textform

Diese erste Aufgabe wird Ihnen zeigen, wie das Labyrinth im Projekt codiert ist, indem Sie es als Text in der Konsole anzeigen sollen. Dies wird Ihnen den ganzen Tag über nützlich sein, da wir immer wieder die gleiche Datenstruktur verwenden werden.

1. Öffnen Sie die Datei `TextDisplay.java`, die sich in `maze/display` befindet, und betrachten Sie die Datei.
2. Beachten Sie, dass es in der Datei eine `main` gibt. Wie in C/C++ stellt `main` einen Einstiegspunkt in das Programm dar.
3. In dem `main` wird ein `MazeContainer` erstellt. Diese Klasse stellt das Labyrinth her und ermöglicht Ihnen den Zugriff darauf in Form eines zweidimensionalen Arrays aus `MazeElem`. In der Klasse befinden sich auch die Informationen über die Dimensionen des Labyrinths (Felder `nCellsX` und `nCellsY`).
4. Öffnen Sie die Klasse `MazeElem` und analysieren Sie sie. Diese letzte Klasse enthält bereits alle Informationen darüber, was sich in einem Feld des Labyrinths befindet (Wände, Spieler, Ausgang ...).
5. Das UML-Klassendiagramm, d. h. wie die Klassen organisiert sind, sieht folgendermassen aus:

   ```{figure} resources/maze-class-diagram-1.svg
   ---
   width: 70%
   name: Maze Class Diagram 1
   ---
   Maze Klassendiagram `MazeContainer` und `MazeElem`
   ```

6. Starten Sie das entsprechende Programm (Rechtsklick auf die Klasse `TextDisplay` => `Run As` => `Java Application`).
7. Ändern Sie das Programm so, dass ein Labyrinth der Grösse 5x5 angezeigt wird.
8. Wie Sie sehen, wird das Labyrinth nicht vollständig angezeigt, sondern nur die Kreuzungen und die Wände ganz unten und ganz rechts. Ergänzen Sie den Code an den mit `TODO Aufgabe 1` bezeichneten Stellen, damit das Labyrinth korrekt wie unten angezeigt wird (`p1` steht für die Position des ersten Spielers und `e` für den Ausgang). Ihre Anzeige folgendermassen sein:

```Text
*---*---*---*---*---*
| p1|               |
*   *   *---*---*   *
|   |   |       |   |
*   *---*   *   *   *
|           |       |
*---*---*---*---*   *
|       |           |
*   *---*   *---*---*
|         e         |
*---*---*---*---*---*
```


## Aufgabe 2 - Zeichnen des Labyrinths als Bild

Nachdem wir nun in der Lage sind, ein Labyrinth korrekt als Text anzuzeigen, ist es an der Zeit, unserem Programm ein wenig Grafik hinzuzufügen. Eine Klasse, die ähnlich wie `TextDisplay` funktioniert, finden Sie in der Datei `GraphicDisplay.java`.

1. Öffnen Sie die Datei `GraphicDisplay.java`.
2. Beobachten Sie die Methode `main` dieser Klasse und führen Sie sie aus.
3. Ändern Sie den Code so, dass ein 10x10-Labyrinth angezeigt wird.
4. Sie können die Grösse jedes kleinen Quadrats ändern, indem Sie einen Parameter im Konstruktor von `GraphicDisplay` verändern. Versuchen Sie es mit anderen grösseren und kleineren Werten.
5. Es ist möglich, das Labyrinth ohne die Fensterränder anzuzeigen. Finden Sie heraus, wie das geht, und führen Sie Ihr Programm aus. Sie werden etwas Ähnliches erhalten wie das, was rechts in der nebenstehenden Abbildung zu sehen ist. Sie können entscheiden, ob Sie eher diese oder die andere Methode verwenden möchten, je nachdem, was Ihnen lieber ist. Versuchen Sie auch, das Hintergrundgitter sichtbar zu machen (hierzu können Sie eine Variable ändern).

   ```{figure} resources/maze-mini.png
   ---
   width: 10%
   name: Mini Maze
   ---
   Mini Maze
   ```

6. Um sicherzustellen, dass die Anzeige korrekt ist, lassen Sie sich auch eine Textversion desselben Labyrinths aus dem `main` anzeigen.

## Aufgabe 3 - Lee's Propagierungsalgorithmus

In dieser Phase werden Sie eine Möglichkeit implementieren, den Ausgang des Labyrinths mithilfe eines Routing-Algorithmus automatisch zu finden.

1. Öffnen Sie die Klasse `AStar.java`, die das Skelett der Solverklasse für das Labyrinth nach der Methode von Lee enthält, die vorgestellt wurde. Die Ausbreitungsphase des Algorithmus (wenn der Pfad vom Startpunkt aus in alle Richtungen wächst) kann formal wie folgt beschrieben werden:

   ```Text
   Algorithmus 1 - Propagation von Lee (Algorithmus A*)
   Markieren Sie den Startpunkt mit 1
   m <= 1
   // Wellenförmige Ausbreitung
   wiederholen
     Markiert alle nicht markierten Nachbars Zellen vom den markierten Punkten m mit m+1
     m <= m+1
   bis zum gefundenen Ziel oder es gibt keine weiteren Punkte die markiert werden können
   ```
2. Um Ihre Methode zu testen, wurde hier auch ein `main` erstellt. Sie können es verwenden, um Ihren Code leichter zu debuggen.
3. Beobachten Sie die Methode `solve`. Sie beginnt damit, eine leere Lösung zu erstellen (die eigentlich ein Array von Ganzzahlen ist). Sie fährt fort, indem sie Lee's Propagation und dann das Backtracking durchführt. Das Ziel des gesamten Algorithmus ist es, überall dort eine `1` zu setzen, wo sich der Lösungsweg zwischen dem als Argument übergebenen Punkt und der Ausgabe befindet. Zum Beispiel das Labyrinth:

   ```Text
   *---*---*---*---*
   | p1|           |
   *   *   *---*   *
   |   |   |       |                              1 - 0 - 0 - 0
   *   *---*   *   *     wird am Ende ergeben     1 - 0 - 1 - 1
   |           |   |                              1 - 1 - 1 - 1
   *---*---*---*   *                              0 - 1 - 1 - 1
   |     e         |
   *---*---*---*---*
   ```

4. Wenn wir das Backtracking entfernen (indem wir die Methode `backtrace()` in `solve` auskommentieren), können wir die Schritte der Ausbreitung sehen, was sehr praktisch ist, um den Code zu debuggen. Im obigen Fall sieht das dann so aus:

   ```Text
   01 - 10 - 09 - 08
   02 - 11 - 06 - 07
   03 - 04 - 05 - 08
   00 - 11 - 10 - 09
   ```

5. Um dieses Ergebnis erzielen zu können, müssen Sie die Methode `expansion` implementieren. Diese wird von `solve` aufgerufen, solange sie nicht `true` zurückgibt (d. h. solange die Ausbreitung der Welle das Ziel noch nicht erreicht hat). Beachten Sie auch, dass die Methode bei jedem Aufruf den Status von `m` erhält, der die Nummer des aktuellen Schritts ist. Es liegt an Ihnen, herauszufinden, wie Sie das machen (mit unserer Hilfe)! Zögern Sie nicht, die Methode `access_solution()` zu verwenden (indem Sie verstehen, wozu sie dient...).

## Aufgabe 4 - Anzeige der Lösung im Grafikfenster

Ihre Implementierung des vorherigen Punktes liefert Ihnen eine Tabelle, die eine Lösung ab einem bestimmten Punkt enthält. Sie haben die Möglichkeit, diese direkt in der grafischen Darstellung des Labyrinths anzuzeigen. Dies werden Sie in dieser Aufgabe umsetzen.
1. Lassen Sie sich von dem bisherigen Vorgehen inspirieren und zeigen Sie vom `main` Klasse `AStar` die grafische Version des Labyrinths an.
2. Das Objekt der Klasse `GraphicDisplay`, das Sie erstellt haben, verfügt über eine Methode `setSolution()`, die als Argument ein Ganzzahl-Array entgegennimmt, das einer Lösung von einem Punkt aus entspricht. Verwenden Sie diese Methode, um die Lösung anzuzeigen, die mit dem im vorherigen Schritt erstellten Lee's Algorithmus berechnet wurde. Wenn Sie die Lösung aus der Anzeige entfernen möchten, verwenden Sie die Methode `clearSolution()`.

## Optionale Aufgaben

1. Ändern Sie die Art und Weise, wie der Spieler gezeichnet wird (andere Form wie ein Pfeil, der den letzten Zug zeigt, Farben, ...).
2. Zeigen Sie eine andere Zeichnung für den Ausgang an (z. B. einen Pfeil, der nach aussen zeigt).