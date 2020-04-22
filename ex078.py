# print('-' * 50)
# valores = [int(input('Digite um número:  ')), int(input('Digite outro número:  ')), int(input('Digite mais um número:  ')),
#            int(input('Digite mais outro número:  ')), int(input('Digite o último número:  '))]
#
# print('-' * 50)
# print(f'Valores digitados: {valores}')
# print(f'O maior número da lista é o {max(valores)}, na posição {valores.index(max(valores))+1}.')
# print(f'O menor número da lista é o {min(valores)}, na posição {valores.index(min(valores))+1}.')
# print('-' * 50)
# print(f'{"FIM DO PROGRAMA!":^50}')
# print('-' * 50)
listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}:  ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('-' * 30)
print(f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
print()