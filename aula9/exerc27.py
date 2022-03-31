nome = str(input('\t--Digite um nome completo--\nNome:')).strip()
nomef = nome.split()
print(f'Primeiro nome: {nomef[0].capitalize()}')
print(f'Ultimo nome: {nomef[-1].capitalize()}')