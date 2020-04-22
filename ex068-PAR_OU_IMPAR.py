from random import randint
from time import sleep

valueDash = 100
print('-' * valueDash)
print('Bem vindo ao jogo!')
print('-' * valueDash)

# Acumuladores
vitorias = cpu = n = 0

while True:
    # Palpite CPU
    cpu = int(randint(0, 10))

    # Palpite Usuário
    user = str(input('\nPAR ou ÍMPAR?\n\n[Digite "p" para "PAR" ou "i" para "ÍMPAR"]: ')).upper().strip()[0]
    n = int(input('Digite o seu palpite: '))

    soma = cpu + n
    pi = soma % 2

    # Descobrindo se deu PAR ou ÍMPAR
    if pi == 1:
        print('=' * valueDash)
        resultado = 'IMPAR'
    elif pi == 0:
        print('=' * valueDash)
        resultado = 'PAR'

    sleep(0.5)

    if resultado[0] == user:
        vitorias += 1
        print(f'Parabéns, você acertou! Deu {resultado}.\nVamos para a próxima...')
        print('=' * valueDash)

    else:
        print(f'\nQue pena, você errou! Deu {soma} → {resultado}.')
        break


# MENSAGENS FINAIS
print(f'O número que eu pensei foi {cpu}, e o que você escolheu foi {n} (somando os dois fica {soma}).')
print(f'Número de vitórias: {vitorias}.')
print('\n[Fim de jogo]')
print('-' * valueDash)