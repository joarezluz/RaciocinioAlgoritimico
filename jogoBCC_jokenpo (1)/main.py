#passoJogo -> passo principal
#evento    -> tipo de evento -> entrada, saída
#etapa-> início, fim, créditos, menu, submenus

#etapas principais [1]início [2]menu [0]fim [3]selecao de modo
#submenus
import random

menu=0 #padrão = 0
subMenu=0 #padrão = 0
modo = 0  #padrão = 0
naveg =[menu,subMenu,modo]# menu e submenu e o modo do jogo


## Etapa == 1 Jogo iniciado
## Etapa == 0 Jogo Finalizado

naveg[0]=1 #iniciar jogo com a intodução


while naveg[0] > 0: # jogo iniciado enquando maior que 0
    if naveg[0] == 1: #introducao
        print('\n::::::::::::::::\n::::Jokenpo!!:::\n:::::Python:::::\n::::::::::::::::')
        naveg[0] = 2 # ir para o menu principal
    if naveg[0] == 2: ##menu principal
        menuSel = int(input('::::::::::::::::\n::>[1] Iniciar\n::>[2] Créditos\n::>[]Sair\n>> '))
        if 1 <= menuSel <= 2:
            naveg[0] = menuSel+2
        else:
            naveg[0] = 0 #sair

    if naveg[0] == 3: ##menu iniciar -> submenu
        naveg[1] = 1
        if naveg[1] == 1:
            print('::::::::::::::::\nSELECIONE O MODO\n::::::::::::::::\n::::::::::::::::')
            naveg[2] = int(input('::=>[1] CPU vs CPU \n::>[0] Voltar\n>> '))
            if naveg[2] == 0: #sair do modo e voltar ao menu anterior [menu principal]
                naveg = [2,0,0]
        if naveg[2] == 1: ## CPU X CPU
            while naveg[2] == 1:
                sel = ['pedra','papel','tesoura']
                cpu1 = random.choice(sel)
                cpu2 = random.choice(sel)
                print(f'::::::::::{modo}::::::\n::::CPU 1::::CPU 2::::::::::::\n::::{cpu1}::X::{cpu2}::::::::::::')
                menuSel = int(input(f'{cpu1} x {cpu2}::\n::> [1] Continuar\n::> [0] Voltar\n::>'))
                if menuSel == 0 : naveg = [3,1,0] #reconfigura o menu

        print('::::::::::::::::\n::::::::::::::::\n::::::::::::::::')
    if naveg[0] == 4: ## Créditos
        print('\n\n\n::::::::::::::::::\n:::Desenvolvedor::\n:Joarez C. da Luz:\n::::::::::::::::::')
        menuSel = int(input('::::::::::::::::::\n::>[1] Voltar\n::>[] Sair\n>> '))
        #print('::::::::::::::::\n::::::::::::::::')
        print('\n\n')
        if menuSel == 1:
            naveg[0] = 2 #menu princial
        else:
            naveg[0] = 0 #sair
print()

