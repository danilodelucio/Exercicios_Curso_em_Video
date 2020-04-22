dist = float(input('Digite a distância de uma viagem em Km: '))
print('Você está prestes à começar a sua viagem de {}Km.'.format(dist))
preço = dist * 0.50 if dist <= 200 else dist * 0.45
'''if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45'''
print('E o preço da sua passagem será de R$ {:.2f}.'.format(preço))
