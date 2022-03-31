cidade = str(input('Nome da cidade: ')).strip()

print(f'A cidade possui Santo no nome: {cidade[:5].upper() == "SANTO"}')
print(f'O nome da cidade digitado :{cidade.title()}')
