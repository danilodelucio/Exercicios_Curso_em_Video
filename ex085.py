listaCompleta = [[], []]
r = 0
for c in range(1, 8):
    r = int(input(f'Digite o {c}º valor: '))
    listaCompleta.append(r)
    if r % 2 == 0:
        listaCompleta[0].append(r)
    elif r % 2 == 1:
        listaCompleta[1].append(r)

print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(listaCompleta[0])}.')
print(f'Os valores ímpares digitados foram: {sorted(listaCompleta[1])}.')
