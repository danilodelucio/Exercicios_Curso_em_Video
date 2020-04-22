from random import randint
from time import sleep
n = int(randint(0, 5))
user = int(input('Qual número que estou pensando? '))
print('PROCESSANDO...')
sleep(2)

if user == n:
    print('Parabéns mizeravi, você acertou!')
else:
    print('Que pena, você perdeu sonso!')
print('O número pensado foi {}.'.format(n))
