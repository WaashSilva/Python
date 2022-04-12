print ('Ola, irei lhe ajudar a fazer o calculo da porcentagem da tua proxima compra')
n1= float(input('Qual o valor do produto que pretende comprar (Ex: 10.99) ?: '))
n2= float(input('Qual o valor de % de desconto a ser aplicado no produto ?: '))
n3= n1*n2/100
n4= n1 - n3
print (f'O valor final do produto com valor de {n1}$ aplicado o desconto de {n2}% que é = a {n3}$ resulta em {n4}$ a ser pago')