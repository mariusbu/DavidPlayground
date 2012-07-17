#autor: georg
#datum: 21.7.09
#arbeit: dreieck

from turtle import *

def jump (distanz, winkel):
    pu ()
    rt (winkel)
    fd (distanz)
    lt (winkel)
    pd ()
    
def dreieck (laenge):
    fd (laenge)
    lt (120)
    fd (laenge)
    lt (120)
    fd (laenge)
    lt (120)

def fuelle_dreieck (seitenlaenge, stiftfarbe, fuellfarbe):
    color (stiftfarbe, fuellfarbe)
    begin_fill ()
    dreieck (seitenlaenge)
    end_fill ()
    lt (120)

def dreierpack (startseite, aenderung):
    seite = startseite
    fuelle_dreieck (seite, "red", "cyan")

    seite = seite + aenderung
    fuelle_dreieck (seite, "green", "magenta")

    seite = seite + aenderung
    fuelle_dreieck (seite, "blue", "yellow")

pensize (10)

rt (90)

dreierpack (80, 30)
jump (250, 40)
dreierpack (100, -15)
jump (300, -50)
dreierpack (200, 50)
hideturtle ()
