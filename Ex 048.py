""" Mostrar a soma de todos numeros multiplos de 3 numa lista de x a y"""

start = int(input("Digite onde deseja começar a contagem: ").strip())
end = int(input("Digite o número onde deseja finalizar a contagem: ").strip())
lista_multiplos = []

for number in range(start, end+1):
    if number % 2 > 0:
        if number % 3 == 0:
            lista_multiplos.append(number)

print(f"\nA quantidade de números multiplos de 3 na lista é de: {len(lista_multiplos)}")
print(f"O valor da soma detodos dados é de: {sum(lista_multiplos)}")
