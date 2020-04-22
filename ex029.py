velCarro = int(input('Quantos Km/h o veículo estava? '))
multa = float((velCarro - 80) * 7)
print('Velocidade informada: {}Km/h.'.format(velCarro))
if velCarro > 80:
    print('Esse veículo foi multado por excesso de velocidade!')
    print('Consta uma multa em aberto no valor de R$ {:.2f}.'.format(multa))
else:
    print('Nada consta!')
