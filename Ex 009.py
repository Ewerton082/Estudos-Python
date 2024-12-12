
num = int(input("Digite um número inteiro para ver sua tábuada: ").strip())

print("-" * 20)
for cont in range(1, 11):
    print(f"{num} x {cont} = {num * cont}")

print("-" * 20)
