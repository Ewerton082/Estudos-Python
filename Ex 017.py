""" Catetos e a Hipotenusa """
from math import hypot

cateto_oposto = float(input("Comprimento do cateto oposto: ").strip().replace(',', '.'))
cateto_adjacente = float(input("Comprimento do cateto adjacente: ").strip().replace(',', '.'))
print("-=-" * 10)
print(f"O Valor da Hipotenusa vai ser de {hypot(cateto_oposto, cateto_adjacente):.2f}")
