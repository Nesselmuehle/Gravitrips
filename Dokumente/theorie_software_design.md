# Theorie – Software Design

Wenn ich als neuer Entwickler ein Modul übernehme, das über lange Zeit gewachsen ist und nur aus wenigen Klassen mit sehr langen Methoden besteht, ergeben sich mehrere Probleme.

Zunächst ist der Code schwer verständlich. Sehr lange Methoden mit mehreren hundert Zeilen sind unübersichtlich und erschweren es, die Logik schnell nachzuvollziehen. Wenn zusätzlich nur wenig dokumentiert ist, kostet die Einarbeitung viel Zeit.

Ein weiteres Problem ist die Wartbarkeit. Wenn viele Aufgaben innerhalb einer einzigen Methode erledigt werden, kann schon eine kleine Änderung unerwartete Auswirkungen auf andere Teile des Codes haben. Dadurch steigt das Risiko, neue Fehler zu verursachen.

Auch das Testen wird schwieriger. Große Methoden lassen sich schlecht in einzelne Teile zerlegen, wodurch Unit-Tests nur eingeschränkt möglich sind. Das erschwert die Qualitätssicherung.

In einem solchen Modul werden vermutlich grundlegende Software-Design-Prinzipien nicht eingehalten. Dazu gehört vor allem das Single Responsibility Principle, nach dem eine Klasse oder Methode nur eine klar definierte Aufgabe haben sollte. Außerdem wird das Prinzip der Modularität verletzt, da der Code nicht in kleinere, übersichtliche Einheiten aufgeteilt ist.
