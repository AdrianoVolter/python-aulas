print('\t---Quantidade de tinta---')
print("\n")

la = float(input('Qual a altura da parede?\nAltura:'))
ll = float(input('Qual a largura da parede?\nLargura:'))
metros = la * ll
quan_tinta =metros/2
print(f'Altura da parede {la} metros,largura da parede {ll} metros')
print(f'Total {metros} m2')
print(f'Quantidade de tinta {quan_tinta} litros')