velocidade = float (input('qual a velocidade do carro ?:'))
if velocidade > 80:
    print ('Multado, exedeu o limite de velocidade de 80KM/h')
    print (f'O valor da multa é de {(velocidade - 80) *7}R$ para pagamento em 10 dias uteis')
else:
    print ('Parabens passou ao nosso radar')