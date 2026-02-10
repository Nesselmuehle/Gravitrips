"""
Spieler-Klasse für Gravitrips (Vier Gewinnt).

Autor: Martin (PremM239)

Diese Klasse repräsentiert einen menschlichen Spieler.
"""


class Spieler:
    """
    Ein menschlicher Spieler.
    
    Attributes
    ----------
    nummer : int
        Spielernummer (1 oder 2)
    symbol : str
        Symbol des Spielers ('X' oder 'O')
    name : str
        Name des Spielers
    """
    
    def __init__(self, nummer):
        """
        Erstellt einen neuen Spieler.
        
        Parameters
        ----------
        nummer : int
            Die Spielernummer (1 oder 2)
        """
        self.nummer = nummer
        
        # Symbol festlegen
        if nummer == 1:
            self.symbol = 'X'
        else:
            self.symbol = 'O'
        
        self.name = f"Spieler {nummer}"
    
    def zug_machen(self, spielfeld):
        """
        Spieler macht einen Zug (fragt nach Eingabe).
        
        Parameters
        ----------
        spielfeld : Spielfeld
            Das aktuelle Spielfeld
        
        Returns
        -------
        int or None
            Gewählte Spalte (0-6) oder None zum Beenden
        """
        while True:
            eingabe = input(f"\n{self.name} ({self.symbol}), wähle Spalte (1-7) oder 'q' zum Beenden: ")
            
            # Beenden?
            if eingabe == "q" or eingabe == "Q":
                return None
            
            # Versuche Zahl zu lesen
            try:
                spalte = int(eingabe) - 1  # -1 weil Array bei 0 anfängt
                
                # Prüfe ob Spalte gültig ist
                if spalte >= 0 and spalte < 7:
                    return spalte
                else:
                    print("Bitte Zahl zwischen 1 und 7 eingeben!")
            except:
                print("Das war keine Zahl! Bitte nochmal.")
