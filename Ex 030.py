""" Par ou impar """


def par_impar(number: int):
    if number % 2 == 0:
        return "\033[92mPAR"
    else:
        return "\033[91mIMPAR"


choice_number = int(input("Me diga um número: ").strip())

print(f"O número {choice_number} é {par_impar(choice_number)} :)")
