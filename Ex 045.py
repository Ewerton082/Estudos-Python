""" Pedra Papel Tesoura """
from random import choice

options = ["pedra", "papel", "tesoura"]

print("""
[1] Pedra
[2] Papel
[3] Tesoura
[4] Encerrar Jogo""")

while True:
    player_choice = input("Selecione sua Arma: ".strip())

    if player_choice not in ['1', '2', '3', '4']:
        print("Selecione uma opção válida!!!")
        continue

    elif player_choice == 4:
        break

    computer_choice = choice(options)
    player_choice = options[int(player_choice) - 1]

    print(f"Computador Escolheu: {computer_choice} || Player Escolheu: {player_choice}")

    if computer_choice == player_choice:
        print("\033[96mVocês Empataram!!\033[0m")
    elif player_choice == "pedra" and computer_choice == "tesoura" or player_choice == "papel" and computer_choice == "pedra" or player_choice == "tesoura" and computer_choice == "papel":
        print("\033[92mPlayer WINS!!!\033[0m")
    else:
        print("\033[91mComputadorr WINS!!!\033[0m")