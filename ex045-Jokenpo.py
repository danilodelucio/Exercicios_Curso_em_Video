from random import randint
from time import sleep

print('''
BEM VINDO AO JOKENPÔ

[ 0 ] PEDRA;
[ 1 ] PAPEL;
[ 2 ] TESOURA;
''')

itens = ('Pedra', 'Papel', 'Tesoura')
cpu = int(randint(0, 2))
user = int(input('Faça a sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 15)
print('O computador escolheu {}.'.format(itens[cpu]))
print('Você escolheu {}.'.format(itens[user]))
print('-=' * 15)

if cpu == 0: # CPU JOGOU PEDRA
    if user == 0:
        print('JOGO EMPATADO!')
    elif user == 1:
        print('VOCÊ VENCEU!')
    elif user == 2:
        print('VOCÊ PERDEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu == 1: # CPU JOGOU PAPEL
    if user == 0:
        print('VOCÊ PERDEU!')
    elif user == 1:
        print('JOGO EMPATADO!')
    elif user == 2:
        print('VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu == 2: # CPU JOGOU TESOURA
    if user == 0:
        print('VOCÊ VENCEU!')
    elif user == 1:
        print('VOCÊ PERDEU!')
    elif user == 2:
        print('JOGO EMPATADO')
    else:
        print('JOGADA INVÁLIDA!')
