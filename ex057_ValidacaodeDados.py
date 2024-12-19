sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Invalidos. Digite sexo [M/F]: ')).strip().upper()[0]
print('Sexo -{}- Registrado com sucesso'.format(sexo))





