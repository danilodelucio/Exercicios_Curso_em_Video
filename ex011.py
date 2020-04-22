largura = float(input("Qual a largura da sua parede? "))
altura = float(input("Qual a altura da sua parede? "))
area = largura * altura
print('Sua parede tem a dimensão de {} x {}, e sua área é de {}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {} litros de tinta.'.format(tinta))
