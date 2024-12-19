nome = str(input('Gigite seu nome: '))
peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / alt ** 2
print('{}, seu IMC = {:.2f}'.format(nome, imc))
if imc < 18.5:
    print('Abaixo do peso !')
elif imc < 25:
    print('Peso Ideal !')
elif imc < 30:
    print('Sobrepeso !')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida !')
