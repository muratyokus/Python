import electric_car
'''
class Restorant():

    def __init__(self, restoran_ismi, mutfak_tipi):

        self.restoran_ismi  = restoran_ismi
        self.mutfak_tipi    = mutfak_tipi

    def restorant_tanimi(self):

        print("Restoran ismi: " + self.restoran_ismi.upper())
        print("Restoran mutfak tipi: " + self.mutfak_tipi.upper())

    def acik_restorant(self):

        print("Acik restorant: " + self.restoran_ismi.title())


class IceCreamStand(Restorant):

    def __init__(self,restoran_ismi,mutfak_tipi):
        super().__init__(restoran_ismi,mutfak_tipi)

    def lezzetler(self):

        self.dondurma = 'Lemon'
        print("Dondurma: " + ' ' + self.dondurma + " 'lu")

restorant = IceCreamStand('De de ye', 'Turk')
restorant.restorant_tanimi()
restorant.lezzetler()'''

#9-9

my_ecar = electric_car


aracim = my_ecar.ElectricCar('Vw', 'Transporter', 2008)

print(aracim.get_descriptive_name())
aracim.battery.get_range()
aracim.battery.upgrade_battery()
aracim.battery.get_range()
