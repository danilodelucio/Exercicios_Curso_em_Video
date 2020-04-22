lista = []
dado = []
maiskg = menoskg = 0
pessoaGorda = pessoaMagra = ''
while True:
    dado.append(str(input('Nome: ')).title().strip())
    dado.append(int(input('Peso(Kg): ')))
    if len(lista) == 0:
        maiskg = menoskg = dado[1]
    else:
        if dado[1] > maiskg:
            maiskg = dado[1]
        if dado[1] < menoskg:
            menoskg = dado[1]
    lista.append(dado[:])
    dado.clear()
    sn = str(input('Deseja cadastrar mais alguma pessoa? [S/N]   ')).upper().strip()
    if sn == 'N':
        break

print('-' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maiskg:.2f} Kg. Peso de: ', end='')
for p in lista:
    if p[1] == maiskg:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menoskg:.2f} Kg. Peso de: ', end='')
for p in lista:
    if p[1] == menoskg:
        print(f'[{p[0]}] ', end='')
print()
