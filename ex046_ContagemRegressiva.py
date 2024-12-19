from time import sleep
n = int(input('Digite um valor para contagem regressiva: '))
for c in range(n, -1, -1):
    print(c)
    sleep(0.5)
print('BOOM BOOM POWWW !!!')


