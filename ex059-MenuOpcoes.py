print(('=' * 20) + ' SEJA BEM VINDO ' + ('=' * 20))

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

valoresRegistrados = str(n1) + ' e ' + str(n2)
print('Valores registrados: ' + valoresRegistrados + '.')

menu = print(('-' * 20) + '''
ESCOLHA A OPERAÇÃO
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''' + ('-' * 20))

escolha = 0
while escolha != 5:
    escolha = int(input('Qual operação deseja fazer? '))
    if escolha == 1:
        somar = n1 + n2
        print('A soma dos valores informados ({} + {}), é: {}.'.format(n1, n2, somar))

    elif escolha == 2:
        multiplicar = n1 * n2
        print('A multiplicação dos valores informados ({} + {}), é: {}.'.format(n1, n2, multiplicar))

    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor dos números informados ({} e {}), é: {}'.format(n1, n2, maior))

    elif escolha == 4:
        n1 = int(input('Digite novamente o primeiro valor: '))
        n2 = int(input('Digite novamente o segundo valor: '))

    else:
        print('Valor inválido, por favor, tente novamente!')

print('ATÉ A PRÓXIMA... OBRIGADO!')
