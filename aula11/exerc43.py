print('\t--Calcule seu Índice de Massa Corporal (IMC)--\n')

altura = float(input("Digite sua altura: "))
peso = float(input('Digite seu peso:Kg '))
imc = peso / (altura**2)
print(" ")

if imc < 18.5:
    print(f'Seu IMC:{imc:.1f}\nVocê esta abaixo do peso!')

elif imc <= 25:
    print(f'Seu IMC:{imc:.1f}\nVocê esta com peso ideal !')

elif imc <= 30:
    print(f'Seu IMC:{imc:.1f}\nVocê esta com sobrepeso !')

elif imc <= 40:
    print(f'Seu IMC:{imc:.1f}\nVocê esta com obesidade !')

elif imc > 40:
    print(f'Seu IMC:{imc:.1f}\nVocê esta com obesidade mórbida !')

#print('– IMC abaixo de 18,5: Abaixo do Peso\n– Entre 18,5 e 25: Peso Ideal\n– 25 até 30: Sobrepeso\n– 30 até 40: Obesidade\n– Acima de 40: Obesidade Mórbida\n')
