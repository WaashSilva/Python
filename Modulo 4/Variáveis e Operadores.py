# Trabalhando com Variáveis
var_teste_1 = 1
print (var_teste_1)
var_teste_2 = 2
print (var_teste_2)
print (type(var_teste_2))
var_teste_3 = 9.5
print(type(var_teste_3))
x = 1
print(x)

# Declaração Multipla
pessoa1, pessoa2, pessoa3, = 'Bob', 'Maria', 'Ana'
print(pessoa1)
print(pessoa2)
print(pessoa3)
fruta1 = fruta2 = fruta3 = 'Melancia'
print(fruta1)
print(fruta2)
print(fruta3)
x1 = 50
print (x1)

#Variáveis Atribuídas a Outras Variáveis e Order dos Operadores
largura = 2
altura = 4
area = largura *altura
print('area = ',area)
perimetro = 2 * largura + 2 * altura
print('perimetro = ',perimetro)
perimetro2 = 2 * (largura + 2) * altura
print('perimetro2 = ',perimetro2)

# Operações com Variáveis
idade1 = 25
idade2 = 35
print(idade1 + idade2)
print(idade2 - idade1)
print(idade2 * idade1)
print(idade2 / idade1)
print(idade2 % idade1)

# Concatenação de Variáveis
nome = 'Bob'
sobrenome = 'Marley'
fullname = nome + ' ' + sobrenome
print(fullname)