
print('\n')
print('\t--CONVERTER NUMERO INTERIRO EM BINARIO, OCTAL ou HEXADECIMAL--\n')

numero = int(input('Digite um numero para converter:'))
print('Conversão?\n-[1]Binario-\n-[2]Octal-\n-[3]Hexadecimal- ')
escolha = int(input("Escolher uma opção:"))

if escolha == 1:
    print(f'Escolheu opção 1, o valor de {numero} em binario: {bin(numero)[2:]}')
elif (escolha == 2):
    print(f'Escolheu opção 2, o valor de {numero} em octal: {(oct(numero)[2:])}')
elif escolha == 3:
    print(f'Escolheu opção 3, o valor de {numero} em hexadecimal: {hex(numero)[2:]}')
elif escolha < 1 or escolha >3:
    print('\t--VALOR DIGITADO INVALIDO--\nDigite somente 1 ou 2 ou 3 ')

# if escolha == 1:
#     convertido = "{0:b}".format(numero)
#     print(f'Escolheu opção 1, o valor de {numero} em binario: {convertido}')
# elif (escolha == 2):
#     convertido = "{0:o}".format(numero)
#     print(f'Escolheu opção 2, o valor de {numero} em octal: {convertido}')
# elif escolha == 3:
#     convertido = "{0:x}".format(numero)
#     print(f'Escolheu opção 3, o valor de {numero} em hexadecimal: {convertido}')
# elif escolha < 1 or escolha >3:
#     print('\t--VALOR DIGITADO INVALIDO--\nDigite somente 1 ou 2 ou 3 ')