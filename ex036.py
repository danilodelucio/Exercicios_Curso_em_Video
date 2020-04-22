casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual sua renda mensal? R$ '))
anos = int(input('Em quantos anos deseja financiar? '))
prestacaoMensal = casa / ( 12 * anos )

print('-=-' * 25)
print('DADOS INFORMADOS:')
print('Valor da residência: R$ {:.2f}.'.format(casa))
print('Renda mensal: R$ {:.2f}.'.format(salario))
print('Tempo de financiamento: {} anos.'.format(anos))
print('-=-' * 25)

if prestacaoMensal > salario * 30 / 100:
    print('Seu financiamento foi negado, o valor excede 30% do salário informado.')
else:
    print('PARABÉNS! Você está apto para realizar o financiamento!')
