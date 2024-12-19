soma = cont = 0
while True:
    n = int(input('Digite o valor (999 to Stop): '))
    if n == 999:
        break
    soma += n
    cont += 1
print("-=-=-=- RESULTADO -=--=-=-")
print(f'Voce digitou {cont} numeros e a soma deles e: {soma}')