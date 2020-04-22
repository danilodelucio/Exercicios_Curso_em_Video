import datetime
anoNascimento = int(input('Qual ano que você nasceu? '))
idade = (datetime.date.today().year) - anoNascimento

if idade > 18:
    print('Seu tempo de alistamento expirou faz {} anos.'.format(idade - 18))
elif idade < 17:
    print('Você ainda não completou 18 anos. Faltam {} anos para o alistamento.'.format(18 - idade))
else:
    idade == 18;
    print('Seu ano de alistamento é esse ano!')
