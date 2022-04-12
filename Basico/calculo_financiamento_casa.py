print ((5*'-'),'\033[34mCredito Imobiliario Washington Silva\033[m',(5*'-'))
print ((10*'-'),'\033[33mVamos a os teus dados\033[m',(10*'-'))
ordenado= float(input('Qual o teu ordenado mensal ? (valor liquido): '))
valor= float(input('Qual o valor do Imovel ? (100000) '))
tempo= int(input('Em quantos anos pretende pagar a casa ?: '))
print ((10*'-=-'),('Calculando'),(10*'-='))
co= (ordenado*0.3)
tp= (tempo*12)
vp= (valor/tp)
print (('O tempo total de pagamento do imovel sera de'), (f'\033[31m{tp}\033[m'),('meses \ncom parcelas mensais de'),
       (f'\033[31m{vp:.2f}\033[m'),('R$, com validade todos os dias 5 de cada mês'))
if co > vp:
    print('\033[32mPARABENS CRÉDITO APROVADO\033[m')
else:
    print(('\033[31mINFELISMENTE NAO CONSEGUIREMOS AVANÇAR COM O CRÉDITO\033[m'), (f'\nO valor maximo da parcela teria '
                                                                                  f'de ser {co}R$ para o crédito ser aprovado'))