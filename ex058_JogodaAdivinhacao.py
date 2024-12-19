from random import randint
cpu = randint(0, 10)
cont = 0
acertar = False
print('Ola, sou seu computador...... Vamos jogar um jogo ?')
print(' Tente adivinhar um numero inteiro entre 0 e 10...')
while not acertar:
    palpite = int(input('Qual seu palpite ? '))
    cont += 1
    if palpite == cpu:
        acertar = True
    else:
        if palpite < cpu:
            print('>>> MAIS...')
        elif palpite > cpu:
            print('...MENOS <<<')
print('-=-ACERTOU-=- \nQuantidade de Tentativas: {}'.format(cont))






