#Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então
#qual o valor da soma e da média aritmética do conjunto.

num = 1
soma = 0
print('Insira números inteiros')
while num <= 10:
    s = int(input(f'{num} '))
    soma += s
    num += 1
print(f'Total = {soma} \nMédia: {soma/10}')


