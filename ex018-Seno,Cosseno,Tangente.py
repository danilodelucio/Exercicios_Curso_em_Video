from math import radians, cos, sin, tan
n = float(input('Digite um ângulo que você deseja: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('O ângulo de {} tem o Seno de {:.2f}.'.format(n, s))
print('O ângulo de {}, tem o Cosseno de {:.2f}'.format(n, c))
print('O ângulo de {}, tem a Tangente de {:.2f}'.format(n, t))
