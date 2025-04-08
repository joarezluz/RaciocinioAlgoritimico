#passoJogo -> passo principal
#evento    -> tipo de evento -> entrada, saída
#etapa-> início, fim, créditos, menu, submenus

#etapas principais [1]início [2]menu [0]fim [3]selecao de modo
#submenus
import random

etapa=1
passosPrin=100 #passo de loop do jogo frequencia de atualizacao
passo=0

modo = 0 # indicar o modo do jogo

while etapa > 0:
    if etapa == 1: #introducao
        if passo == 1:
                print('\n::::::::::::::::\n::::Jokenpo!!:::\n:::::Python:::::\n::::::::::::::::')
        if passo <= passosPrin:
            passo += 1
        else:   #fim do passo em etapa 1
            passo = 0
            etapa = 2 ## menu
    if etapa == 2: ##menu
        if passo == 1:
                etapa = int(input('::::::::::::::::\n::>Iniciar [3]\n::>Créditos [4]\n::>Sair [0]\n>> '))
        #print('\n\n')
        if passo <= passosPrin:
            passo += 1
        else:   #fim do passo em etapa 1
            passo = 0
    if etapa == 3: ##menu jogar
        if passo == 1:
            print('::::::::::::::::\nSELECIONE O MODO\n::::::::::::::::\n::::::::::::::::')
            modo = int(input('::=>CPU vs CPU [1]\n::>Voltar [0]\n>> '))
            if modo == 0: etapa = 1
            if modo == 1:
                sel = ['pedra','papel','tesoura']
                cpu1 = random.choice(sel)
                cpu2 = random.choice(sel)
                print(f'::::::::::::::::\n::::CPU 1::::CPU 2::::::::::::\n::::{cpu1}::X::{cpu2}::::::::::::')
                modo = input(f'{cpu1} x {cpu2}::\nContinuar[1] Voltar[0] : ')
                #print('::::::::::::::::\n::::CPU 2::::::::::::\n::::::::::::::::')
        print('::::::::::::::::\n::::::::::::::::\n::::::::::::::::')
        if passo <= passosPrin:
            passo += 1
        else:   #fim do passo em etapa 1
            passo = 0
    if etapa == 4:
        if passo == 1:
                print('\n\n\n::::::::::::::::::\n:::Desenvolvedor::\n:Joarez C. da Luz:\n::::::::::::::::::')
        if passo == 1:
            etapa = int(input('::::::::::::::::::\n::>Voltar [2]\n::>Sair [0]\n>> '))
            #print('::::::::::::::::\n::::::::::::::::')
            print('\n\n')
        if passo <= passosPrin:
            passo += 1
        else:   #fim do passo em etapa 1
            passo = 0
    if etapa >= 5 or etapa < 0:
        etapa = 1
print()