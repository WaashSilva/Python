print ('Base de calculo para pintura')
n1= float (input ('Qual altura da sua parede ? (Ex: 1,2,3,4): '))
n2= float (input ('Qual a largura da sua parde ? ( Ex: 1,2,3,4): '))
n3 = n1 * n2
print (f'A dimensão de sua paerede é {n1}x{n2} e sua área é de {n3}m²')
print (f'Para conseguir pintar {n3}m² de parede, tera de comprar {((n2*n1)/2)}L de tinta')