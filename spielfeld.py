"""
Spielfeld-Klasse für Gravitrips (Vier Gewinnt).

Autor: Paul (Nesselmuehle)
Status: Abgeschlossen ✓

Aufgaben laut Issue #4:
- Verwaltung des Spielfelds (6 Reihen, 7 Spalten)
- Einfügen von Spielsteinen (Schwerkraft beachten)
- Überprüfung der Gültigkeit von Spielzügen
- Gewinnüberprüfung (horizontal, vertikal, diagonal)
"""


class Spielfeld:
    """
    Das Spielfeld für Gravitrips.
    
    Attributes
    ----------
    reihen : int
        Anzahl der Reihen (6)
    spalten : int
        Anzahl der Spalten (7)
    feld : list
        Das Spielfeld als 2D-Liste
    """
    
    def __init__(self):
        """Erstellt ein neues Spielfeld."""
        self.reihen = 6
        self.spalten = 7
        self.feld = []
        
        # Feld mit Nullen füllen (0 = leer)
        for i in range(self.reihen):
            reihe = []
            for j in range(self.spalten):
                reihe.append(0)
            self.feld.append(reihe)
    
    def stein_einwerfen(self, spalte, spieler):
        """
        Wirft einen Stein in eine Spalte (berücksichtigt Schwerkraft).
        
        Parameters
        ----------
        spalte : int
            Die Spalte (0-6)
        spieler : int
            Spielernummer (1 oder 2)
        
        Returns
        -------
        bool
            True wenn erfolgreich, False wenn Spalte voll
        """
        # Prüfen ob Spalte gültig ist
        if spalte < 0 or spalte >= 7:
            return False
        
        # Prüfen ob Spalte voll ist
        if self.feld[0][spalte] != 0:
            return False
        
        # Stein fällt nach unten bis er auf was trifft
        for reihe in range(self.reihen - 1, -1, -1):
            if self.feld[reihe][spalte] == 0:
                self.feld[reihe][spalte] = spieler
                return True
        
        return False
    
    def ist_spalte_voll(self, spalte):
        """
        Prüft ob eine Spalte voll ist.
        
        Parameters
        ----------
        spalte : int
            Die Spalte (0-6)
        
        Returns
        -------
        bool
            True wenn voll
        """
        if spalte < 0 or spalte >= 7:
            return True
        
        # Wenn oberste Reihe nicht leer ist, ist Spalte voll
        if self.feld[0][spalte] != 0:
            return True
        else:
            return False
    
    def ist_voll(self):
        """
        Prüft ob das gesamte Feld voll ist.
        
        Returns
        -------
        bool
            True wenn komplett voll
        """
        # Wenn oberste Reihe überall gefüllt ist, ist alles voll
        for spalte in range(7):
            if self.feld[0][spalte] == 0:
                return False
        return True
    
    def gewinn_pruefen(self, spieler):
        """
        Prüft ob ein Spieler gewonnen hat.
        
        Parameters
        ----------
        spieler : int
            Spielernummer (1 oder 2)
        
        Returns
        -------
        bool
            True wenn Spieler gewonnen hat
        """
        # Horizontal prüfen
        for reihe in range(self.reihen):
            for spalte in range(self.spalten - 3):
                if (self.feld[reihe][spalte] == spieler and
                    self.feld[reihe][spalte + 1] == spieler and
                    self.feld[reihe][spalte + 2] == spieler and
                    self.feld[reihe][spalte + 3] == spieler):
                    return True
        
        # Vertikal prüfen
        for spalte in range(self.spalten):
            for reihe in range(self.reihen - 3):
                if (self.feld[reihe][spalte] == spieler and
                    self.feld[reihe + 1][spalte] == spieler and
                    self.feld[reihe + 2][spalte] == spieler and
                    self.feld[reihe + 3][spalte] == spieler):
                    return True
        
        # Diagonal nach rechts oben
        for reihe in range(3, self.reihen):
            for spalte in range(self.spalten - 3):
                if (self.feld[reihe][spalte] == spieler and
                    self.feld[reihe - 1][spalte + 1] == spieler and
                    self.feld[reihe - 2][spalte + 2] == spieler and
                    self.feld[reihe - 3][spalte + 3] == spieler):
                    return True
        
        # Diagonal nach rechts unten
        for reihe in range(self.reihen - 3):
            for spalte in range(self.spalten - 3):
                if (self.feld[reihe][spalte] == spieler and
                    self.feld[reihe + 1][spalte + 1] == spieler and
                    self.feld[reihe + 2][spalte + 2] == spieler and
                    self.feld[reihe + 3][spalte + 3] == spieler):
                    return True
        
        return False
    
    def feld_holen(self):
        """
        Gibt das aktuelle Spielfeld zurück.
        
        Returns
        -------
        list
            Das Spielfeld
        """
        return self.feld
    
    def zuruecksetzen(self):
        """Setzt das Spielfeld zurück."""
        for i in range(self.reihen):
            for j in range(self.spalten):
                self.feld[i][j] = 0
