print('Exercício 06')

altura = float(input('Insira a altura do tanque em metro: '))
raio = float(input('Insira o raio do tanque em metro: '))
latas = ( (2 * 3.14159265) * (raio + altura )) / 3 # área total dividido pelo rendimento em m²
valorTotal = latas * 50

print(f'Precisará de {int(latas)} latas de tinta com valor total de R${round(valorTotal,2)}')

