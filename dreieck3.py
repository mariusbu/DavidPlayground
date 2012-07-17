#autor: georg
#datum: 21.7.09
#arbeit: dreieck

from xturtle import *

pensize (3)

rt (90)

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

seite = 65
aenderung = 35

fuelle_dreieck (seite, "red", "cyan")

seite = seite + aenderung
fuelle_dreieck (seite, "green", "magenta")

seite = seite + aenderung
fuelle_dreieck (seite, "blue", "yellow")

