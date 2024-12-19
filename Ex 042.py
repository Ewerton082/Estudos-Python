""" Calcular se 3 retas formam um triangulo e qual tipo de triangulo será feito"""


def forma_triangulo(retaA: float, retaB: float, retaC: float):
    if retaA + retaB > retaC and retaA + retaC > retaB and retaB + retaC > retaA:
        if retaA == retaB == retaC:
            return "\033[92m\nÉ Possivel sim formar um triângulo com essas retas e o triangulo será EQUILÁTERO\033[0m"
        elif retaA == retaC or retaA == retaB or retaC == retaB:
            return "\033[92m\nÉ Possivel sim formar um triângulo com essas retas e o triangulo será ISÓSCELES\033[0m"
        else:
            return "\033[92m\nÉ Possivel sim formar um triângulo com essas retas e o triangulo será ESCALENO\033[0m"

    else:
        return "\033[91m\nNão é Possivel formar um triângulo com essas retas \033[0m"


reta1 = float(input("Me Diga o comprimento da Primeira reta: ").strip().replace(',', '.'))
reta2 = float(input("Me Diga o comprimento da Segunda reta: ").strip().replace(',', '.'))
reta3 = float(input("Me Diga o comprimento da Terceira reta: ").strip().replace(',', '.'))
print(forma_triangulo(reta1, reta2, reta3))
