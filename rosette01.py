from turtle import *

def n_eck (eckenzahl, seitenlaenge):
    drehwinkel = 360.0 / eckenzahl
    blau = 1.0
    aenderung = -2.0 / eckenzahl
    for i in range (eckenzahl):
        rot = 1.0 - blau
        pencolor(rot, 0, blau)
        fd (seitenlaenge)
        lt (drehwinkel)
        if i == eckenzahl // 2.0:
            aenderung = -aenderung
        blau = blau + aenderung
        

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

title ("turtle - Wikipedia Beispiel Nr. 1")

bgcolor ("black")

pensize (2)
tracer (False)
super_rosette (36, 15)
tracer (True)

ht ()
