maioridade = homens = mulheres = 0
sepadaror = '-' * 30

while True:
    # INTRO
    print(sepadaror)
    print('CADASTRE UMA PESSOA')
    print(sepadaror)

    idade = int(input('Qual a idade? '))
    #print('Valor inválido, por favor digite novamente!')
    if idade > 18:
        maioridade += 1

    sexo = str(input('Qual o sexo? [M/F]  ')).upper().strip()[0]
    if sexo == 'F' and idade < 20:
        mulheres += 1

    elif sexo == 'M':
        homens += 1

    pergunta = str(input('Deseja cadastrar mais uma pessoa? [S/N]  ')).upper().strip()[0]
    if pergunta == 'N':
        break
    elif pergunta not in 'SN':
        print('Resposta incorreta! Por favor digite novamente!')


print(sepadaror)
print('FIM DO PROGRAMA')
print(f'\nTotal de pessoas com mais de 18 anos: {maioridade}.')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}.')