""" Jogo de adivinhação basico """
from time import sleep
from random import randint

print("\033[93m-=-\033[0m" * 20)
print("    " * 4 +"\033[96m Jogo de Adivinhação V1")
print("\033[93m-=-\033[0m" * 20)

choice_number = randint(0, 5)
player_number = int(input("Escolha um número entre \033[91m 0 a 5\033[0m e veja se acerta hihi:"))
if 0 <= player_number <= 5:
    print("\033[97m Processando...")
    sleep(2)
    if choice_number == player_number:
        print(f"\033[92m Meus Parabens você acertou\033[0m")
    else:
        print(f"\033[91m Infelizmente você  errou eu tinha pensado no {choice_number}, não no {player_number}\033[0m")
else:
    print("\033[97mcansei de brincar vc é burro")
