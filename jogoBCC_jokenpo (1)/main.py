#passoJogo -> passo principal
#evento    -> tipo de evento -> entrada, saída
#etapa-> início, fim, créditos, menu, submenus

#etapas principais [1]início [2]menu [0]fim [3]selecao de modo
#submenus
import random

etapa=1


modo = 0 # indicar o modo do jogo

while etapa > 0:
    if etapa == 1: #introducao
        print('\n::::::::::::::::\n::::Jokenpo!!:::\n:::::Python:::::\n::::::::::::::::')
        etapa = 2
    if etapa == 2: ##menu
        etapa = int(input('::::::::::::::::\n::>Iniciar [3]\n::>Créditos [4]\n::>Sair [0]\n>> '))
        #Fim do menu
    if etapa == 3: ##menu jogar
        modo = -1
        if modo == -1:
            print('::::::::::::::::\nSELECIONE O MODO\n::::::::::::::::\n::::::::::::::::')
            modo = int(input('::=>CPU vs CPU [1]\n::>Voltar [0]\n>> '))

        if modo == 0: etapa = 1
        if modo == 1: ## CPU X CPU
            while modo > 0:
                sel = ['pedra','papel','tesoura']
                cpu1 = random.choice(sel)
                cpu2 = random.choice(sel)
                print(f'::::::::::{modo}::::::\n::::CPU 1::::CPU 2::::::::::::\n::::{cpu1}::X::{cpu2}::::::::::::')
                modo = input(f'{cpu1} x {cpu2}::\nContinuar[1] Voltar[2] : ')
                


            #print('::::::::::::::::\n::::CPU 2::::::::::::\n::::::::::::::::')
        print('::::::::::::::::\n::::::::::::::::\n::::::::::::::::')

    if etapa == 4:
        print('\n\n\n::::::::::::::::::\n:::Desenvolvedor::\n:Joarez C. da Luz:\n::::::::::::::::::')
        etapa = int(input('::::::::::::::::::\n::>Voltar [2]\n::>Sair [0]\n>> '))
        #print('::::::::::::::::\n::::::::::::::::')
        print('\n\n')
    if etapa >= 5 or etapa < 0:
        etapa = 1
print()

