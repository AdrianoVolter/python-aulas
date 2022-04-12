import datetime
print('\n--ALISTAMENTO MILITAR--\n')
ano = int(input('Digite o ano de nascimento:'))
data = datetime.date.today()
anoatual = int(data.strftime("%Y"))
idade = anoatual - ano

if (anoatual - ano) ==18:
    print(f'Voce tem ou vai fazer {idade} anos,\nALISTE-SE NO SERVIÇO MILITAR !! ')

elif (idade >18) and (idade <= 21):
    passou = idade - 18
    print(f'Voce tem ou vai fazer {idade} anos.\nJá passou {passou} anos do seu alistamento.\nVÁ SE ALISTAR!')
    print(f'Ano do seu alistamento foi : {anoatual - passou}')
elif (anoatual - ano) < 18 :
    falta = 18 - (anoatual - ano)
    print(f'Voce tem ou vai fazer {idade} anos.\nAinda falta {falta} ano(s) para seu alistamento')
    print(f'Ano do seu alistamento: {falta + anoatual}')

elif (anoatual - ano) > 21:
    passou = idade - 18
    print(f'Voce tem ou vai fazer {idade} anos , provavelmente voce ja se alistou-se !')
    print(f'Ano do seu alistamento foi: {anoatual - passou}')