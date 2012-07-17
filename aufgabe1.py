from turtle import *
    

def dreieck (laenge):
    fd (laenge)
    lt (120)
    fd (laenge)
    lt (120)
    fd (laenge)

def viereck (laenge):
    fd (laenge)
    lt (90)
    fd (laenge)
    lt (90)
    fd (laenge)
    lt (90)
    fd (laenge)

def zeichne (figur, laenge):
    if figur == "Dreieck":
        print dreieck (laenge)
    elif figur == "Viereck":
        print viereck (laenge)
    else:
        print "Wähle 'Dreieck' oder 'Viereck'!"

print "Hallo lieber Matheschüler."
print "Hier kannst Du etwas ausprobieren."
figur = raw_input ("Willst Du lieber ein Dreieck, oder ein Viereck zeichnen? ")
laenge = raw_input ("Welche Seitenlänge soll die Figur haben? ")
laenge = float (laenge)
zeichne (figur, laenge)
    
    





    
    
