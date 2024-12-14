""" Dizer onde foi a Primeira e ultima aparição da letra a """

while True:
    char_choice = str(input("Escolha uma vogal:").strip().upper())
    if len(char_choice) == 1:
        phrase_choice = str(input("Digite uma frase para contar quantas veses a vogal apareceu: ").strip().upper())
        if phrase_choice.count(char_choice) != 0:
            print(f"""
            Abaixo iremos contar e dizer as vezes que {char_choice} Apareceu\n
            a letra escolhida apareceu {phrase_choice.count(char_choice)} vezes
            a letra escolhida apareceu pela primeira vez na posição {phrase_choice.find(char_choice,0) + 1}
            a letra escolhida apareceu pela ultima vez na posição {phrase_choice.rfind(char_choice, 0)}
            """)
            break
        else:
            print('Tente Denovo!\n')

    else:
        print("Tente Denovo!\n")
