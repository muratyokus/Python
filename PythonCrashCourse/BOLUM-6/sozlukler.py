arkadas = {'Ad':'Murat','Soyad':'YOKUS','Memleket':'Adana','Yas':'23','Uyruk':'T.C'}
favori_numara = {'Murat':'7','Mehmet':'1','Ahmet':'2','Selman':'3','Rasul':'4'}
print(arkadas['Ad'])
print(arkadas['Soyad'])
print(arkadas['Memleket'])
print(arkadas['Yas'])
print(arkadas['Uyruk'])

arkadas['Yas'] = '22'
print(str(arkadas['Yas']))

arkadas['Meslek'] = 'siber guvenlik meraklisi'
print(arkadas['Meslek'].title()+'\n')
print(arkadas['Meslek'].upper()+'\n')
print(arkadas['Meslek'].capitalize()+'\n')
print(arkadas['Meslek'].swapcase()+'\n')
print(len(arkadas['Meslek']),'\n')


print('Murat in favori numarasi: '+favori_numara['Murat']+'\n'
      'Mehmet in favori numarasi: '+favori_numara['Mehmet']+'\n'
      'Ahmet in favori numarasi: '+favori_numara['Ahmet']+'\n'
      'Selman in favori numarasi: '+favori_numara['Selman']+'\n'
      'Rasul un favori numarasi: '+favori_numara['Rasul'])
