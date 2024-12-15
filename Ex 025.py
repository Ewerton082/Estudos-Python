""" Confirmar se tem silva em algum nome """

nome_completo = str(input("Qual seu nome completo: ").strip().upper())
existe_silva = "SILVA" in nome_completo

print(f"em seu nome tem Silva : {existe_silva}")
