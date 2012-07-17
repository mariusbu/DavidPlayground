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
        tracer (False)
        n_eck (eckenzahl, seitenlaenge)
        tracer (True)
        lt (drehwinkel)

title ("turtle - Wikipedia Beispiel Nr. 2")

bgcolor ("black")

pensize (3)

super_rosette (36, 20)

ht ()
