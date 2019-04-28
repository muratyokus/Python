'''kiralik_arac = ("Ne tur bir araba kiralamak istersiniz ?\n")
kiralik_arac = input(kiralik_arac)
print("\nSeni bulabilecek miyim, " + ' ' + kiralik_arac + ' ' + "bakalim.")

#7.2
kisi_sayisi = ("Aksam yemeginde kac kisi olacak ? ")
kisi_sayisi = int(input(kisi_sayisi))

if kisi_sayisi > 8:
    print("Masa beklemeniz gerekiyor.")
else:
    print("Masaniz hazir.")
'''
#7.3
sayi = int(input("Bir sayi girin: "))

if sayi%10 == 0:
    print("Sayi 10'un katidir.")

else:
    print("Sayi 10'un kati degil.")
