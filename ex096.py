print(' CONTROLE DE TERRENOS ')
print('-' * 30)

def calculo(a, b):
    print(f'A área de um terreno {a}x{b} é de {a*b}m².')


largura = float(input('LARGURA (m):  '))
comprimento = float(input('COMPRIMENTO (m):  '))
print(calculo(largura, comprimento))