print ('{:=^49}'.format(' Loja do Xitão '))
a = int(input('Qual o Valor a ser pago ?: '))
b = int(input('''Qual a forma de pagamento ?: \n[1] á vista, dinheiro ou cheque
              \n[2] em 2x no cartão \n[3] mais de 3x no cartão \n[4] á vista no cartão
              \nQual sera a forma de pagamento ?:'''))
b1 = (a-(a*0.10))
b3 = (a+(a*0.20))
b4 = (a-(a*0.05))
if b == 1:
    print (f'O valor a ser pago é de:{b1}')
elif b == 2:
    print (f'O valor a ser pago sera 2x de: {a/2}')
elif b == 3:
    p= int(input('quantas parcelas deseja realizar ?'))
    print (f'O valor a ser pago sera {p}x de: {b3/p}')
elif b== 4:
    print (f'O valor a ser pago é de: {b4}')
else:
    print ('algo de errado acontereu, vamos tentar novmente')
print ('{:=^49}'.format(' Obrigado e volte sempre '))