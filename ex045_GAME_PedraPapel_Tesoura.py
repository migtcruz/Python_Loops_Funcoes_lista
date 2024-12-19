from random import randint
from time import sleep
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('{:=^30}'.format('JOKENPO'))
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua Escolha ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(1)
print('-=' * 11)
print('Jogador: {}'.format(opcoes[jogador]))
print('Computador: {}'.format(opcoes[computador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE !!!')
    elif jogador == 1:
        print('Jogador VENCEU !!')
    elif jogador == 2:
        print('Computador VENVEU !!')
    else:
        print('JOGADA INVALIDA !! Tente de novo')


elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU !!!')
    elif jogador == 1:
        print('EMPATE !!')
    elif jogador == 2:
        print('Jogador VENVEU !!')
    else:
        print('JOGADA INVALIDA !! Tente de novo')

elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU !!!')
    elif jogador == 1:
        print('Computador VENCEU !!')
    elif jogador == 2:
        print('EMPATE !!')
    else:
        print('JOGADA INVALIDA !! Tente de novo')





