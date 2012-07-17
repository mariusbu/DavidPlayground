#autor: georg
#datum: 21.7.09
#arbeit: quiz

def quizfrage ():
    global punkte
    antwort = raw_input (frage)
    if antwort == loesung:
        print "Richtig!"
        punkte = punkte + 1
    else:
        print "Leider falsch!"
        print "Richtig ist:", loesung
    print

print """Hallo!
Du kannst hier ein paar Quizfragen beantworten,
um dein Wissen zu überprüfen"""
name = raw_input ("Wie heißt Du denn? " )
print "Also viel Glück,", name,", es geht los"

punkte = 0

#frage 1

frage = "Welche Programmiersprache lernst Du gerade? "
loesung = "Python"

quizfrage ()

#frage 2

frage = "Mit welchem Wort beginnt eine Funktionsdefinition? "
loesung = "def"

quizfrage ()

#frage 3

frage = "Wie viele reservierte Worte hat Python? "
loesung = "30"

quizfrage ()

if punkte == 3:
    print "Super", name, "! Du hast", punkte, "von 3 Punkten erreicht."
elif punkte > 0:
    print "Nicht schlecht", name, "! Du hast", punkte, "von 3 Punkten erreicht."
else:
    print "Schluck!", name, "Du hast", punkte, "von 3 Punkten erreicht."
    print "Ich glaube, Du solltest noch mal wiederholen. "
