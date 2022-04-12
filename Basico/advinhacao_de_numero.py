from random import randint
from time import sleep
computador = randint (0,5)
print ('-=-' * 20)
print ('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print ('-=-' * 20)
jogador = int (input('Em qual numero eu pensei ?: '))
print ('Processando...')
sleep (3)
if jogador == computador:
    print ('Parabens! voce conseguiu me vencer')
else:
    print (f'Ganhei ! Eu pensei no numero {computador} e nao no {jogador}')