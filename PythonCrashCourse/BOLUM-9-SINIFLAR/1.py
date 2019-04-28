class Restoran():

    def __init__(self, restoran_ismi, mutfak_tipi):

        self.restoran_ismi = restoran_ismi
        self.mutfak_tipi   = mutfak_tipi

    def restoran_tanimi(self):

        #print("Restorant ismi: " + self.restoran_ismi)
        print(self.restoran_ismi.upper() + ', ' + "Restorant mutfak tipi: " + self.mutfak_tipi.upper())

    def acik_restorant(self):
        print("Acik restorant ismi: " + self.restoran_ismi.upper())

restorant = Restoran('Ananin Yeri','Turkish')
restorant.acik_restorant()
restorant.restoran_tanimi()

restorant2 = Restoran('Babanin Yeri','Alman')
restorant3 = Restoran('Adalar','Dominik')

restorant2.restoran_tanimi()
restorant3.restoran_tanimi()


class Kullanicilar():

    ad      =" "
    soyad   =" "

    def ornek_user(self, ad, soyad):

        self.ad     = ad
        self.soyad  = soyad
        print("\n""Kullanici Adi: " + self.ad + '\n' + "Kullanici Soyadi: " + self.soyad)

    def selam_user(self):

        print("\n""Selam ey gidi sevgili user: " + self.ad.upper() + ' ' + self.soyad.upper())

Kullanici = Kullanicilar()
Kullanici.ornek_user('Murat', 'Yokus')
Kullanici.selam_user()