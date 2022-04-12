import random
from time import sleep
print('\t======GAME==PEDRA==PAPEL==TESOURA======\n')

escolha = str(input('Escolha, PEDRA ,PAPEL ou TESOURA :')).strip()
escolhido = escolha.lower()
maquina = ['pedra','papel','tesoura']
sorteio = random.choice(maquina)

print('JO')
sleep(0.7)
print('KEN')
sleep(0.6)
print('PO!')
sleep(0.6)

if escolhido == sorteio:
    print(f'\nEu {escolhido},maquina {sorteio}\nEMPATE !!')
elif escolhido == 'papel' and sorteio == 'pedra' :
    print(f'Eu {escolhido}.\nMaquina {sorteio}\nVOCE VENCEU !!')
elif escolhido == 'tesoura' and sorteio == 'papel':
    print(f'Eu {escolhido}.\nMaquina {sorteio}\nVOCE VENCEU !!')
elif escolhido == 'pedra' and sorteio == 'tesoura':
    print(f'Eu {escolhido}.\nMaquina {sorteio}\nVOCE VENCEU !!')
else:
    print(f'Eu {escolhido}.\nMaquina {sorteio}\nPERDEU !!')
