print('\t-|--Calcule o valor a ser pago por um produto--|-\n')
valor = float(input('Valor do produto:R$ '))
print(' ')
print('Forma de pagamento:\n[1]-Pagamento à vista.\n[2]-À vista no cartão.\n[3]-Ate 2x no cartão.\n[4]-3x ou mais no catão.\n')
forma = int(input('QUAL OPÇÃO? :'))

if forma == 1:
    print(f'Valor:R$ {valor - (valor * 0.10)}.\nCom 10% de desconto.')

elif forma == 2:
    print(f'Valor:R$ {valor - (valor * 0.05)}.\nEsta com 5% de desconto.')

elif forma == 3:
    print(f'Valor:R$ {valor}.\nSem juros.')

elif forma == 4:
    vezes = int(input('Em quantas vezes ? :'))
    if vezes == 1:
        print(f'Valor:R$ {valor}.\nSem juros.')
    elif vezes == 2:
        print(f'Valor:R$ {valor / 2} em 2x')
    else:
        print(f'Valor de R$ {(valor + (valor * 0.20)) / vezes} em {vezes} vezes :Total R$ {valor + (valor * 0.20)}.\nCom 20% de juros.')

else:
    print('ATENÇÃO DIGITE UMA OPÇÃO VALIDA')