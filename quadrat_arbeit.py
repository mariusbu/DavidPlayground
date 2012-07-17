print"""Dieses Pogramm zeichent 6 gegeneinander gedrehte
bunte Quadrate mit wachsender oder abnehmender Größe"""
seite = raw_input ("Länge der Seiten des ersten Quadrates:")
faktor = raw_input ("faktor der Quadratseiten:")

seite = float(seite)
faktor = float(faktor)

from turtle import *

shape ("turtle")
speed (0)

pensize (5)
pencolor ("red")
fillcolor ("cyan")

rt (45)

begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("green")
fillcolor ("magenta")

seite = seite * faktor
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("blue")
fillcolor ("yellow")

seite = seite * faktor
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("cyan")
fillcolor ("red")

seite = seite * faktor
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("magenta")
fillcolor ("green")

seite = seite * faktor
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("yellow")
fillcolor ("blue")

seite = seite * faktor
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

print "Klasse was!?"
