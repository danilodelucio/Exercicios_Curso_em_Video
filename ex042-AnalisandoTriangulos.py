'''
TABELA INFORMATIVA:
- Equilátero: todos os lados são iguais.
- Isósceles: dois lados são iguais.
- Escaleno: todos os lados são diferentes
'''
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EUILÁTERO!')
    elif r1 != r2 != r3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂGULO!')
