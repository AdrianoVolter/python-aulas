nome = str(input('Digite um nome completo: ')).strip()
# nomesil= nome.upper()
# nomef = nomesil.find('SILVA')
#print(f'No seu nome tem Silva?\n \t---{nomef != -1}---')
#print(nomesil)
#print(nomef)

print(f'No seu nome tem Silva?\n\n \t---{"SILVA" in nome.upper()}---\n')