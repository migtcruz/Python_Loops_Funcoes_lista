h = m = menor = 0
while True:
    print('-' * 20)
    print('CADASTRO DE PESSOAS')
    print('-' * 20)
    id = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if id >= 18:
        m +=1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and id < 20:
        menor += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-=-=-=- RESULTADO PESQUISA -=-=-=-=-')
print(f'Homens cadastrados: {h}')
print(f'Pessoaas acima de 18 anos: {m}')
print(f'Mulheres com menos de 20 anos: {menor}')
