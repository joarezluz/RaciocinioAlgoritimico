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
        print('\n..............................\n...........Jokenpo!...........\n............Python............\n::::::::::::::::')
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
            naveg[2] = int(input('::=>[1] CPU vs CPU \n::>[] Voltar\n>> '))
            if naveg[2] != 1: #sair do modo e voltar ao menu anterior [menu principal]
                naveg = [2,0,0]
        if naveg[2] == 1: ## CPU X CPU
            jog1 = "CPU1"
            jog2 = "CPU2"
            while naveg[2] == 1:
                sel = ['Papel','Pedra','Tesoura']
                cpu1 = random.choice(sel)
                cpu2 = random.choice(sel)
                pontCpu1=0
                pontCpu2=0
                ganhador = "Ninguém"

                if ((cpu1 == sel[0] and cpu2 == sel[1])
                        or (cpu1 == sel[1] and cpu2 == sel[2])
                        or (cpu1 == sel[2] and cpu2 == sel[0])) :
                    pontCpu1 += 1
                    ganhador = jog1 + ' Ganhou'

                if ((cpu2 == sel[0] and cpu1 == sel[1])
                        or (cpu2 == sel[1] and cpu1 == sel[2])
                        or (cpu2 == sel[2] and cpu1 == sel[0])) :
                    pontCpu2 += 1
                    ganhador = jog2 + 'Ganhou'
                if cpu1 == cpu2: ganhador = "Empate"
                print(f'::::::::::::::::\n::::CPU 1::::CPU 2::::::::::::\n::::{cpu1}::X::{cpu2}::::::::::::\n *****{ganhador}!!****')
                menuSel = int(input(f'{jog1} = {pontCpu1} \n {jog2} = {pontCpu2} \n::> [1] Continuar\n::> [] Voltar\n::>'))

                if pontCpu1 > pontCpu2: ganhador = jog1
                elif pontCpu2 > pontCpu1:(
                    ganhador) = jog2
                else:
                    ganhador = "Empate"
                print(f'::::::::::::::::\n::::{ganhador}!!!!\n::::::::::::::::')

                if menuSel != 1 : naveg = [3,1,0] #reconfigura o menu

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

