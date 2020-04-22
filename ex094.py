
# ACUMULADORES
dados = dict()
dadosList = list()
cadastros = 0
somaIdades = 0
mulheres = ''

while True:
    # MAIN INFOS
    dados['Nome'] = str(input('Nome: ')).strip().title()
    dados['Sexo'] = ''
    while True:
        dados['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if dados['Sexo'] not in 'MF':
            print('ERRO! POR FAVOR DIGITE "M" OU "F".')
        else:
            break
    dados['Idade'] = int(input('Idade: '))
    somaIdades += dados['Idade']

    # MULHERES
    if dados['Sexo'] == 'F':
        mulheres += dados['Nome'] + ' '

    # CLEAR
    dadosList.append(dados.copy())
    dados.clear()
    cadastros += 1

    # SIM OU NAO
    sn = ''
    while True:
        sn = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        if sn not in 'SN':
            print('ERRO! RESPONDA APENAS COM "S" OU "N".')
        else:
            break
    if sn == 'N':
        break

media = somaIdades / cadastros
print('-' * 40)
print(f'Dados cadastrados:\n{dadosList}.')
print(f'O grupo tem {cadastros} pessoas cadastradas.')
print(f'A média de idade é de {media:.1f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}.')

# print(f'Listas das pessoas que estão acima da média:\n.')

print('<<< ENCERRADO >>>')