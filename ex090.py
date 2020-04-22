
ficha = dict()

ficha['Nome'] = str(input('Nome: '))
ficha['Media'] = float(input(f'Média de {ficha["Nome"]}: '))

if ficha['Media'] < 5:
    ficha['Situação'] = 'Reprovado'
elif ficha['Media'] >= 8:
    ficha['Situação'] = 'Aprovado'
else:
    ficha['Situação'] = 'Recuperação'
print('-' * 30)
for k, v in ficha.items():
    print(f'{k} é igual a {v}.')

