somaIdade = 0
maiorIdade = 0
nomeVelho = ''
totmulher20 = 0
for p in range(1, 3):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1



mediaIdade = int(somaIdade / 4)
print('A média de idade do grupo de pessoas é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdade, nomeVelho))
print('Ao todo são {} mulher com menos de 20 anos.'.format(totmulher20))