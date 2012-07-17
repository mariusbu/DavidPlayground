from turtle import *

def fuelle_Quadrate():
    begin_fill()
    Quadrate()
    end_fill()
    right(60)
    
def Quadrate():
    forward(seite)
    left(90)
    forward(seite)
    left(90)
    forward(seite)
    left(90)
    forward(seite)
    left(90)

startseite = 110
aenderung = -5

reset()
pensize(5)

right(45)
color ("red", "cyan")

seite = startseite
fuelle_Quadrate()




color ("green", "magenta")
seite = seite + aenderung
fuelle_Quadrate()




color ("blue", "yellow")
seite = seite + aenderung
fuelle_Quadrate()




color ("cyan", "red")
seite = seite + aenderung
fuelle_Quadrate()




color ("magenta", "green")
seite = seite + aenderung
fuelle_Quadrate()




color ("yellow", "blue")
seite = seite + aenderung
fuelle_Quadrate()



