print('{:^20}'.format('BRASILEIRÃO 2019'))
classificacao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',
                 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense',
                 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'\nOs 5 primeiros colocados são: {classificacao[:5]}.')
print(f'\nOs 4 últimos colocados são: {classificacao[16:]}')
print(f'\nEm ordem alfabética, a Classificação fica: \n'
      f'{sorted(classificacao)}')
print(f'O Chapecoense está na {classificacao.index("Chapecoense")+1}ª posição.')