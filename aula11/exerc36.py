emprestimo = float(input('Digite o valor do emprestimo:R$ '))
salario = float(input('Qual valor do seu salario? :R$'))
tempo = float(input('Em quantos para pagar? :'))
porcento = salario * 0.3
meses = tempo * 12

valorparc = emprestimo / meses
print(f'Valor do empestimo: R$ {emprestimo},\nSeu salario: R$ {salario}\nTempo para pagar {tempo} ano(s)')
if (valorparc > porcento):
    print(f'O valor da parcela é R$ {valorparc:.2f} em {meses} meses,\n\t--EMPRESTIMO NEGADO--')

elif(valorparc <= porcento):
   print(f'O valor da parcela é R$ {valorparc:.2f} em {meses} meses,\n\t--EMPRESTIMO APROVADO--')

