name = raw_input ("Hi! Wie heißt du? ")
print "Also, ", name,
fach = raw_input ("was ist denn dein bestes Fach? ")
print "Was hattest du für eine Note in", fach,
note1 = raw_input ("in der 1.Klassenarbeit? ")
note2 = raw_input ("Und was hattest du für eine Note in der 2.Klassenarbeit? ")
note3 = raw_input ("Und was hattest du für eine Note in der 3.Klassenarbeit? ")

note1 = float(note1)
note2 = float(note2)
note3 = float(note3)
durchschnitt = ( note1 + note2 + note3) / 3.0

print "Du hast im Fach" , fach, "einen Durchschnitt von", durchschnitt,
