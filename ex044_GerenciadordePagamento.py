print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Digite o valor das Compras >> R$: '))
print('''FORMAS DE PAGAMENTO:
[1] Dinheiro / Cheque
[2] Cartao
[3] 2x Cartao
[4] 3x ou mais Cartao''')
opcao = int(input('Informe OPCAO PG: '))

if opcao == 1:
    valor = preco - (preco * 0.10)
    print('Valor R$ {} com 10% desconto: TOTAL R$ {}'.format(preco, valor))
elif opcao == 2:
    valor = preco - (preco * 0.05)
    print("Valor R$ {} com 5% desconto: TOTAL R$ {}".format(preco, valor))
elif opcao == 3:
    valor = preco / 2
    print('Valor R$ {} em 2x cartao de R$ {}'.format(preco, valor))
elif opcao == 4:
    div = int(input('Quantas vezes no cartao ?'))
    valor = preco + (preco * 0.2)
    total = valor / div
    print('Valor R$ {} em {}x no cartao de R$ {}'.format(preco, div, total))
else:
    print('OPCAO INVALIDA de pagamento. Tente novamente !')





