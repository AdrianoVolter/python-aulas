print('\t------------------------------------\n\t---Formação de Triangulos e Tipos---\n\t------------------------------------')
a = float(input('\tDigite o comprimento da reta (a): '))
b = float(input('\tDigite o comprimento da reta (b): '))
c = float(input('\tDigite o comprimento da reta (c): '))
print(" ")   
   
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c) :
    print('Triangulo equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Triangulo isósceles')
else:
    print('Triangulo escaleno')
