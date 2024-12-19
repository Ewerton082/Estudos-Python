""" Calcurar o IMC de alguem """

altura = float(input("Qual sua altura em metros? ").strip().replace(',', '.'))
peso = float(input("Qual seu peso em quilos? ").strip().replace(',', '.'))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"Seu IMC atual é de {imc:.2f}")
    print("Você está abaixo do peso | MAGREZA")
elif imc <= 24.9:
    print(f"Seu IMC atual é de {imc:.2f}")
    print("Meus parabens seu você está no peso | IDEAL")
elif imc <= 29.9:
    print(f"Seu IMC atual é de {imc:.2f}")
    print("Você está um pouco acima do peso | SOBREPESO")
else:
    print(f"Seu IMC atual é de {imc:.2f}")
    print("Você está | OBESO procure se tratar")
