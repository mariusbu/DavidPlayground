from turtle import *

def jump (distanz, winkel=0):
    pu ()
    rt (winkel)
    fd (distanz)
    lt (winkel)
    pd ()

def n_eck (eckenzahl, seitenlaenge):
    drehwinkel = 360.0 / eckenzahl
    for i in range (eckenzahl):
        fd (seitenlaenge)
        lt (drehwinkel)

def n_eck_demo (seitenlaenge):
    for i in range (a, b):
        n_eck (i, seitenlaenge)
        jump (100)
a = 4
b = 9
seitenlaenge = 20

jump (-200)
n_eck_demo (seitenlaenge)
