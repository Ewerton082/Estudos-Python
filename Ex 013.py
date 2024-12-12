""" alcular aumento de 15% no sálariode alguem """

valor_inicial = float(input("Qual era o valor do seu salário? R$ ").strip().replace(',', '.'))
valor_aumento = (valor_inicial / 100) * 15

print(f"Você que antes recebia {valor_inicial}, como nosso aumento de 15% anual passará a receber {valor_inicial + valor_aumento:.2f} R$")
