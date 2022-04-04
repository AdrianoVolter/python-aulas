print('\t----------------------------\n\t---Formação de Triangulos---\n\t----------------------------')
a = float(input('\tDigite o comprimento da reta (a): '))
b = float(input('\tDigite o comprimento da reta (b): '))
c = float(input('\tDigite o comprimento da reta (c): '))
print(" ")

if (b - c) < a < b +c and (a - c)< b < a + c and (a - b)< c < a+b :
    print(f'\tAs linhas a,b e c formam um triangulo! ')
else:
    print('\tO comprimento das linhas não formam um triangulo retangulo .')