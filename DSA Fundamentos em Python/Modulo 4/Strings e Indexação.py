# Criando uma string
'Oi'
'Criando uma string em Python'
'Podemos usar aspas duplas ou simples para strings em Python'
"Testando Strings em 'Python'"

# Imprimindo uma String
print('Testando Strings em Python')
print('Testando \nStrings \nem \nPython')
print('\n')

# Indexando Strings
s = 'Data Science Academy'
print(s)
print('Primeiro elemento da string', s[0])
print('Segundo elemento da string', s[1])
print('Terceiro elemento da string', s[2])
print('Quarto elemento da string',s[3])
print('Quinto elemento da string', s[4])
# Retorna todos os elementos da string, começando pela posição 
# (lembre-se que Python começa a indexação pela posição 0),
# até o fim da string.
print(s[1:])
9# A string original permanece inalterada
print(s)
9# Retorna tudo até a posição de índice 3
print(s[:3])
# Retorna tudo até a posição de índice 4
print(s[:4])
# Nós também podemos usar a indexação negativa e ler de trás para frente
print(s[-1])
# Retornar tudo, exceto a última letra
print(s[:-1])
print(s[::1])
print(s[::2])
print(s[::-1])

# Propriedades da String
# Concatenando strings
s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'
print(s)
# Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'
letra * 3

#funçoes Built in de Strings
s
# Upper Case 
s.upper()
# Lower case
s.lower()
# Dividir uma string por espaços em branco (padrão)
s.split()
# Dividir uma string por um elemento específico
s.split('y')

#Funções String
s = 'seja bem vindo ao universo da Linguagem Python!'
s
s.capitalize()
s.count('a')
s.isalnum()
s.islower()
s.isspace()
s.endswith('o')
s = '1000'
s
type(s)

# Comparando Strings
print("Python" == "R")
print("Python" == "Python")










