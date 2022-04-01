print ('Vamos tratar da % de reajuste salarial do ano')
n0= str(input('Qual o nome do(a) funcionario(a) ?: '))
n1= float(input(f'Qual o valor do ordenado do {n0} (Ex: 1000.00): '))
n2= str (input('O valor a ser reajustado se trata de % ou valor inteiro ? '))
if n2 == '%':
    n4= float (input('Qual a porcentagem a ser reajustada ? '))
    print (f'O novo ordenado do(a): {n0}, sera: ${n1+(n1*n4/100)}')
else:
    n3= float (input (f'Qual o valor a ser reajustado ? '))
    print (f'O novo ordenado do(a): {n0}, sera: ${n1+n3}')