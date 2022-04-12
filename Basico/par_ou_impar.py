n= int(input('selecione um numero qualquer e direi se ele é par ou impar: '))
n1= n % 2
if n1 == 1:
    print (f'O numero escolhido {n} é impar')
else:
    print (f'O numero escolhido {n} é par')