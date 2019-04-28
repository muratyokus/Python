print("***Alistirma 8-12***")
def sandivic(*icerik):
    """siparis edilen sandivic icerigi"""
    print(icerik)


sandivic('1','2','3','4','5')
sandivic('elma','armut','karpuz','yer elmasi')
sandivic('sucuklu','maydonoz','ketcap','mayonez')

print("----------Alistirma 8-13----------")

sozluk = {}
def ozelligim(ad, soyad, **ozellik):
    sozluk['adim'] = ad
    sozluk['soyadim'] = soyad
    sozluk['ozelliklerim'] = ozellik

    for anahtar,deger in sozluk.items():
        print(anahtar)
    return sozluk

profil = ozelligim('murat','yokus',tenim='esmer',program='python')
print(profil)