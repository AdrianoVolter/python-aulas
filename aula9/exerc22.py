nome = str(input('Digite um nome completo: '))
print(f'Nome com as letras maiusculas: {nome.upper()}')
print(f'Nome com as letras minusculas: {nome.lower()} ')
print(f'Seu nome tem {(len(nome) - nome.count(" "))} letras')

#nomef = nome.replace(' ', '')
#print(f'O nome tem {len(nomef)} letras')

nomep = nome.split()
print(f'O primeiro nome é {nomep[0]} e tem {len(nomep[0])} letras')
