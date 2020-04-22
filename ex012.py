produto = float(input("Qual o valor do produto? R$ "))
desconto = 5 * produto / 100
valorfinal = produto - desconto
print("O valor do produto é R$ {:.2f}, mas com 5% de desconto ele está saindo por R$ {:.2f}.".format(produto, valorfinal))
