palavras = ('nuke', 'mocha', 'syntheyes', 'blender', 'substance painter', 'after effects',
            'pycharm', 'python', 'photoshop', 'crazybump', 'premiere', 'unreal', 'embergen',
            'davinci resolve', 'audition')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais:  ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')