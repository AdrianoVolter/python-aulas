import random
from time import sleep
numero = int(input('Qual numero entre 0 e 5 eu pensei?\nDigite um numero entre 0 e 5: '))
num = random.randint(0, 5)
print('\t---PROCESSANDO---')
sleep(3)
if(num == numero):
    print(f'Parabens voce acertou , o numero era {num}')
else:
    print(f'Que pena ! Voce errou , o numero era {num}')
