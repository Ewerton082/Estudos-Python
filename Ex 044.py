""" Calcular Preços """

valor_compra = float(input("Qual o Valor da sua compra: R$ ").strip().format(',', '.'))
print("-=-" * 10)
print("""
[1] Dinheiro ou Pix
[2] uma vez cartão
[3] 2x no cartão
[4] 3x ou mais""")
print("-=-" * 10)
while True:
    opt = int(input("Qual Forma de pagamento? ").strip())
    if 1 <= opt <= 4:
        break
    else:
        print("\033[91mEscolha uma opção válida!!\033[0m")

if opt == 1:
    print(f"Ao pagar no dinheiro você consegue 10% de desconto | Valor Final: R$ {valor_compra - (valor_compra * 10 / 100):.2f}")
elif opt == 2:
    print(f"Ao pagar no Cartão em 1x você consegue 5% de desconto | Valor Final: R$ {valor_compra - (valor_compra * 5 / 100):.2f}")
elif opt == 3:
    print(f"Ao pagar no Cartão em 2x não tem desconto | Valor Final: R$ {valor_compra:.2f}")
elif opt == 4:
    print(f"Ao pagar no Cartão em 3x ou mais há 20% de juros| Valor Final: R$ {(valor_compra * 20 / 100) + valor_compra:.2f}")
