n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL.''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual e {}.'.format(n, hex(n)[2:]))
else:
    print('Valor incorreto, por favor tente novamente!')
