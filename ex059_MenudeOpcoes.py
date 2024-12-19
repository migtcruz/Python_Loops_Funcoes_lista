n1 = int(input('Informe 1° valor: '))
n2 = int(input('Informe 2º valor: '))
opcao =0
while opcao != 5:
    print('''-=-=- MENU -=-=-
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do Programaa''')
    opcao = int(input('Qual sua opção ? '))
    if opcao == 1:
        soma = (n1 + n2)
        print('O resultado de: {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = (n1 * n2)
        print('O resultado de: {} x {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o MAIOR e: {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o MAIOR e: {}'.format(n1, n2, maior))
        else:
            print('Os numeros sao iguais')
    elif opcao == 4:
        print('-=- INFORME NOVAMENTE OS VALORES -=-')
        n1 = int(input('Informe 1° valor: '))
        n2 = int(input('Informe 2º valor: '))
    elif opcao == 5:
        print('Finalizando.....')
    else:
        print('<> OPCAO INVALIDA <> TENTE NOVAMENTE.')

print('-=-=-=- FIM DO PROGRAMA -=-=-=-')

