""" Ver qual o menor e o maior valor entre 5 numeros """

number_list = []

for index in range(0, 5):
    number = int(input("Digite um número: ").strip())
    number_list.append(number)

print(f"O \033[92mMaior\033[0m Número digitado foi {min(number_list)}")
print(f"O \033[91mMenor\033[0m Número digitado foi {max(number_list)}")
print(f"\n Os numeros da lista foram {number_list}")
