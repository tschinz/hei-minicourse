# Branch und Merge

Bisher haben wir die grundlegenden Funktionen von git verwendet. Es gibt auch die Funktionen `branch` (Zweig) und `merge` (zusammenführen), die Git im Vergleich zu den früher existierenden Tools stark vereinfacht hat.

Für diese praktische Arbeit können Sie sich mit dem Befehl `gitk` behelfen, der Ihnen eine grafische Darstellung und einen visuellen Verlauf der Commits in Ihrem Repo liefert.

1. Erstellen Sie in Ihrem lokalen Repo einen Entwicklungszweig `dev01`.
2. Erstellen Sie auf diesem Zweig zwei Commits:
   * Einen, um eine Datei `hello_world.py` zu erstellen.
   * Eines, um diese Datei `hello_world.py` zu füllen
3. Vom `master` Branch aus erstellen Sie einen neuen Entwicklungszweig `dev02`.
4. Erstellen Sie auf dem Zweig `dev02` einen Commit:
   * Bearbeiten Sie die Datei `README.md`.
5. Merge den Zweig `dev02` in `master`.
6. Merge den Zweig `dev01` in `master`.
7. Pushen Sie Ihr lokales Repository auf Ihren GitHub Remote.
