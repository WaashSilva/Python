a= int(input('digite um numero qualquer: '))
b= int(input('digite outro numero qualquer: '))
c= int(input('digite outro numero qualquer: '))
menor= a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior= a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'o maior valor é {maior}, menor valor é {menor}')