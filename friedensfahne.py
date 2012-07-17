from turtle import *

def jump (distanz, winkel=0):
    pu ()
    rt (winkel)
    fd (distanz)
    lt (winkel)
    pd ()

friedensfarben = ["red3","orange","yellow","seagreen","orchid4",
                  "royalblue1","dodgerblue4"]

streifenbreite = 44


def streifen (laenge, breite, farbe):
    pensize (breite)
    pencolor (farbe)
    fd (laenge)
    jump (-laenge)

def fahne ():
    lt (90)
    jump(-3*streifenbreite)
    rt (90)
    jump (-200)

    for farbe in friedensfarben:
        streifen (400, streifenbreite, farbe)
        jump (streifenbreite, -90)
    pu ()
    home ()
    pd ()

def kreis (radius):
    jump (radius, 90)
    circle (radius)
    jump (radius, -90)

def logo (radius):
    for winkel in [225, 270, 315, 90]:
        setheading (winkel)
        streifen (radius, 20, "white")
    kreis (radius)

def peace ():
    fahne ()
    logo (120)
    ht ()

reset ()
peace ()
