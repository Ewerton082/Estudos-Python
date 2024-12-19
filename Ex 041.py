"""Classificação de atletas """
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input("Em qual ano você nasceu? ").strip())
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"Você tem {idade} anos então está na categoria Mirim")
elif idade <= 14:
    print(f"Você tem {idade} anos então está na categoria Infantil")
elif idade <= 19:
    print(f"Você tem {idade} anos então está na categoria Júnior")
elif idade <= 25:
    print(f"Você tem {idade} anos então está na categoria Sênior")
else:
    print(f"Você tem {idade} anos então está na categoria Master")



