salario = float(input('Qual o valor do salario? '))

if salario <= 1250:
    novo = (salario * 15 / 100) + salario
    print('Seu salário de R$ {:.2f}, teve um aumento de 15%, sendo ajustado para {:.2f}.'.format(salario, novo))
else:
    novo = (salario * 10 / 100) + salario
    print('Seu salário de R$ {:.2f}, teve um aumento de 10%, sendo reajustado para {:.2f}.'.format(salario, novo))
