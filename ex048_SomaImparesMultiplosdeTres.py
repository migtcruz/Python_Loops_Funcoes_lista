soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('Resultado da soma: {}'.format(soma))
print('Quantidde numeros impares : {}'.format(cont))

