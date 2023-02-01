# Konfiguration

Der erste Schritt ist die Installation von Git. Du kannst die neueste Version über die offizielle Website https://git-scm.com/ herunterladen. Git ist für Linux, Mac und Windows verfügbar. Für dieses Labor wird git ≥ 2.27 benötigt.

## Kommandozeile

Starte "Git Bash". Dies ist ein Unix/Linux-ähnlicher Befehlseditor, der es ermöglicht, Git-Befehle im Konsolenmodus auszuführen. Diese Schnittstelle werden wir in diesem Labor verwenden.

```{figure} resources/git-terminal.png
---
width: 80%
name: Git terminal
---
git Terminal
```

```{important}
Beachten Sie, dass Sie bei allen Befehlen in Git Bash Hilfe erhalten, indem Sie  nach dem Befehl `--help` einfügen.
```

## Globale Konfiguration

Eine Vielzahl von Einstellungen kann in Git konfiguriert werden. Es ist möglich, die Einstellungen global auf deinem Computer (Flag `--global`) oder nur für ein bestimmtes Repository zu ändern. Sie werden die Minimalkonfiguration durchführen.
Konfigurieren Sie nun Ihre Identität. Verwende die folgenden Befehle, um deine Identität in Git global auf dem System einzustellen. Verwende deinen Namen und deine E-Mail-Adresse. Diese Informationen sind öffentlich sichtbar, um deine Arbeit (deine Commits) zu identifizieren.

```bash
git config --global user.name "Firstname Lastname"
git config --global user.email first.last@email.ch
```

Sie können die Konfiguration mit dem folgenden Befehl überprüfen:

```bash
git config --list
```

Sie können auch eine bestimmte Einstellung überprüfen:

```bash
git config user.name
 ```
