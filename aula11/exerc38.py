print(' ')
num1 = int(input('Digite um numero inteiro:'))
num2 = int(input('Digite outro numero inteiro:'))

if num1 > num2 :
    print(f'O primeiro numero maior.\n{num1} é maior que {num2}')
elif num2 > num1:
    print(f'O segundo numero maior.\n{num2} é maior que {num1}')
else:
    print(f'O primeiro numero e o segundo numero são iguais.\n{num1} é igual {num2}')
