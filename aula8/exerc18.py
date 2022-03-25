import math


angulo = float(input('Digite o valor de um angulo: '))
cose = math.degrees(math.cos(angulo))
seno = math.degrees(math.sin(angulo))
tang = math.degrees(math.tan(angulo))

print(f'Angulo digitado {angulo} graus.\nO coseno do angulo {cose} graus.\nO seno do angulo {seno} graus.\nO tangente é {tang} graus.')
