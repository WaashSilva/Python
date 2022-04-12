n= int(input('Qual a distancia da viagem a percorrer para calcularmos o valor:'))
if n> 199:
    print (f'o valor da sua viagem sera de {n * 0.45}R$')
else:
    print (f'O valor de sua passagem sera de {n * 0.50}R$')