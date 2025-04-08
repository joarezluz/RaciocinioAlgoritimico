# Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os
# valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao
# intervalo, ou seja, intervalo aberto.

li = int(input('Insira o limite inicial [Inteiro]: '))
lf = int(input('Insita o limite final   [Inteiro]: '))

while li < lf:
    if li % 3 == 0:
        print(li)
    li += 1
