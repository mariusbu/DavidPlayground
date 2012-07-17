
quizdaten=[("Wie nennt man die Spitze des Bootes? ", "Bug"),
           ("Wie nennt man das Ende des Bootes? ", "Heck"),
           ("Wie nennt man das Brett, das in der Mitte " +
            "unten aus dem Boot herausguckt? ", "Schwert"),
           ("Was heißt rechts in seemännisch? " , "steuerbord"),
           ("Wie heißt der Windrichtungsanzeiger, "+
            "der ganz oben am Mast befestigt wird? ","Verklicker"),
           ("Wie nennt man den Stab, den man in der Hand hält, "+
            "um das Boot zu steuern? ","Pinnenausleger")]

fragenzahl = len(quizdaten)

def quizfrage(quizeintrag):
    global punkte
    frage, loesung = quizeintrag
    antwort = raw_input(frage)
    if antwort == loesung:
        print "Jop!"
        punkte = punkte + 1
    else:
        print "Nö! Falsch!"
        print "Richtig wäre %s gewesen." % (loesung)

punkte = 0

print """Hallo, liebe Segelkinder!
Heute wollen wir ein kleines Quiz machen,
um zu testen, wieviel ihr schon wißt."""
frage = "Wie heißt Du denn eigentlich? "
name = raw_input(frage)

print "Na dann Mast und Schotbruch, %s, wie der Seemann sagt." % (name)

for eintrag in quizdaten:
    quizfrage (eintrag)

if punkte == fragenzahl:
    print "Supi, %s!" % (name)
    print "Du bist ja schon fast ein richtiger Kapitän."
elif punkte > fragenzahl * 0.75:
    print "Gut, gut, %s!" % (name)
    print "Dir fehlt nicht mehr viel zum 1. Offizier."
elif punkte > fragenzahl * 0.5:
    print "Nicht schlecht, %s!" % (name)
    print "Bald kannst Du auch auf die Kommandobrücke."
elif punkte > fragenzahl * 0.25:
    print "Hui!"
    print "Da fehlt aber noch ne Menge, %s!" % (name)
    print "Aber auch als Smutje hat man sicher Spaß."
else:
    print "O je!"
    print "Lieber %s, vielleicht solltest Du Dir ein anderes Hobby suchen?!" % (name)
