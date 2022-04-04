# nome  = str(input("Digite seu nome: "))
# if nome == 'Adriano':
#     print('Que nome lindo voce tem!!')
# print(f'Boma dia, {nome} !')
# print('\t---FIM---')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2)/2
print(f'A media das notas são: {media:.1f}')
if media >=6:
    print('Parabens voce passou!')
else:
    print('Que pena! voce reprovou.')
