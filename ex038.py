n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('-=-' * 10)
print('Número 01: {}.'.format(n1))
print('Número 02: {}.'.format(n2))

if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O segundo número é maior.')
else:
    print('Não exite valor maior, os dois são iguais.')
