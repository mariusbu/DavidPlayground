#autor: georg
#datum: 21.7.09
#arbeit: dreieck

from xturtle import *

pensize (10)
rt (90)

def dreieck (laenge):
    fd (laenge)
    lt (120)
    fd (laenge)
    lt (120)
    fd (laenge)
    lt (120)

pencolor ("red")

dreieck (65)
lt (120)

pencolor ("green")

dreieck (100)
lt (120)

pencolor ("blue")

dreieck (135)
lt (120)

hideturtle ()
