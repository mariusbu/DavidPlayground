#autor: georg
#datum: 21.7.09
#arbeit: dreieck

from xturtle import *

pensize (3)

rt (90)

def dreieck ():
    fd (seite)
    lt (120)
    fd (seite)
    lt (120)
    fd (seite)
    lt (120)

def fuelle_dreieck ():
    global seite
    begin_fill ()
    dreieck ()
    end_fill ()
    seite = seite + aenderung
    lt (120)

color ("red", "cyan")

startseite = 65
aenderung = 35
seite=startseite

fuelle_dreieck ()

color ("green", "magenta")

fuelle_dreieck ()

color ("blue", "yellow")

fuelle_dreieck ()

