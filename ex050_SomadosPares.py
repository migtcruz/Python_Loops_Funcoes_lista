soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} numero inteiro: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('VC informou {} numero(s) PAR(es) e a soma deles foi: {}'.format(cont, soma))
