from time import sleep

sleep(0.5)
print('BEM VINDO À TABUADA DO DANDAN')
print('(Para sair, digite zero (0) à qualquer momento)')
sleep(2)
quant = int(input('Primeiro, digite o valor de quantas vezes você quer multiplicar: '))

while True:
    n = int(input('Digite o número que deseja ver a tabuada: '))
    if n > 0:
        sleep(0.5)
        print('-' * 20)
        for c in range(0, quant+1):
            print(f'{n} x {c} = {n * c}')
        print('-' * 20)
    if n == 0:
        break
print('Tabuada encerrada. Obrigado!')