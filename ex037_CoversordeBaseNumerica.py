num = int(input('Digite um numero inteiro: '))
print('''Escoha a base para conversao :
1 - BINARIO
2 - OCTAL
3 - HEXADECIMAL''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print('Numero {} .. Conversao BINARIO = {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print("Numero {} .. Conversao OCTAL = {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print('Numero {} .. Conversao HEXADECIMAL = {}'.format(num, hex(num)[2:]))
else:
    print('Opçao INVALIDA !! Tente de novo ...')
