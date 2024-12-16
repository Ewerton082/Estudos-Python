""" Calcular aumento de um sálario basead no valor que ja recebiam """

your_salary = float(input("Quanto era o valor do seu salario? ").strip().replace(',', '.'))

if your_salary <= 1250:
    your_salary = ((your_salary / 100) * 15) + your_salary
    print(f"Com o aumento de 15% seu sálario passa a ser de {your_salary:.2f} R$")

else:
    your_salary = ((your_salary / 100) * 10) + your_salary
    print(f"Com o aumento de 10% seu sálario passa a ser de {your_salary:.2f} R$")
