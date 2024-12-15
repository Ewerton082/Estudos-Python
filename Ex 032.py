""" Calcular se o ano é bissexto """
from datetime import date


def ano_bissexto(ano: int):
    if ano == 0:
        ano = date.today().year

    if ano % 4 == 0:
        return f"O ano de {ano} \033[92mÉ BISSEXTO"
    else:
        return f"O ano de {ano} \033[91mNÃO É BISSEXTO"


user_input = int(input("Qual ano deseja analizar? digite 0 paraver o ano atual: ").strip())
print(f"\n {ano_bissexto(user_input)}")
