from turtle import *

def jump (distanz, winkel=0):
    pu ()
    rt (winkel)
    fd (distanz)
    lt (winkel)
    pd ()


def streifen (laenge, breite, farbe):
    pensize (breite)
    pencolor (farbe)
    fd (laenge)
    jump (-laenge)

friedensfarben = ("red3","orange","yellow","seagreen4",
                  "orchid4","royalblue1","dodgerblue4")
streifenbreite = 44

def fahne ()
    jump(-3 * streifenbreite)
    rt (90)
    jump (-200)

    for farbe in friedensfarben:
        streifen (400, streifenbreite, farbe)
        jump(streifenbreite, -90)

    pu ()
    home ()
    pd ()

reset ()
home ()
