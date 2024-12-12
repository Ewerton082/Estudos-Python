""" Calculando 5% de desconto em produtos """

valor_produto = float(input("Qual o Valor inicial do produto? R$ ").strip().replace(',', '.'))
valor_desconto = (valor_produto / 100) * 5

print(f"O produto que custava antes {valor_produto} com nossa promoção de 5% de desconto estará custando apenas {valor_produto - valor_desconto:.2f}")