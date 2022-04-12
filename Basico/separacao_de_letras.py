nome= str(input('Digite seu nome completo: ')). strip()
print(f'Seu nome em letras maiuscula é: {nome.upper()}')
print(f'Seu nome em letras minusculas é: {nome.lower()}')
print('Seu nome tem ao todo {} letras'. format(len(nome) - nome.count(' ')))
separa = nome.split()
print ('Seu primeiro nome é: {} e ele tem {} letras'.format(separa[0], len(separa[0])))

print('Vamos agora separar alguns numeros...')
num= int(input('Informe um numero: '))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print (f'unidade: {u} \n Dezena: {d} \n Centena: {c} \n Milhar: {m}')