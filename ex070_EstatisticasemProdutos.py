total = maiorpreco = menorpreco = cont = 0
while True:
    print('---- LOJA BARATAO ----')
    produto = str(input('Nome Produto: '))
    preco = float(input('Preço R$: '))
    resp = ' '
    total += preco
    cont += 1
    if preco > 1000:
        maiorpreco += 1
    if cont == 1 or preco < menorpreco:
        produtomenor = produto
        menorpreco = preco
    while resp not in 'SN':
        resp = str(input('Contunuar ? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('---- RESULTADO COMPRA ------')
print(f'TOTAL COMPRA: R$ {total}')
print(f'QTDE PRODUTOS acima de R$ 1000,00: {maiorpreco}')
print(f'PRODUTO MAIS BARATO {produtomenor} <> PREÇO R$: {menorpreco}')
