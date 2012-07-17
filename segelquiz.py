#autor: georg
#datum: 21.7.09
#arbeit: hobbyquiz

from turtle import *

#einleitung

print """Hallo, liebe Optikinder!
Wir beginnen heute mit einem kleinen Quiz,
dass überprüfen soll, was ihr alles schon wisst!
Ich bin übrigens die Möwe Jonathan."""
name = raw_input ("Und wie heißt Du? ")
print "Na dann Mast- und Schotbruch,", name,", wie der Seemann sagt. "



def quizfrage ():
    global punkte
    antwort = raw_input (frage)
    if antwort == loesung:
        print "Das ist richtig!"
        punkte = punkte + 1
    else:
        print "Hm. das ist leider falsch."
        print "Die richtige Antwort wäre ", loesung, "gewesen. "

punkte = 0
        
frage = "1. Wie nennt man die linke Seite des Bootes? "
loesung = "Backbord"

quizfrage ()

frage = "2. Wie nennt man die Spitze des Bootes? "
loesung = "Bug"

quizfrage ()

frage = "3. Wie nennt man den Windanzeiger, der ganz oben am Mast befestigt ist? "
loesung = "Verklicker"

quizfrage ()

frage = """4. Wie nennt man die Stange, die unten quer vom Mast wegführt,
und an der man sich leicht den Kopf anhaut? """
loesung = "Baum"

quizfrage ()

frage = "5. Wie heißt das Segelmanöver, bei dem der Bug durch den Wind geht? "
loesung = "Wende"

quizfrage ()

frage = "6. Wie nennt man das Schiefwerden des Bootes, wenn der Wind ordentlich pustet? "
loesung = "Kraengen"

quizfrage ()

print "So, ", name, "dann wollen wir mal schauen."

if punkte == 6:
    print "Super,", name, "!"
    print "Du hast", punkte, "von maximal 6 Punkten erreicht."
    print "Du bist ja schon ein richtiger Seemann."
elif punkte >=4:
    print "Gut gemacht, ", name, "!"
    print "Du hast", punkte, "von maximal 6 Punkten erreicht."
    print "Du bist ein Fachmann."
elif punkte >=2:
    print "Nicht schlecht", name, "!"
    print "Du hast", punkte, "von maximal 6 Punkten erreicht."
    print "Du hast schon Grundkenntnisse."
else:
    print name, "Du hast leider nur", punkte, "von maximal 6 Punkten erreicht."
    print "Wer sagt denn, dass man deswegen schlechter segelt? "
