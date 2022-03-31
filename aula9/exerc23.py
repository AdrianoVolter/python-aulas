num = int(input('Digite um numero entre 0 e 9999: '))
#n1= str(num)
# print(f'Numero digitado: {num}')
# print(f'Unidade = {num[3]}')
# print(f'Dezena = {num[2]}')
# print(f'Centena = {num[1]}')
# print(f'Milhar = {num[0]}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade = {u}')
print(f'Dezena = {d}')
print(f'Centena = {c}')
print(f'Milhar = {m}')
