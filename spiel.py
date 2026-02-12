"""
Spiel-Klasse für Gravitrips (Vier Gewinnt).

Autor: Martin (PremM239)

Aufgaben laut Issue #3:
- Spielstart und zentrale Spielschleife
- Abfrage und Verarbeitung der Spielmodi
- Steuerung der Spielerwechsel
- Darstellung des Spielfelds im Terminal
"""

from spieler import Spieler
from computerspieler import ComputerSpieler


class Spiel:
    """
    Die Hauptklasse die das Spiel steuert.
    
    Attributes
    ----------
    spielfeld : Spielfeld
        Das Spielfeld
    spieler1 : Spieler
        Erster Spieler
    spieler2 : Spieler oder ComputerSpieler
        Zweiter Spieler oder Computer
    aktueller_spieler : Spieler
        Wer gerade dran ist
    laeuft : bool
        Ob das Spiel läuft
    """
    
    def __init__(self, spielfeld):
        """
        Erstellt ein neues Spiel.
        
        Parameters
        ----------
        spielfeld : Spielfeld
            Das zu verwendende Spielfeld
        """
        self.spielfeld = spielfeld
        self.spieler1 = None
        self.spieler2 = None
        self.aktueller_spieler = None
        self.laeuft = False
    
    def starten(self):
        """Startet das Spiel."""
        print("\n" + "="*50)
        print("Willkommen bei GRAVITRIPS!")
        print("="*50)
        
        # Spielmodus wählen
        modus = self.modus_waehlen()
        
        # Spieler erstellen
        self.spieler1 = Spieler(1)
        
        if modus == "mensch":
            self.spieler2 = Spieler(2)
        else:
            self.spieler2 = ComputerSpieler()
        
        # Startspieler
        self.aktueller_spieler = self.spieler1
        
        print(f"\nSpiel gestartet!")
        print(f"{self.spieler1.name}: {self.spieler1.symbol}")
        print(f"{self.spieler2.name}: {self.spieler2.symbol}")
        print()
        
        # Spiel starten
        self.laeuft = True
        self.spiel_schleife()
    
    def modus_waehlen(self):
        """
        Fragt nach Spielmodus.
        
        Returns
        -------
        str
            'mensch' oder 'computer'
        """
        while True:
            print("\nWähle einen Spielmodus:")
            print("1 - Mensch gegen Mensch")
            print("2 - Mensch gegen Computer")
            
            auswahl = input("Deine Wahl (1 oder 2): ")
            
            if auswahl == "1":
                return "mensch"
            elif auswahl == "2":
                return "computer"
            else:
                print("Ungültig! Bitte 1 oder 2 eingeben.")
    
    def spiel_schleife(self):
        """Die zentrale Spielschleife."""
        while self.laeuft:
            # Spielfeld anzeigen
            self.spielfeld_anzeigen()
            
            # Aktueller Spieler macht Zug
            spalte = self.aktueller_spieler.zug_machen(self.spielfeld)
            
            # Möchte Spieler beenden?
            if spalte is None:
                print("\nSpiel beendet.")
                self.laeuft = False
                break
            
            # Computer-Zug anzeigen
            if self.aktueller_spieler.name == "Computer":
                print(f"\nComputer wählt Spalte {spalte + 1}")
            
            # Stein einwerfen
            erfolg = self.spielfeld.stein_einwerfen(spalte, self.aktueller_spieler.nummer)
            
            if not erfolg:
                print("Spalte ist voll! Wähle eine andere.")
                continue
            
            # Hat jemand gewonnen?
            if self.spielfeld.gewinn_pruefen(self.aktueller_spieler.nummer):
                self.spielfeld_anzeigen()
                self.gewonnen()
                break
            
            # Ist Feld voll (Unentschieden)?
            if self.spielfeld.ist_voll():
                self.spielfeld_anzeigen()
                self.unentschieden()
                break
            
            # Spieler wechseln
            self.spieler_wechseln()
    
    def spieler_wechseln(self):
        """Wechselt zwischen den Spielern."""
        if self.aktueller_spieler == self.spieler1:
            self.aktueller_spieler = self.spieler2
        else:
            self.aktueller_spieler = self.spieler1
    
    def spielfeld_anzeigen(self):
        """Zeigt das Spielfeld im Terminal an."""
        print("\n" + "="*50)
        print("  1   2   3   4   5   6   7")
        print("-" * 29)
        
        feld = self.spielfeld.feld_holen()
        
        # Jede Reihe durchgehen
        for reihe in feld:
            zeile = "| "
            for zelle in reihe:
                if zelle == 0:
                    zeile = zeile + ". "
                elif zelle == 1:
                    zeile = zeile + "X "
                else:
                    zeile = zeile + "O "
                zeile = zeile + "| "
            print(zeile)
        
        print("-" * 29)
        print("="*50)
    
    def gewonnen(self):
        """Wird aufgerufen wenn jemand gewonnen hat."""
        print("\n" + "="*50)
        print(f"🎉 {self.aktueller_spieler.name} ({self.aktueller_spieler.symbol}) hat gewonnen! 🎉")
        print("="*50)
        print("Danke fürs Spielen!")
        self.laeuft = False
    
    def unentschieden(self):
        """Wird aufgerufen bei Unentschieden."""
        print("\n" + "="*50)
        print("⚖️  Unentschieden! Das Feld ist voll. ⚖️")
        print("="*50)
        print("Danke fürs Spielen!")
        self.laeuft = False
