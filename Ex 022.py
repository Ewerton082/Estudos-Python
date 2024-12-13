"""Analizando e modificando alguns texto """

nome = str(input("Me diga seu nome completo: ").strip())
nome_separado = nome.split(' ')
print("-=-" * 17)
print(f"\nSeu nome todo maiusculo é: {nome.upper()}")
print(f"Seu nome todo minusculo é: {nome.lower()}")
print(f"Ao total seu nome tem {len(nome.replace(' ', ''))} Letras")
print(f"O seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} Letras")
