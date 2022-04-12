from datetime import date
n= int(input('qual ano iremos analizar ?: digite 0 caso seje o ano atual o analisado '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print (f'O ano de {n} é bisexto')
else:
    print(f'O ano de {n} não é bisexto')