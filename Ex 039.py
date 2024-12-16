""" Ver data de Alistamento """
from datetime import date

ano_nascimento = int(input("QUal ano você Nasceu: ").strip())
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f"você tem {idade} anos, e está no ano de se alistar")
    print(f"\033[96mVenha trabalhar com a gente !!!")
elif idade > 18:
    print(f"você tem {idade} anos, você deveria ter se alistado há {idade - 18} anos")
    print(f"\033[91mo ano do seu alistamento será em {ano_atual - (idade - 18)}")
else:
    print(f"você tem {idade} anos, faltam {18 - idade} anos para precisar se alistar")
    print(f"\033[92mo ano do seu alistamento será em {ano_atual + (18 - idade)}")
