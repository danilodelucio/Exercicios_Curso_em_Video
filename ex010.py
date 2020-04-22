real = float(input("Quantos reais você quer converter? R$ "))
cotacao = 3.14
aud = real / cotacao
print("Com R$ {:.2f}, você pode comprar AUD {:.2f} seguindo a cotação de hoje: R$ {}.".format(real, aud, cotacao))
