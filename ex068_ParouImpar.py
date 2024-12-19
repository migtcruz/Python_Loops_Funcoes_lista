from random import randint
cont = 0
while True:
    print('-=-' * 15)
    print('JOGO - PAR ou IMPAR')
    print('-=-' * 15)
    num = int(input('Informe o Valor [0-20]: '))
    cpu = randint(0, 21)
    soma = num + cpu
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Escolha PAR ou IMPAR > [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {num} e CPU jogou {cpu}. Total {soma}')
    if soma % 2 == 0 and tipo == 'P':
        print(f'Valor = {soma} é PAR >>>> Voce GANHOU !!')
        cont += 1
    elif soma % 2 == 1 and tipo == 'I':
        print(f'Valor = {soma} é IMPAR >>>> Voce GANHOU !!')
        cont += 1
    else:
        print('Voce PERDEU !!')
        break
print(f'>>>> JOGO ACABOU. Voce ganhou {cont} vez(es) !!')









'''jogue par ou ímpar com o computador. O
 jogo só será interrompido quando o jogador perder, 
 mostrando o total de vitórias consecutivas
  que ele conquistou no final do jogo.'''