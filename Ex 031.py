""" Calcular custos de viagem """


def calcular_viagem(distancia:float):
    if distancia < 200:
        return distancia * 0.5

    else:
        return distancia * 0.45


distancia = float(input("Quantos KM é a distancia de sua viagem? ").strip().replace(",", "."))

print(f"\n O valor total de sua viagem é de \033[92m{calcular_viagem(distancia):.2f} R$")
