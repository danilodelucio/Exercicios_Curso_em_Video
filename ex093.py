dados = dict()
totalGols = 0
golsList = list()

dados['nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(1, partidas+1):
    gols = int(input(f'Quantos gols na partida {p}? '))
    totalGols += gols
    golsList.append(gols)
    dados['gols'] = golsList

dados['total'] = totalGols
print('-' * 50)
print(dados)
print('-' * 50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')

print('-' * 50)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(dados['gols']):
    print(f'Na partida {i+1}, fez {v} gols.')

print('-' * 50)