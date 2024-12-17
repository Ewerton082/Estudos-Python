""" Contador de numeros pares numa lista de x a y"""

start = int(input("Digite onde deseja começar a contagem: ").strip())
end = int(input("Digite o número onde deseja finalizar a contagem: ").strip())
lista_par = []

for number in range(start, end+1):
    if number % 2 == 0:
        lista_par.append(number)

print(f"\nA quantidade de números pares na lista {len(lista_par)}")
print(lista_par)
