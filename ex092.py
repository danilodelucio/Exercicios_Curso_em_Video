from datetime import date

# datetime.now().year

dados = dict()
anoAtual = date.today().year

dados['nome'] = str(input('Nome: ')).strip().title()
dados['idade'] = anoAtual - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (digite 0 para caso não tenha): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (35 - (anoAtual - dados['contratação'])) + dados['idade']

print(dados)

print('-' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}.')