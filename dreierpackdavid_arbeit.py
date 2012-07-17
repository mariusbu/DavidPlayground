#Autor: David
#Datum: 25.07.09
#arbeit: Dreiecke

from turtle import *

startseite=65
aenderung=35

pensize(10)
color ("red", "cyan")

seite = startseite
begin_fill()
fd(seite), lt(120)
fd(seite), lt(120)
fd(seite)
end_fill()

color ("green",  "magenta")

seite = seite + aenderung
begin_fill()
fd(seite), lt(120)
fd(seite), lt(120)
fd(seite)
end_fill()

color ("blue",  "yellow")


seite = seite + aenderung
begin_fill()
fd(seite), lt(120)
fd(seite), lt(120)
fd(seite)
end_fill()

hideturtle()
