"""
Tests für die Spielfeld-Klasse.

Autor: Paul (Nesselmuehle)
"""

import pytest
from spielfeld import Spielfeld


def test_spielfeld_erstellen():
    """Testet ob Spielfeld erstellt werden kann."""
    spielfeld = Spielfeld()
    assert spielfeld.reihen == 6
    assert spielfeld.spalten == 7


def test_spielfeld_ist_leer():
    """Testet ob neues Spielfeld leer ist."""
    spielfeld = Spielfeld()
    for reihe in spielfeld.feld:
        for zelle in reihe:
            assert zelle == 0


def test_stein_einwerfen():
    """Testet ob Stein eingeworfen werden kann."""
    spielfeld = Spielfeld()
    erfolg = spielfeld.stein_einwerfen(3, 1)
    assert erfolg == True
    assert spielfeld.feld[5][3] == 1


def test_mehrere_steine():
    """Testet ob mehrere Steine übereinander fallen."""
    spielfeld = Spielfeld()
    spielfeld.stein_einwerfen(3, 1)
    spielfeld.stein_einwerfen(3, 2)
    spielfeld.stein_einwerfen(3, 1)
    
    assert spielfeld.feld[5][3] == 1
    assert spielfeld.feld[4][3] == 2
    assert spielfeld.feld[3][3] == 1


def test_volle_spalte():
    """Testet was passiert wenn Spalte voll ist."""
    spielfeld = Spielfeld()
    
    # Spalte 0 voll machen
    for i in range(6):
        spielfeld.stein_einwerfen(0, 1)
    
    # Noch einen Stein versuchen
    erfolg = spielfeld.stein_einwerfen(0, 1)
    assert erfolg == False


def test_spalte_voll():
    """Testet die ist_spalte_voll Funktion."""
    spielfeld = Spielfeld()
    
    # Am Anfang nicht voll
    assert spielfeld.ist_spalte_voll(3) == False
    
    # Spalte voll machen
    for i in range(6):
        spielfeld.stein_einwerfen(3, 1)
    
    # Jetzt voll
    assert spielfeld.ist_spalte_voll(3) == True


def test_feld_voll():
    """Testet ob erkannt wird wenn Feld voll ist."""
    spielfeld = Spielfeld()
    
    # Am Anfang nicht voll
    assert spielfeld.ist_voll() == False
    
    # Alles voll machen
    for spalte in range(7):
        for reihe in range(6):
            spielfeld.stein_einwerfen(spalte, 1)
    
    # Jetzt voll
    assert spielfeld.ist_voll() == True


def test_horizontal_gewinn():
    """Testet horizontalen Gewinn."""
    spielfeld = Spielfeld()
    
    # 4 Steine nebeneinander
    spielfeld.stein_einwerfen(0, 1)
    spielfeld.stein_einwerfen(1, 1)
    spielfeld.stein_einwerfen(2, 1)
    spielfeld.stein_einwerfen(3, 1)
    
    assert spielfeld.gewinn_pruefen(1) == True


def test_vertikal_gewinn():
    """Testet vertikalen Gewinn."""
    spielfeld = Spielfeld()
    
    # 4 Steine übereinander
    spielfeld.stein_einwerfen(3, 1)
    spielfeld.stein_einwerfen(3, 1)
    spielfeld.stein_einwerfen(3, 1)
    spielfeld.stein_einwerfen(3, 1)
    
    assert spielfeld.gewinn_pruefen(1) == True


def test_diagonal_gewinn():
    """Testet diagonalen Gewinn."""
    spielfeld = Spielfeld()
    
    # Diagonal aufbauen
    spielfeld.stein_einwerfen(0, 1)
    
    spielfeld.stein_einwerfen(1, 2)
    spielfeld.stein_einwerfen(1, 1)
    
    spielfeld.stein_einwerfen(2, 2)
    spielfeld.stein_einwerfen(2, 2)
    spielfeld.stein_einwerfen(2, 1)
    
    spielfeld.stein_einwerfen(3, 2)
    spielfeld.stein_einwerfen(3, 2)
    spielfeld.stein_einwerfen(3, 2)
    spielfeld.stein_einwerfen(3, 1)
    
    assert spielfeld.gewinn_pruefen(1) == True


def test_kein_gewinn():
    """Testet dass kein Gewinn erkannt wird wenn keiner da ist."""
    spielfeld = Spielfeld()
    
    spielfeld.stein_einwerfen(0, 1)
    spielfeld.stein_einwerfen(1, 2)
    spielfeld.stein_einwerfen(2, 1)
    
    assert spielfeld.gewinn_pruefen(1) == False
    assert spielfeld.gewinn_pruefen(2) == False


def test_drei_steine():
    """Testet dass 3 Steine nicht als Gewinn zählen."""
    spielfeld = Spielfeld()
    
    spielfeld.stein_einwerfen(0, 1)
    spielfeld.stein_einwerfen(1, 1)
    spielfeld.stein_einwerfen(2, 1)
    
    assert spielfeld.gewinn_pruefen(1) == False


def test_zuruecksetzen():
    """Testet ob Reset funktioniert."""
    spielfeld = Spielfeld()
    
    # Paar Steine einwerfen
    spielfeld.stein_einwerfen(0, 1)
    spielfeld.stein_einwerfen(1, 2)
    spielfeld.stein_einwerfen(2, 1)
    
    # Reset
    spielfeld.zuruecksetzen()
    
    # Alles leer?
    for reihe in spielfeld.feld:
        for zelle in reihe:
            assert zelle == 0
