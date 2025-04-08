# media >= 7.0 ->Aprovado
# media <  4.0 -> Reprovado
# media >= 4 e media <7-> em recuperacao

media = float(input('Inserir a media: '))

if media >=7:
    print('Aprovado')
elif media <4:
    print('reprovado')
else:
    print('recuperacao')