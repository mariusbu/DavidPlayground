#autor: georg
#datum: 21.7.09
#arbeit: wabe

from xturtle import *

def dreieck ():
    rt (30)
    fd (seite)
    lt (120)
    fd (seite)
    lt (120)
    fd (seite)
    lt (150)

pensize (4)
seite = 60

dreieck ()

rt (180)

dreieck ()

seite = 2 * seite

rt (90)

dreieck ()

rt (180)

dreieck ()
