"""
Hauptprogramm für Gravitrips (Vier Gewinnt).

Startet das Spiel.
"""

from spielfeld import Spielfeld
from spiel import Spiel


def main():
    """Startet das Spiel."""
    # Spielfeld erstellen
    spielfeld = Spielfeld()
    
    # Spiel erstellen
    spiel = Spiel(spielfeld)
    
    # Spiel starten
    spiel.starten()


if __name__ == "__main__":
    main()
