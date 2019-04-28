nehirler = {'kizilirmak':'turkiye','nehir2':'hindistan','nehir3':'silikon_vadisi'}

for nehir,ulke in nehirler.items():
    print(nehir + ' ' + 'nehri ' + ulke + ' ' + 'uzerinden gecer.')

print ("\n")
for nehir in nehirler.keys():
    print(nehir)

print ("\n")
for ulke in nehirler.values():
    print(ulke)