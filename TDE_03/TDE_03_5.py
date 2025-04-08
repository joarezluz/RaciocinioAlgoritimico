#5.	Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário.

num = int(input("Insira um número inteiro maior que 1: "))

while num >= 1:
    if num%2 != 0:  print(num)
    num = num - 1