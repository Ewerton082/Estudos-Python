from math import sqrt

""" Calcular dobro,triplo e raiz quadrada """

num = int(input("Digite um número: ").strip())
print(f"Dados do número {num}")
print("-=" * 15)

print(f"O dobro é {num * 2}")
print(f"O triplo é {num * 3}")
print(f"Sua raiz quadrada é {sqrt(num)}")
