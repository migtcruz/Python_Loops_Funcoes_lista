'''from math import factorial
n = int(input('Digite o numero a ser fatotado: '))
f = factorial(n)
print('O fatorial de {}! é:  {}'.format(n, f))'''
from time import sleep
n = int(input('Digite o numero a ser fatotado: '))
c = n
f = 1
print('Calculando Fatorial de {}! >>> '.format(n), end='')
sleep(1)
while c > 0:
    print('{} '.format(c), end='')
    if c > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))





