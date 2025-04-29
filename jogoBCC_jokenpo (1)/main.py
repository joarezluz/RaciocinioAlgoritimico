#passoJogo -> passo principal
#evento    -> tipo de evento -> entrada, saída
#etapa-> início, fim, créditos, menu, submenus

#etapas principais [1]início [2]menu [0]fim [3]selecao de modo
#submenus
import random ##gerar numeros aleatórios
import getpass ##ocultar digitos no Pessoa vs Pessoa



menu=0 #padrão = 0
subMenu=0 #padrão = 0
modo = 0  #padrão = 0
naveg =[menu,subMenu,modo]# menu e submenu e o modo do jogo



##*******Imagens
imgLogo = """
······························································
:     ██╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██████╗  ██████╗ :
:     ██║██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔═══██╗:
:     ██║██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██████╔╝██║   ██║:
:██   ██║██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔═══╝ ██║   ██║:
:╚█████╔╝╚██████╔╝██║  ██╗███████╗██║ ╚████║██║     ╚██████╔╝:
: ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝ :
······························································
"""



imgPedra = """
..............................
.......:#%@@@@@@@@@@@%#-.....
.....-@@@%############@@@*....
.:%@@@@#...............-@@#...
+@@+....................=@@=..
@@=.....................=@@+:.
@@=.....................=@@@@=
@@=...+.....=-....--....=@-+@@
@@=...@.....@=....##....=@--@@
@@=...@.....@=....##....=@--@@
@@#...@.....@=....##....=@--@@
:@@@@@@:....@=....##....=@-=@@
...:=%@@=...@=....##...=@+-@@#
......-@@@@@@@@@#######--@@@=.
..............@@@*====+@@@+...
...............-#@@@@@@@=.....
..............................
"""


imgPapel ="""
.....=@@@@@@@@@@+.............
....@@@:.:@@=.:@@@@@=.........
.:@@@@@....@-..=@%%@@@-.......
#@@@#@@....@-..=@...+@@.......
@@+...@....@-..=@...-@@:......
@@+...@....@-..=@...-@@:......
@@+...@....@-..=@...-@@:......
@@+...@....@-..=@...-@@:......
@@+...@....@-..=@...-@@:......
@@+.................-@@@@@@@=.
@@+.................-@@@=.=@@@
@@+.................-@......@@
@@+........:@@+:...........@@@
@@+.......#@.............@@@%.
@@@.......@:...........#@@@...
#@@.......-..........+@@@:....
.@@@...............+@@@:......
..@@@+...........+@@@.........
...:@@@@*:...:+@@@@...........
......=@@@@@@@@@=.............
"""


imgTesoura = """
.....................@@@@@@@..
.........+@@@@@@@..+@@@@#@@@@=
........@@@@*+@@@@+@@@-...=@@@
.......=@@@....-@@@@@@....-@@@
.......-@@@+....%@@@@@....-@@@
........-@@@-....@@@@@....-@@@
.........#@@@....:@@@@....-@@@
..........@@@@....*@@@....-@@@
..........=@@@=....%@@....-@@@
.......+@@@@@@@-....@@....-@@@
..=@@@@@@@=...@@..........-@@@
:@@@@@@@@+....@@..........-@@@
@@@=...=@+....@@..........-@@@
@@@....=@+....@@..........-@@@
@@@...+@@@@@@@@@@@@@@@@#-.-@@@
@@@..@@:...............-@@@@@@
@@@.:@....................@@@@
@@@..@@#..................-@@@
@@@....=++++@@-...........-@@@
@@@=........#@-...........+@@@
+@@@........#@-..........:@@@-
.@@@@.......#@-.........:@@@*.
..%@@@-................%@@@=..
...=@@@@@-..........=@@@@@:...
.....-@@@@@@@@@@@@@@@@@%:.....
.........#@@@@@@@@@@+.........
"""
##***************************************



## Etapa == 1 Jogo iniciado
## Etapa == 0 Jogo Finalizado

naveg[0]=1 #iniciar jogo com a intodução


while naveg[0] > 0: # jogo iniciado enquando maior que 0
    if naveg[0] == 1: #introducao
        #print('\n..............................\n...........Jokenpo!...........\n............Python............\n::::::::::::::::')
        print(imgLogo)
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
            naveg[2] = int(input('::=>[1] CPU vs CPU\n'
                                 '::=>[2] CPU vs Jogador\n'
                                 '::>[] Voltar\n>> '))
            if naveg[2] not in [1,2]: #sair do modo e voltar ao menu anterior [menu principal]
                naveg = [2,0,0]
                sel = ['Papel', 'Pedra', 'Tesoura']
        if naveg[2] == 1: ## CPU X CPU
            pontJog1 = 0
            pontJog2 = 0
            jog1 = "CPU1"
            jog2 = "CPU2"
            cpu1 = ["",""]
            cpu2 = ["",""]
            sel = ['Papel', 'Pedra', 'Tesoura']
            while naveg[2] == 1:
                cpu1[0] = random.choice(sel)
                cpu2[0] = random.choice(sel)

                ganhador = "Ninguém"

                if ((cpu1[0] == sel[0] and cpu2[0] == sel[1])           #papel x pedra
                        or (cpu1[0] == sel[1] and cpu2[0] == sel[2])    #pedra x tesoura
                        or (cpu1[0] == sel[2] and cpu2[0] == sel[0])) : #tesour x papel
                    pontJog1 += 1
                    ganhador = jog1 + '*Ganhou '

                if ((cpu2[0] == sel[0] and cpu1[0] == sel[1])           #papel X pedra
                        or (cpu2[0] == sel[1] and cpu1[0] == sel[2])    #pedra X tesoura
                        or (cpu2[0] == sel[2] and cpu1[0] == sel[0])) : #tesoura x Papel
                    pontJog2 += 1
                    ganhador = jog2 + '*Ganhou '

                if cpu1[0] == sel[0]: cpu1[1] = imgPapel
                elif cpu1[0] == sel[1]: cpu1[1] = imgPedra
                else: cpu1[1] = imgTesoura
                if cpu2[0] == sel[0]: cpu2[1] = imgPapel
                elif cpu2[0] == sel[1]: cpu2[1] = imgPedra
                else: cpu2[1] = imgTesoura

                if cpu1 == cpu2: ganhador = "Empate"

                print(cpu1[1] + cpu2[1])

                print(f'\n *****{ganhador}!!****')
                menuSel = int(input(f'{jog1} = {pontJog1} \n {jog2} = {pontJog2} \n::> [1] Continuar\n::> [] Voltar\n::>'))

                if pontJog1 > pontJog2: ganhador = jog1
                elif pontJog2 > pontJog1:
                    ganhador = jog2
                else:
                    ganhador = "Empate"
                print(f'::::::::::::::::::::::::::::::\n::::Ganhador Fianl {ganhador}!!!!\n::::::::::::::::::::::::::::::')

                if menuSel != 1 : naveg = [3,1,0] #reconfigura o menu
        if naveg[2] == 2: ## CPU X Jogador
            pontJog1 = 0
            pontJog2 = 0
            jog1 = "CPU1"
            jog2 = input("Insira o nmome do Jogador: ")
            cpu1 = ["",""]
            cpu2 = ["",""]
            sel = ['Papel', 'Pedra', 'Tesoura']
            while naveg[2] == 2:
                cpu1[0] = random.choice(sel)
                cpu2[0] = input("Escolha um alternativa\n"
                                "[1]:>Papel\n"
                                "[2]:>Pedra]\n"
                                "[3]:>Tesoura\n"
                                "[]:> Aleatório\n")
               #if cpu2[0] not in [1,2,3]: cpu2[0] = random.choice(sel)

                ganhador = "Ninguém"

                if ((cpu1[0] == sel[0] and cpu2[0] == sel[1])           #papel x pedra
                        or (cpu1[0] == sel[1] and cpu2[0] == sel[2])    #pedra x tesoura
                        or (cpu1[0] == sel[2] and cpu2[0] == sel[0])) : #tesour x papel
                    pontJog1 += 1
                    ganhador = jog1 + '*Ganhou '

                if ((cpu2[0] == sel[0] and cpu1[0] == sel[1])           #papel X pedra
                        or (cpu2[0] == sel[1] and cpu1[0] == sel[2])    #pedra X tesoura
                        or (cpu2[0] == sel[2] and cpu1[0] == sel[0])) : #tesoura x Papel
                    pontJog2 += 1
                    ganhador = jog2 + '*Ganhou '

                if cpu1[0] == sel[0]: cpu1[1] = imgPapel
                elif cpu1[0] == sel[1]: cpu1[1] = imgPedra
                else: cpu1[1] = imgTesoura
                if cpu2[0] == sel[0]: cpu2[1] = imgPapel
                elif cpu2[0] == sel[1]: cpu2[1] = imgPedra
                else: cpu2[1] = imgTesoura

                if cpu1 == cpu2: ganhador = "Empate"

                print(cpu1[1] + cpu2[1])

                print(f'\n *****{ganhador}!!****')
                menuSel = int(input(f'{jog1} = {pontJog1} \n {jog2} = {pontJog2} \n::> [1] Continuar\n::> [] Voltar\n::>'))

                if pontJog1 > pontJog2: ganhador = jog1
                elif pontJog2 > pontJog1:
                    ganhador = jog2
                else:
                    ganhador = "Empate"
                print(f'::::::::::::::::::::::::::::::\n::::Ganhador Fianl {ganhador}!!!!\n::::::::::::::::::::::::::::::')

                if menuSel != 1 : naveg = [3,1,0] #reconfigura o menu

        print('::::::::::::::::\n::::::::::::::::\n::::::::::::::::')
    if naveg[0] == 4: ## Créditos
        print('\n\n\n::::::::::::::::::\n:::Desenvolvedor::\n:Joarez C. da Luz:\n::::::::::::::::::'
              '\n:::::::::::::::::::::\nGerador das artes ASCII:\nhttps://www.asciiart.eu/image-to-ascii\n:::::::::::::::::::')
        menuSel = int(input('::::::::::::::::::\n::>[1] Voltar\n::>[] Sair\n>> '))
        #print('::::::::::::::::\n::::::::::::::::')
        print('\n\n')
        if menuSel == 1:
            naveg[0] = 2 #menu princial
        else:
            naveg[0] = 0 #sair
print()

