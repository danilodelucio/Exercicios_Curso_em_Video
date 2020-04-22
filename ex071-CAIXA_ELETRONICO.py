print('=' * 30)
print('{:^30}'.format('BANCO 100 GRANA'))
print('=' * 30)
valor = int(input('Que valor deseja sacar? R$  '))
total = valor
nota = 50
totalNota = 0
while True:
    if total >= nota:
        total -= nota
        totalNota += 1
    else:
        if totalNota > 0:
            print(f'Total de {totalNota} cédulas de R$ {nota}.')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalNota = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre!')