fragen_mit_loesungen = [("Wie heißt die Hauptstadt? ","Bern"),
                        ("Wie heißt die größte Stadt? ","Zuerich"),
                        ("Wieviele Länder grenzen an die Schweiz? ","5"),
                        ("Wieviele Amtssprachen gibt es? ","4"),
                        ("Wie heißt die berühmte Holzbrücke in Luzern? ","Koppelbruecke")]

fragenanzahl = len (fragen_mit_loesungen)

def quiz (fragen_mit_loesungen):
    global punkte
    frage, loesung = fragen_mit_loesungen
    antwort = raw_input (frage)
    if antwort == loesung:
        print "Stimmt genau!"
        print
        punkte = punkte + 1
    else:
        print "Das stimmt leider nicht."
        print "Die Lösung lautet: %s." % (loesung)
    print

punkte = 0

print """Heute wollen wir ein kleines Quiz über ein kleines Land machen.
Nämlich die Schweiz.
Vielleicht weißt Du ..."""
anrede = """Hoppla! Ich weiß ja noch gar nicht wie Du heißt.
Also: Wie heißt Du? """
name = raw_input(anrede)
print """Jetzt nochmal, %s: Vielleicht weißt Du ja genausoviel
über die Schweiz wie ich.
Noch ein Sache, %s: Bitte gib keine Umlaute ein, sondern z.B. ue usw..
Viel Glück, %s!""" % (name, name, name)

for i in fragen_mit_loesungen:
    quiz (i)

if punkte == fragenanzahl:
    print "Fantastisch, %s!" % (name)
    print "Du kannst ja schon fast die schweizer Staatsbürgerschaft beantragen."
elif punkte > fragenanzahl * 0.66:
    print "Ja, ja!"
    print "Du bist ein echter Schweizfan %s. Gut gemacht!" % (name)
elif punkte > fragenanzahl * 0.33:
    print "Nun ja. Die Schweiz gehört nicht gerade zu Deinem Fachgebiet, %s!" % (name)
else:
    print "Schweiz? Nie gehört."
    print "%, Du solltest mal einen Atlas aufschlagen ;-)" % (name)
