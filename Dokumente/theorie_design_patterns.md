\# Theorie – Design Patterns

\## 1. Strategy Pattern

Das Strategy Pattern wird verwendet, wenn es mehrere Möglichkeiten gibt, ein bestimmtes Problem zu lösen. Statt alle Varianten direkt in einer großen Methode mit vielen Bedingungen zu implementieren, werden die unterschiedlichen Lösungswege in eigene Klassen ausgelagert.

Das Problem entsteht häufig, wenn ein Programm verschiedene Verhaltensweisen unterstützen soll. Wenn man alles in einer Klasse regelt, wird der Code schnell unübersichtlich und schwer erweiterbar. Jede neue Variante würde Änderungen am bestehenden Code erfordern.

Beim Strategy Pattern definiert man eine gemeinsame Schnittstelle für alle Strategien. Jede konkrete Strategie implementiert diese Schnittstelle auf ihre eigene Weise. Das Hauptprogramm arbeitet nur mit dieser gemeinsamen Schnittstelle und kann zur Laufzeit entscheiden, welche Strategie verwendet werden soll.

Der Vorteil liegt darin, dass neue Strategien ergänzt werden können, ohne vorhandenen Code stark verändern zu müssen. Außerdem wird der Code besser strukturiert und leichter wartbar.

---

\## 2. Observer Pattern

Das Observer Pattern beschreibt ein Benachrichtigungssystem zwischen Objekten. Wenn sich der Zustand eines Objekts ändert, werden andere Objekte automatisch darüber informiert.

Das Problem tritt auf, wenn mehrere Teile eines Programms auf Änderungen reagieren müssen. Ohne ein solches Muster entsteht schnell eine starke Abhängigkeit zwischen den Klassen, was spätere Änderungen erschwert.

Beim Observer Pattern gibt es ein sogenanntes Subjekt, das eine Liste von Beobachtern verwaltet. Diese Beobachter können sich registrieren. Wenn sich der Zustand des Subjekts ändert, werden alle registrierten Beobachter benachrichtigt.

Der Vorteil ist, dass neue Beobachter hinzugefügt werden können, ohne das Subjekt grundlegend zu verändern. Dadurch bleibt das System flexibel und besser erweiterbar.
