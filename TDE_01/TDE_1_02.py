print('Exercício 02')

ano = int(input('Insira o ano de nascimento: '))

idade2022 = 2022 - ano
if idade2022 < 0:
    print('insira um ano menor')
else:
    print(f'Idade em 2022: {idade2022}')
