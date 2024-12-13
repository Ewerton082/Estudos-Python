""" Seno, Cosseno, Tangente """
from math import sin, cos, tan, radians

angulo = float(input(f"Digite o ângulo que você deseja: "))

print("-=-" * 15)
print(f"o ângulo de {angulo:.2f} tem o SENO de {sin(radians(angulo)):.2f}")
print(f"o ângulo de {angulo:.2f} tem o COSSENO de {cos(radians(angulo)):.2f}")
print(f"o ângulo de {angulo:.2f} tem o TANGENTE de {tan(radians(angulo)):.2f}")
