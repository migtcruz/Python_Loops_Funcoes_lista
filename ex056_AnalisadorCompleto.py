soma = 0
maioridhomem = 0
nomev = ''
media = 0
cont = 0
for p in range(1, 5):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('Informe seu nome: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe genero (M/F): ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridhomem = idade
        nomev = nome
    if sexo in 'Mn' and idade > maioridhomem:
        maioridhomem = idade
        nomev = nome
    if idade < 20 and sexo in 'Ff':
        cont += 1
media = soma / 4
print('------- RESULTADOS PESQUISA ------')
print('A media de idade do grupo é de {} anos.'.format(media))
print('Homem mais Velho >> Nome: {} Idade: {}'.format(nomev, maioridhomem))
print('Total mulheres abaixo de 20 anos: {}'.format(cont))




