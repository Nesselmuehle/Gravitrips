# Planung - Gravitrips Projekt

## Projektziel

Entwicklung eines funktionsfähigen Vier-Gewinnt-Spiels (Gravitrips) in Python mit objektorientierter Programmierung.

---

## Geplante Klassenstruktur

### 1. Spielfeld-Klasse

**Verantwortlichkeit:** Verwaltung des Spielbretts und Spiellogik

**Attribute:**
- `reihen: int` - Anzahl Reihen (6)
- `spalten: int` - Anzahl Spalten (7)
- `feld: list` - 2D-Liste für das Spielfeld

**Methoden:**
- `__init__()` - Initialisierung des Spielfelds
- `stein_einwerfen(spalte, spieler)` - Stein in Spalte werfen
- `ist_spalte_voll(spalte)` - Prüft ob Spalte voll ist
- `ist_voll()` - Prüft ob gesamtes Feld voll ist
- `gewinn_pruefen(spieler)` - Prüft alle Gewinnbedingungen
- `feld_holen()` - Gibt aktuelles Feld zurück
- `zuruecksetzen()` - Setzt Feld zurück

### 2. Spiel-Klasse

**Verantwortlichkeit:** Steuerung des Spielablaufs und UI

**Attribute:**
- `spielfeld: Spielfeld` - Das Spielfeld-Objekt
- `spieler1: Spieler` - Erster Spieler
- `spieler2: Spieler/ComputerSpieler` - Zweiter Spieler
- `aktueller_spieler: Spieler` - Wer gerade dran ist
- `laeuft: bool` - Spiel-Status

**Methoden:**
- `__init__(spielfeld)` - Initialisierung mit Spielfeld
- `starten()` - Startet das Spiel
- `modus_waehlen()` - Spielmodus-Auswahl
- `spiel_schleife()` - Zentrale Spielschleife
- `spieler_wechseln()` - Wechselt aktiven Spieler
- `spielfeld_anzeigen()` - Zeigt Spielfeld im Terminal
- `gewonnen()` - Gewinn-Nachricht
- `unentschieden()` - Unentschieden-Nachricht

### 3. Spieler-Klasse

**Verantwortlichkeit:** Repräsentation eines menschlichen Spielers

**Attribute:**
- `nummer: int` - Spielernummer (1 oder 2)
- `symbol: str` - Spielsymbol ('X' oder 'O')
- `name: str` - Spielername

**Methoden:**
- `__init__(nummer)` - Initialisierung
- `zug_machen(spielfeld)` - Fragt nach Eingabe, gibt Spalte zurück

### 4. ComputerSpieler-Klasse

**Verantwortlichkeit:** Einfacher Computer-Gegner

**Attribute:**
- `nummer: int` - Immer 2
- `symbol: str` - Immer 'O'
- `name: str` - "Computer"

**Methoden:**
- `__init__()` - Initialisierung
- `zug_machen(spielfeld)` - Wählt zufällige gültige Spalte

---

## Klasseninteraktion

```
main.py
  └─ erstellt Spielfeld
  └─ erstellt Spiel(spielfeld)
  └─ ruft spiel.starten()

Spiel
  └─ verwendet Spielfeld
  └─ erstellt Spieler1
  └─ erstellt Spieler2 oder ComputerSpieler
  └─ ruft spieler.zug_machen(spielfeld)
  └─ ruft spielfeld.stein_einwerfen()
  └─ ruft spielfeld.gewinn_pruefen()
```

## Änderungen während der Implementierung

### Geplant vs. Tatsächlich

**Geplant:**
- 4 Klassen: Spielfeld, Spiel, Spieler, ComputerSpieler

**Tatsächlich umgesetzt:**
- ✅ Genau wie geplant!
- Keine wesentlichen Änderungen

**Kleinere Anpassungen:**
- Symbole 'X' und 'O' statt 1 und 2 für Anzeige
- Einfache Zufallsstrategie für Computer
