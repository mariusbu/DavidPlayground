
quizdaten = [("Welche Programmiersprache lernst du gerade? ", "Python"),
             ("Mit welchem reservierten Wort beginnt " +
              "eine Funktionsdefinition? " , "def"),
             ("Mit welchem Wort beginnt man eine Schleife? ", "for"),
             ("Wieviel reservierte Wörter hat Python? ", "30")
            ]



def quizfrage(quizeintrag):
    global punkte
    frage, loesung = quizeintrag
    antwort = raw_input(frage)
    if antwort == loesung:
        print "Richtig!"
        punkte = punkte + 1
    else:
        print "Leider falsch!"
        print "Richtig ist:", loesung
    
def quiz(daten):
    global punkte
    print """
Hallo! Du kannst hier ein paar Quizfragen
beantworten, um dein Wissen zu Überprüfen."""
    name = raw_input("Wie heißt du denn? ")
    print "Also viel Glück,", name, "- es geht los!"

    punkte = 0
    fragen_zahl = len(quizdaten)

    for eintrag in quizdaten:
        quizfrage (eintrag)

    print "Du hast", punkte, "von", fragen_zahl, "Punkten erreicht!"

    if punkte == fragen_zahl:
        print "Super,",
    elif punkte > fragen_zahl*0.66:
        print "Fein, du hast schon einiges gelernt,",
    elif punkte > fragen_zahl*0.33:
        print "Na ja. Du solltest nochmal etwas wiederholen,"
    else:
        print "Du stehst noch ziemlich am Anfang,",

    print "%s!" % (name)
    print "Sieh dir doch mal das Python-Video auf der CD an!"

quiz(quizdaten)
