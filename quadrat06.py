from turtle import *

startseite = 110
aenderung = -5

pensize (5)
pencolor ("red")
fillcolor ("cyan")

rt (45)

seite=startseite
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("green")
fillcolor ("magenta")

seite=seite - 10
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("blue")
fillcolor ("yellow")

seite = seite + aenderung
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("cyan")
fillcolor ("red")

seite = seite + aenderung
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("magenta")
fillcolor ("green")

seite = seite + aenderung
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)

pencolor ("yellow")
fillcolor ("blue")

seite = seite + aenderung
begin_fill ()
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
fd (seite), lt (90)
end_fill()

rt (60)
