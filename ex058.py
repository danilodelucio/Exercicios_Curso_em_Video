from random import randint

print(('-' * 10) + ' JOGO DE ADIVINHAÇÃO ' + ('-' * 10))

n = int(randint(0, 5))
palpites = 0

user = int(input('Qual número que estou pensando? '))
done = False

while not done:
    user = int(input('Que pena, você errou sonso!\nTente outra vez:  '))
    palpites += 1
    if user == n:
        done = True
    else:
        if user > n:
            print('Quase... menos!')
        elif user < n:
            print('Quase... mais!')

print('Parabéns mizeravi, você acertou!')
print('O número pensado foi {}, e você acertou na {}ª tentativa.'.format(n, palpites + 1))
