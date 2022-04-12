
import datetime

print('\n\tLeia o ano de nascimento de um atleta e mostre sua categoria\n')

ano = int(input('Digite o ano de nascimento:'))
data = datetime.date.today()
anoatual = int(data.strftime("%Y"))
idade =anoatual -ano

if idade <= 9:
    print(f'O atleta tem  ou vai fazer {idade} anos,\n\tCATEGORIA MIRIM !! ')

elif (idade >9) and (idade <= 14): 
     print(f'O atleta tem ou vai fazer {idade} anos.\n\tCATEGORIA INFANTIL !!')

elif (idade <= 19) and (idade > 14)  :
     print(f'O atleta tem ou vai fazer {idade} anos.\n\tCATEGORIA JÚNIOR !!')

elif (idade > 19) and (idade <= 25):
    print(f'O atleta tem ou vai fazer {idade} anos.\n\tCATEGORIA SÊNIOR !!')
    
elif idade > 25:   
    print(f'O atleta tem ou vai fazer {idade} anos.\n\tCATEGORIA MASTER !!')