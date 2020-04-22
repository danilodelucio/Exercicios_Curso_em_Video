n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Sua média foi {}.'.format(media))

if media < 5.0:
    print('Você está REPROVADO!')
elif 5.0 <= media < 7.0:
    print('Você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print(f'Com a {media} Parabéns, você foi APROVADO!')
