""" Verificar se a cidade que você nasceu começa com Santo """

cidade = str(input("Em Qual Cidade você nasceu? ").strip().upper())
lista_cidade = cidade.split()
print("SANTO" in lista_cidade[0])
