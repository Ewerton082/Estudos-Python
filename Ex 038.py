""" Comparando Numeros """

number_list = []
for index in range(0,2):
    number = int(input(f"Digite o {index + 1}º número: ").strip())
    number_list.append(number)

print("")
if number_list[0] == number_list[1]:
    print("Os dois numeros são iguais")
else:
    print(f"\033[92mO maior número é {max(number_list)}\033[0m")
    print(f"\033[91mO menor número é {min(number_list)}\033[0m")
