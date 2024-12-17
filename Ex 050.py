""" Ler 6 numeros passados pelo usuario e fazer a soma dos numeros pares """

lista_num = []

for i in range(1, 7):
    numb_choice = int(input(f"Escolha o {i}º número: ").strip())
    if numb_choice % 2 == 0:
        lista_num.append(numb_choice)

print(f"Os numeros pares passado foram {lista_num} e o valor da soma deles é de {sum(lista_num)}")