from datetime import date
anoAtual = date.today().year

maiorIdade = 0
menorIdade = 0
anos = 'Datas de Nascimentos registrados: '

for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = anoAtual - ano
    if idade < 18:
        menorIdade += 1
    if idade > 18:
        maiorIdade += 1
    anos += str(ano) + ' - '

print(anos[:-3] + '.')
print('''
Número de pessoas que NÃO ATINGIRAM a maioridade: {}.
Número de pessoas que ATINGIRAM a maioridade: {}.'''.format(maiorIdade, menorIdade))

