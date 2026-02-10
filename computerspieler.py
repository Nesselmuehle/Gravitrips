"""
ComputerSpieler-Klasse für Gravitrips (Vier Gewinnt).

Autor: Martin (PremM239)

Diese Klasse implementiert einen einfachen Computergegner.
"""

import random


class ComputerSpieler:
    """
    Ein Computer-Gegner.
    
    Attributes
    ----------
    nummer : int
        Spielernummer (immer 2)
    symbol : str
        Symbol des Computers ('O')
    name : str
        Name des Computers
    """
    
    def __init__(self):
        """Erstellt einen neuen Computer-Gegner."""
        self.nummer = 2
        self.symbol = 'O'
        self.name = "Computer"
    
    def zug_machen(self, spielfeld):
        """
        Computer macht einen Zug (wählt zufällige gültige Spalte).
        
        Parameters
        ----------
        spielfeld : Spielfeld
            Das aktuelle Spielfeld
        
        Returns
        -------
        int
            Gewählte Spalte (0-6)
        """
        # Finde alle Spalten die nicht voll sind
        freie_spalten = []
        for i in range(7):
            if not spielfeld.ist_spalte_voll(i):
                freie_spalten.append(i)
        
        # Wähle zufällig eine davon
        spalte = random.choice(freie_spalten)
        
        return spalte
