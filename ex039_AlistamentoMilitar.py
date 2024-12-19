from datetime import date
atual = date.today().year
nasc = int(input('Informe o Ano de Nascimento: '))
idade = atual - nasc
print('Quem naceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce deve se alistar de IMEDIATO !!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar.'.format(saldo))
    ano = atual + saldo
    print('Voce deve alistar se em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce devia ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('Voce devia ter se alistado em {}'.format(ano))
