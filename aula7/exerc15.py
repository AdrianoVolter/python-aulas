dias = float(input('Dias alugado = '))
km =float(input('Kilometragem rodada ='))
diast =dias * 60
kmt = km * 0.15
total = diast + kmt
print(f'O carro ficou {dias} dias.\nRodou {km} km.\nCusto total a pagar é R$ {total}')