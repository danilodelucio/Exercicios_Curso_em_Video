
print('{:=^40}'.format(' LOJAS LACRAU '))
valorProduto = float(input('Qual o valor do produto? R$ '))


print('''FORMAS DE PAGAMENTO:
      [ 1 ] À vista no dinheiro/cheque: 10% de desconto;
      [ 2 ] À vista no cartão de débito/crédito: 5% de desconto;
      [ 3 ] Em até 2x no cartão: preço normal;
      [ 4 ] 3x ou mais no cartão: 20% de juros;
      ''')
formaPgto = int(input('Qual será a forma de pagamento? '))

if formaPgto == 1:
    desconto = (valorProduto * 10) / 100
    print('À vista no dinheiro/cheque, seu produto de R$ {:.2f}, fica R$ {:.2f} com 10% de desconto.'.format(valorProduto, valorProduto - desconto))
elif formaPgto == 2:
    desconto = (valorProduto * 5) / 100
    print('À vista no cartão de débito/crédito, seu produto de R$ {:.2f}, fica R$ {:.2f} com 5% de desconto.'.format(valorProduto, valorProduto - desconto))
elif formaPgto == 3:
    print('Dividindo 2x no cartão, o seu produto no valor de R$ {:.2f}, você vai pagar 2x de R$ {:.2f}.'.format(valorProduto, valorProduto / 2))
elif formaPgto == 4:
    juros = (valorProduto * 20) / 100
    print('Divindo em 3x ou mais no cartão, o seu produto no valor de R$ {:.2f}, vai ficar R$ {:.2f} (20% de juros).'.format(valorProduto, valorProduto + juros))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
