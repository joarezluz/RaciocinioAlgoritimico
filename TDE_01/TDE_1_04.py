print('Exercício 04')

valorProd = float(input('Insira o valor do produto em R$: '))

print(f'À vista com 5% de desconto: {valorProd - (valorProd * 0.05)}')
print(f'2 Parcelas de: R${valorProd / 2}')
print(f'3 Parcelas de: R${(valorProd + (valorProd * 0.05))/ 3} com juros de 5%')
