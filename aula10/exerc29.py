vel = float(input('A velocidade que voce andou :  '))
print(f'Velocidade é ; {vel} km/h')
if(vel > 80 ):
    print(f'Voce ultrapassou a velocidade,\nVoce foi multado em: R$ {(vel - 80)*7}')
else:
    print('Tudo Ok!')