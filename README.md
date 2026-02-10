# Gravitrips (Vier Gewinnt)

Ein klassisches Vier-Gewinnt-Spiel in Python.

Projekt für die Lehrveranstaltung "SEM - AI" im Wintersemester 2025.

## Spielregeln

Zwei Spieler werfen abwechselnd Spielsteine in ein senkrechtes Gitter mit 7 Spalten und 6 Reihen. Die Steine fallen durch die Schwerkraft nach unten. Gewonnen hat, wer zuerst vier eigene Steine in einer Reihe hat – waagerecht, senkrecht oder diagonal.

## Installation

Du brauchst Python 3 auf deinem Computer.

### Repository klonen

```bash
git clone https://github.com/Nesselmuehle/Gravitrips.git
cd Gravitrips
```

## Spielen

```bash
python main.py
```

1. Wähle Spielmodus (1 oder 2)
2. Gib die Spaltennummer ein (1-7)
3. Drücke 'q' zum Beenden

## Tests ausführen

```bash
pip install pytest
pytest
```

## Projektstruktur

```
Gravitrips/
├── main.py              # Startet das Spiel
├── spiel.py             # Spiel-Klasse (Martin)
├── spielfeld.py         # Spielfeld-Klasse (Paul)
├── spieler.py           # Spieler-Klasse (Martin)
├── computerspieler.py   # ComputerSpieler-Klasse (Martin)
├── test_spielfeld.py    # Tests
├── README.md            # Diese Datei
└── docs/                # Dokumentation
```

## Status

✅ Spielfeld-Klasse (Paul) - Abgeschlossen
✅ Spiel-Klasse (Martin) - Abgeschlossen
✅ Spieler-Klasse (Martin) - Abgeschlossen
✅ ComputerSpieler-Klasse (Martin) - Abgeschlossen
✅ Tests - Abgeschlossen
