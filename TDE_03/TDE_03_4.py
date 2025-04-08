#4.	Imprima os números múltiplos de 4 existentes no intervalo aberto de 1 a 100.

num = 1

while num <= 100:
    if num % 4 == 0:
        print(num)
    num = num + 1
