p = float(input('Digite seu peso em kilogramas:'))
a = float(input('Digite sua altura em metros:'))

imc = p / (a * a)
print(imc)

if imc < 16:
    print('seu imc esta muito baixo')
elif imc < 25:
    print('seu imc é ideal')
elif imc < 30:
    print('seu imc está acima do ideal')
else:
    print('seu imc está muito acima do ideal')
