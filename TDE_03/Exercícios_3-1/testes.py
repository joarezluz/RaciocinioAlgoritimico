import random


def get_winner(player1, player2):
    """
    Determines the winner of a round based on standard Rock-Paper-Scissors rules.
    Returns 'player1', 'player2', or 'draw' to indicate the result.
    """
    rules = {'PEDRA': 'TESOURA', 'TESOURA': 'PAPEL', 'PAPEL': 'PEDRA'}
    if player1 == player2:
        return "draw"
    elif rules[player1] == player2:
        return "player1"
    else:
        return "player2"


def get_computer_choice():
    """
    Generates and returns a random choice for the computer (PEDRA, PAPEL, or TESOURA).
    """
    return random.choice(["PEDRA", "PAPEL", "TESOURA"])


def play_jokenpo():
    """
    Main function to play the JoKenPo game.
    Handles game modes, rounds, and scores, as well as continuation or exit prompts.
    """
    print("Bem-vindo ao Jokenpô!")
    print("Escolha a modalidade:")
    print("1. Humano x Humano")
    print("2. Humano x Computador")
    print("3. Computador x Computador")

    # Get the game mode
    while True:
        try:
            mode = int(input("Digite o número da modalidade escolhida: "))
            if mode in [1, 2, 3]:
                break
            else:
                print("Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    # Initialize player names and scores
    if mode == 1:
        player1_name = input("Digite o nome do Jogador 1: ")
        player2_name = input("Digite o nome do Jogador 2: ")
    elif mode == 2:
        player1_name = input("Digite o nome do Jogador: ")
        player2_name = "Computador"
    else:
        player1_name = "Computador 1"
        player2_name = "Computador 2"

    scores = {player1_name: 0, player2_name: 0}

    while True:
        # Get player moves
        if mode == 1:
            player1_move = input(f"{player1_name}, escolha PEDRA, PAPEL ou TESOURA: ").upper()
            player2_move = input(f"{player2_name}, escolha PEDRA, PAPEL ou TESOURA: ").upper()
        elif mode == 2:
            player1_move = input(f"{player1_name}, escolha PEDRA, PAPEL ou TESOURA: ").upper()
            player2_move = get_computer_choice()
        else:
            player1_move = get_computer_choice()
            player2_move = get_computer_choice()

        # Validate inputs
        if player1_move not in ["PEDRA", "PAPEL", "TESOURA"] or player2_move not in ["PEDRA", "PAPEL", "TESOURA"]:
            print("Jogada inválida. Tente novamente!")
            continue

        # Display moves
        print(f"{player1_name} escolheu {player1_move}")
        print(f"{player2_name} escolheu {player2_move}")

        # Determine the winner
        result = get_winner(player1_move, player2_move)
        if result == "draw":
            print("Empate!")
        elif result == "player1":
            print(f"{player1_name} venceu esta rodada!")
            scores[player1_name] += 1
        else:
            print(f"{player2_name} venceu esta rodada!")
            scores[player2_name] += 1

        # Show current score
        print("\nPlacar atual:")
        for player, score in scores.items():
            print(f"{player}: {score}")

        # Ask to continue or exit
        while True:
            continue_game = input("\nDeseja CONTINUAR ou SAIR? ").upper()
            if continue_game in ["CONTINUAR", "SAIR"]:
                break
            print("Entrada inválida. Por favor, digite 'CONTINUAR' ou 'SAIR'.")

        if continue_game == "SAIR":
            print("\nPlacar final:")
            for player, score in scores.items():
                print(f"{player}: {score}")
            print(f"\nObrigado por jogar! Até a próxima, {player1_name} e {player2_name}!")
            break


if __name__ == "__main__":
    play_jokenpo()

