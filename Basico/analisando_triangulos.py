print ('Analisador de triangulos')
print ('-='*20)
r1= float (input('Comprimento da primeira linha: '))
r2= float (input('Comprimento da segunda linha : '))
r3= float (input('Comprimento da terceira linha: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos acima podem formar um triangulo')
else:
    print ('Os segmentos acima nao podem formar um triangulo')