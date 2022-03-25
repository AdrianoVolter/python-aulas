import math

opo = float(input('Digite o tamanho do cateto oposto:'))
adj = float(input('Digite o tamanho do cateto adjacente: '))

ipo = (opo**2) + (adj**2)
res = math.sqrt(ipo)
print(res)