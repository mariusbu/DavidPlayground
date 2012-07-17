#autor: georg
#datum: 21.7.09
#arbeit: wabe

from turtle import *

def sechseck ():
    fd (seite)
    rt (120)
    pd ()
    begin_fill ()
    fd (seite)
    rt (60)
    fd (seite)
    rt (60)
    fd (seite)
    rt (60)
    fd (seite)
    rt (60)
    fd (seite)
    rt (60)
    fd (seite)
    end_fill ()
    pu ()
    home ()

def drehung ():
    fd (seite)
    rt (60)
    fd (seite)

color ("brown", "yellow")
pensize (4)
seite = 60

pu ()

sechseck ()

drehung ()

color ("brown", "orange")

sechseck ()

rt (60)
drehung ()

sechseck ()

rt (120)
drehung ()

sechseck ()

rt (180)
drehung ()

sechseck ()

rt (240)
drehung ()

sechseck ()

rt (300)
drehung ()

sechseck ()

hideturtle ()
