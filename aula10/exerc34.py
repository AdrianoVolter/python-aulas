salario = float(input('Digite um valor de salario R$ '))

if (salario > 1250.00):
    reajustado = (salario * 0.10) + salario
    print(f'O salario teve 10% aumento, o valor ficou em : {reajustado} R$')
else:
    reajustado = (salario * 0.15) + salario
    print(f'O salario teve 15% de aumento, o valor ficou em : {reajustado} R$')