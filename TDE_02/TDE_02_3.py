##Exercício 03
#Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe
#“Valor inválido” para números negativos)

numero = int(input("Insira um número inteiro: "))
if 0 > int(numero):
    print("Este número é inválido!")
else:
    print(f'A raíz quadrada desde numero é : {int(numero ** 0.5)}') #elevado a 1/2
