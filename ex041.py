import datetime
anoNascimento = int(input('Que ano você nasceu? '))
idade = (datetime.date.today().year) - anoNascimento

''' 
TABELA CATEGORIAS
- ATÉ 9 ANOS: MIRIM
- ATÉ 14 ANOS: INFANTIL
- ATÉ 19 ANOS: JUNIOR
- ATÉ 20 ANOS: SÊNIOR
- ACIMA DE 20 ANOS: MASTER
'''

print('Você tem {} anos.'.format(idade))

if idade <= 9:
    print('Você faz parte da categoria MIRIM!')
elif 9 < idade <= 14:
    print('Você faz parte da categoria INFANTIL!')
elif 14 < idade <= 19:
    print('Você faz parte da categoria JUNIOR!')
elif idade == 20:
    print('Você faz parte da categoria SÊNIOR!')
elif idade > 20:
    print('Você faz parte da categoria MASTER!')
