casa = float(input('Informe o valor da casa: R$ '))
sal = float(input('Informe sua renda mensal: R$ '))
temp = int(input('Informe o tempo de parcelento em anos: '))
prest = casa / (temp * 12)
minimo = sal * 0.30
print('Para financiar uma casa de R$ {:.2f} em {} anos'.format(casa, temp), end='')
print(' a prestacao mensal sera de R$ {:.2f} '.format(prest))
if prest <= minimo:
    print('Financiamento APROVADO !!!')
else:
    print('Financiamento NAO APROVADO !!!!')
