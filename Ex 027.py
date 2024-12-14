""" Primeiro e Ultimo Nome do usuário """

username = str(input("Qual seu nome completo? ").strip())
username_list = username.split(' ',)
print(f"\nSeu primeiro nome é: {username_list[0]}")
print(f"Seu ultimo nome é: {username_list[-1]}")
