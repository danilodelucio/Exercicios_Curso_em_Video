dados = dict()
totalGols = 0
golsList = list()
registroGeral = list()

while True:
    # COD / NOME / GOLS / TOTAL DE GOLS
    dados['nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['gols'] = 0
    dados['total'] = 0
    for p in range(1, partidas+1):
        gols = int(input(f'Quantos gols na partida {p}? '))
        golsList.append(gols)
        dados['gols'] = golsList[:]
        dados['total'] += gols

    # CLEAR
    golsList.clear()
    registroGeral.append(dados.copy())
    dados.clear()
    print('-' * 40)

    # SIM OU NAO
    sn = ''
    while True:
        sn = str(input('Deseja cadastrar outro jogador?[S/N] ')).strip().upper()[0]
        if sn not in 'SN':
            print('-' * 40)
            print('ERRO! Por favor digite apenas "S" ou "N".')
        else:
            break

    if sn == 'N':
        break

print('FIM')

print(dados)
print(registroGeral)


print(f'{"Cod":^5} {"Nome":<7} {"Gols":^10} {"Total":>13}')
print('-' * 40)
for i, v in enumerate(registroGeral):
    print(f'{i:^5} {v["nome"]:<11}', end='')
    print(f'{v["gols"]}', end='')
    print(f'{v["total"]:>9}')
