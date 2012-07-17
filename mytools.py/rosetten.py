from turtle import *

def n_eck (eckenzahl, seitenlaenge):
    drehwinkel = 360.0 / eckenzahl
    for i in range (eckenzahl):
        fd (seitenlaenge)
        lt (drehwinkel)

def rosette (eckenzahl, blattzahl, seitenlaenge):
    drehwinkel = 360.0 / blattzahl
    for i in range (blattzahl):
        n_eck (eckenzahl, seitenlaenge)
        lt (drehwinkel)

def super_rosette (eckenzahl, seitenlaenge):
    drehwinkel = 360.0 / eckenzahl 
    for i in range (eckenzahl):
        n_eck (eckenzahl, seitenlaenge)
        lt (drehwinkel)





