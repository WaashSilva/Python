print('Bem Vindo, serei seu assistente para ajudar tua produção')
n1 = str(input('Oque iremos produzir ? = '))
n2 = str(input(f"Há produção de {n1} em atrazo ? \n Exemplo (sim,não) = "))
if n2 == 'sim':
    n10 = int(input(f'Qual a quantidade de {n1} esta em atrazo ? = '))
if n2 == 'nao':
    n10 = 0
qd = int(input(f'Qual a quantidade recebemos hoje de {n1} para produção ? = '))
print()
print('Irei somar a quantidade am atrazo junto das futuras, asssim lhe dar um calculo \n'
      'estatistico de quanto tempo levaremos para acabar com o atraso da produção se houver.')
print()
ht = int(input(f'Quantas horas o setor de {n1} funciona, incluindo horario de descanso ?\n '
               f'Exemplo: (8,10,12) = '))
hd = float(input(f'Quanto tempo o setor de {n1} tem de descanso ?\n'
                 f'Exemplo (Hora = 1.00) (Minutos = 0.05) = '))
n8 = ht - hd
tempo = float(input(f'Quanto tempo leva para produzir 1 unidade de {n1} \n'
                    f'Exemplo (Hora = 1.00) (Minutos = 0.05) = '))
if tempo >= 1:
    n3 = n8 / tempo
if tempo <= 0.9:
    n3 = (n8 * 60) / (tempo * 10)
if tempo <= 0.09:
    n3 = (n8 * 60) / (tempo * 100)
n7 = round(n8)
n5 = n10 + qd
tt= n5/n3
import math
n6 = math.ceil(tt)
n9 = round(n3)
print()
print('Vamos ao calculo:')
print()
print(f'Com a fabrica funcionando:{n7} horas\n-Quatidade do pedido de {n1}:{qd}\n-Quantidade em atrazo de {n1}:{n10}'
      f'\n-Capacidade de produção diaria de {n1}:{n9} unidades\n-Concluiremos a produção, aproximadamente em {n6} dias')
print ()
print ('Desenvolvido por Washington Luiz Silva')