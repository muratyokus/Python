araba = ['transporter','civic','kamyon','bmw','bugatti']
marka = ['vw','audi','honda','mercedes','fiat','tesla']

if 'mercedes' not in araba:
    print(araba == 'mercedes')

if 'bugatti' not in marka:
    print(marka=='bugatti')

for arabalar in araba:
    if arabalar == 'transporter':
        print(arabalar=='transporter')

for markalar in marka:
    if markalar == 'vw':
        print(markalar == 'vw')

    if 'mercedes'.lower() in markalar:
        print('mercedes'.lower() == markalar)

