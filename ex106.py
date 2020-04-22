def ajuda(com):
    help(com)


def titulo(msg, cor):
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA HELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)