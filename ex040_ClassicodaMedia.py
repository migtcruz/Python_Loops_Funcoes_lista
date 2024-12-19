nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('Nota 1: {} .. Nota 2: {} .. Media: {}'.format(nota1, nota2, media))
if media < 5:
    print('Aluno REPROVADO !!')
elif media >= 5 and media <= 6.9:
    print('Aluno em RECUPERAÇÂO !!!')
else:
    print('Aluno APROVADO !!!!')



