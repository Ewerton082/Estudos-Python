""" Conversor de bases numericas """

while True:
    number_choice = input("Escolha um número para converter: ").strip()
    if number_choice.isnumeric():
        print(("""\033[94m
        [1] Binaio
        [2] Hexadecimal
        [3] Octal
        \033[0m"""))
        while True:
            choice = int(input("Escolha uma opção: ").strip())
            if choice == 1:
                print(f"Valor convertido em Binario: {bin(int(number_choice)) [2:]}")
                break
            if choice == 2:
                print(f"Valor convertido em Hexadecimal: {hex(int(number_choice)) [2:]}")
                break
            if choice == 3:
                print(f"Valor convertido em Octal: {oct(int(number_choice)) [2:]}")
                break
        break
    else:
        print("\033[91mDado informado foi invalido!!\033[0m")
