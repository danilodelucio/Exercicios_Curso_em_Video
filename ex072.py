numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# n = int(input('Digite um número entre 0 e 20:  '))
# while True:
#     if n not in range(0, 21):
#         n = int(input('Valor inválido. Por favor, digite novamente um número entre 0 e 20:  '))
#     else:
#         break
while True:
    n = int(input('Digite um número entre 0 e 20:  '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou {numeros[n]}.')