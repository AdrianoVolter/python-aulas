print('Preço: R$ 0.50 ate 200 Km.\nPreço: R$ 0.45 acima de 200 Km.')

dist = float(input('Qual distancia da viagem?\nDistancia Km: '))

if (dist <= 200):
    print(f'\nValor a pagar: {dist * 0.50 :.2f} R$')
else:
    print(f'\nValor a pagar: {dist * 0.45 :.2f} R$')


