print('\t======CALCULO DE MÉDIA======\n')
nota1 = float(input('Nota primeiro bimestre:'))
nota2 = float(input('Nota segundo bimestre:'))

media = (nota1 + nota2) / 2
if media < 5:
    print(f'– Sua media é {media:.2f}.\nMédia abaixo de 5.0: REPROVADO')
elif (media >= 5) and (media < 6.9):
    print(f'– Sua media é {media:.2f}.\nMédia entre 5.0 e 6.9: RECUPERAÇÃO')
elif media >=7:
    print(f'- Sua media é {media:.2F}.\n\t--APROVADO--')

