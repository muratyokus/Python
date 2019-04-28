#7-4

while True:
    yas = int(input("Yasiniz: \n"))

    if yas < 3:
        print("Bilet 0$")
    elif yas >= 3 and yas <= 12:
        print("bilet 10$")

    elif yas > 12:
        print("Bilet 15$")