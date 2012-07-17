def quizfrage():
    global punkte
    global loesung3
    antwort = raw_input(frage)
    if antwort == loesung1:
        print "Das ist richtig!"
        punkte = punkte + 1
    elif antwort == loesung2:
        print "Das ist richtig!"
        punkte = punkte + 1
    else:
        print "Das ist leider falsch!"
        print "Richtig ist:" , loesung1
    print

punkte = 0

name = raw_input ("""Hallo!!Hier bei diesem Quiz kannst du dein
Wissen über Tischtennis testen. Wie heißt du eigentlich? """)
print "Na dann kann es ja los gehen," ,name
print """Ach übrigens! Schreibe alle deine Antworten bitte mit ü,ä,ö und ß
und du kannst wählen ob du als Antwort a,b,c, oder d nimmst
oder ob du richtige Wörter benutzt. """

frage = """Wie heißt die rote Seite des Schlägers?
a Rückseite b Vorhand c Rückhand d Vorseite """ 
loesung1 = "Vorhand"
loesung2 = "b"
quizfrage()

frage = """Welche Farbe hat die Rückhandseite auf dem Schläger?
a blau b grün c schwarz d rot """ 
loesung1 = "schwarz"
loesung2 = "c"
quizfrage()

frage = """Wie groß ist der Durchmesser eines Balls?
a 50mm b 45mm c 30mm d 40mm """ 
loesung1 = "40mm"
loesung2 = "d"
quizfrage()

frage = """Wie lang ist eine offizielle Tischtennisplatte?
a 1.60m b 2.70m c 2.40m d 3.00m """ 
loesung1 = "2.70m"
loesung2 = "b"
quizfrage()

frage = """Mit einem dicken Schwamm unter dem Belag fliegt der Ball...
a ...langsam b ...normal c ...schnell d ...gar nicht """
loesung1 = "schnell"
loesung2 = "c"
quizfrage()

if punkte == 5:
    print "Super,"
elif punkte > 0:
    print "Fein,"
else:
    print "Oh,"

print name, ",du hast",
print punkte, "von 5 möglichen Punkten erreicht!"
