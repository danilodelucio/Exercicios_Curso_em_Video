n = int(input('Digite um número: '))
resultado = n % 2
# SIGNIFICA QUE O RESTO DA DIVISÃO DE NÚMEROS PARES SERÃO 0 E DE NÚMEROS ÍMPARES SERÃO 1.

if resultado == 0:
    print('O número {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))