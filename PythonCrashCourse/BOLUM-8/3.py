#8-9

sihirbazlar = ['Murat','Hacer','Aybora','AyTurk','Aysa']
bos_sihirbaz = []
def show_magicians(sihirbazlar):
    for sihirbaz in sihirbazlar:
        print(sihirbaz)

def make_great(sihirbazlar):

    for sihirbaz in sihirbazlar:
        #print(sihirbaz)
        #sihirbazlar1 = sihirbaz.pop()
        bos_sihirbaz.append('Great' + ' '+sihirbaz)

    for dolu_sihirbaz in bos_sihirbaz:
        print(dolu_sihirbaz)

show_magicians(sihirbazlar)
make_great(sihirbazlar)