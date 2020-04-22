salarioAtual = float(input("Qual o salário do funcionário? R$ "))
porcento = 15
aumento = salarioAtual * porcento / 100
salarioFInal = salarioAtual + aumento
print("O salário de R$ {:.2f}, foi reajustado com 15% de aumento, ficando em R$ {:.2f}".format(salarioAtual, salarioFInal))
