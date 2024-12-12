""" Calculando custo do aluguel de um carro """

dias_alugados = int(input("Quantos Dias Alugou o carro? ").strip())
km_rodados = float(input("Quantos KM você rodou? ").strip().replace(',', '.'))
valor_total = (dias_alugados * 60) + (km_rodados * 0.15)
print("-=-" * 15)
print(f"Valor total a pagar é de {valor_total:.2f} R$")
