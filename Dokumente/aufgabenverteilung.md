# Aufgabenverteilung - Gravitrips Projekt

**Projekt:** Gravitrips (Vier Gewinnt)  
**Team:** Paul (Nesselmuehle) und Martin (PremM239)  
**Semester:** WS 2025

---

## Team-Mitglieder

- **Paul (Nesselmuehle)**: Verantwortlich für Spielfeld-Klasse und Tests
- **Martin (PremM239)**: Verantwortlich für Spiel-Klasse, Spieler-Klassen und UI

---

## Erste Schritte (abgeschlossen)

### Gemeinsam
- [x] Analyse der Projektangabe
- [x] Erarbeitung der Spielregeln von Gravitrips
- [x] Festlegung der Sprache: Deutsch
- [x] GitHub-Repository erstellen und initialisieren
- [x] Erste konzeptionelle Überlegungen zur Klassenstruktur

---

## Erste Klasseneinteilung (abgeschlossen)

Wir haben uns für folgende Klassenstruktur entschieden:

### Klassen

1. **Spiel**
   - Verantwortlich für den gesamten Spielablauf
   - Spielsteuerung
   - Benutzerinteraktion

2. **Spielfeld**
   - Verwaltung des Spielbretts
   - Durchführung von Spielzügen
   - Überprüfung der Spielregeln

3. **Spieler**
   - Repräsentiert einen menschlichen Spieler

4. **ComputerSpieler**
   - Implementiert einen einfachen Computergegner
   - Wählt gültige Spielzüge automatisch aus

---

## Aufgaben von Paul (abgeschlossen ✅)

### Implementierung der Spielfeld-Klasse
- [x] Verwaltung des Spielfelds (6 Reihen, 7 Spalten)
- [x] Umsetzung des Einfügens von Spielsteinen
- [x] Berücksichtigung der Schwerkraft beim Einwerfen
- [x] Überprüfung der Gültigkeit von Spielzügen
- [x] Implementierung der Gewinnüberprüfung
  - [x] Horizontal
  - [x] Vertikal
  - [x] Diagonal (beide Richtungen)

### Tests
- [x] Unit-Tests für alle Spielfeld-Methoden
- [x] Test-Abdeckung sicherstellen

---

## Aufgaben von Martin (abgeschlossen ✅)

### Implementierung der Spiel-Klasse
- [x] Umsetzung des Spielstarts
- [x] Zentrale Spielschleife implementieren
- [x] Abfrage und Verarbeitung der Spielmodi
  - [x] Mensch gegen Mensch
  - [x] Mensch gegen Computer
- [x] Steuerung der Spielerwechsel

### Implementierung der Spieler-Klasse
- [x] Repräsentation eines menschlichen Spielers
- [x] Eingabe-Verarbeitung

### Implementierung der ComputerSpieler-Klasse
- [x] Auswahl zufälliger, gültiger Spielzüge
- [x] Integration in die Spielschleife




