from math import floor, hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
#h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}.'.format(floor(h)))
