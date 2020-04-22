milReais = soma = menor = cont = 0
produtos = ''
barato = ''
while True:
    nomeProduto = str(input('Nome do produto: ')).title().strip()
    precoProduto = float(input('Qua o valor do produto? '))
    if precoProduto > 1000:
        milReais += 1
    produtos += nomeProduto + ' - '
    soma += precoProduto
    if cont == 1 or precoProduto < menor:
        menor = precoProduto
        barato = nomeProduto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nDeseja cadastrar outro produto? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print('-' * 50)

print('-' * 50)
print('FIM DA COMPRA')
print(f'O total da compra deu R$ {soma:.2f}.')

# PRODUTOS QUE CUSTARAM MAIS DE R$ 1.000
if milReais == 1:
    print(f'Apenas {milReais} produto custou mais de R$ 1.000.')
elif milReais > 1:
    print(f'Foram {milReais} produtos que custaram mais de R$ 1.000.')

# PRODUTO MAIS BARATO DA COMPRA
print(f'O produto mais barato da compra foi {barato}, e custou R# {menor}')

print('\nLista da compra:')
print(produtos[:-3] + '.')

