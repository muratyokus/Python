#7-8
sandivic_siparis = ['pastirma','etli','kofteli','pastirma','sade','soslu','acili','pastirma']
hazir_sandivic   = []

'''
while True:
    hazir_sandivic = sandivic_siparis.pop()

    for sandivic_siparis in 'pastirma':
        if sandivic_siparis in 'pastirma':
            print(hazir_sandivic + ' ' + 'hazirlandi, teslimat icin hazir!')

    if sandivic_siparis in 'pastirma':
        print("pastirmali sandivic bitti!")
        break
    else:
        continue
'''


'''while sandivic_siparis:
    hazir_sandivic = sandivic_siparis.pop()
    print(hazir_sandivic + ' ' + 'hazirlandi, teslimat icin hazir!')
'''


soru = "Dunyayi gezmek isteseydiniz nereye gitmek isterdiniz ?"
anket = []

while True:
    anket = input("Cevap: ")

    if len(anket) == 5:
        print("Anket maximum sayiya ulasti.")
        break
    else:
        print(anket)
        continue
