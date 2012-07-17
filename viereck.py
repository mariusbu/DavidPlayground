#autor: georg
#datum: 21.7.09
#arbeit: wabe

from xturtle import *

def viereck ():
    begin_fill ()
    fd (seite)
    lt (90)
    fd (seite)
    lt (90)
    fd (seite)
    lt (90)
    fd (seite)
    lt (30)
    end_fill ()


pensize (4)
color ("red", "cyan")
seite = 35
aenderung = 15

viereck ()

color ("green", "magenta")
seite = seite + aenderung

viereck ()

color ("blue", "yellow")
seite = seite + aenderung

viereck ()

color ("cyan", "red")
seite = seite + aenderung

viereck ()

color ("magenta", "green")
seite = seite + aenderung

viereck ()

color ("yellow", "blue")
seite = seite + aenderung

viereck ()
