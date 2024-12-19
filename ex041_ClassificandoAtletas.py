from datetime import date
atual = date.today().year
anonasc = int(input('Digite o ano de nascimento:'))
idade = atual - anonasc
if idade <= 9:
    print("Idade: {} .. Categoria: MIRIM".format(idade))
elif idade > 9 and idade <= 14:
    print('Idade: {} .. Categoria: INFANTIL'.format(idade))
elif 14 > idade <= 19:
    print("Idade: {} .. Categoria: JUNIOR".format(idade))
elif 19 > idade <= 25:
    print('Idade: {} .. Categoria: SENIOR'.format(idade))
else:
    print('Idade: {} .. Categoria: MASTER'.format(idade))

