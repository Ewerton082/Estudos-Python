"""" Criar um programa que calcula a area e o quanto de tinta será necessario """

largura = float(input("Quantos Metros de Largura mede sua parede? ").strip().replace(',' ,'.'))
altura = float(input("Quantos Metros de Altura tem sua parede? ").strip().replace(',', '.'))
area = largura * altura

print("-=-" * 25)
print(f"O valor da area de uma parede que mede {largura} X {altura} é de {area:.2f} M²")
print(f"Nossa tinta cobre 2 M² por litro então você irá precisar de {area / 2:.2f} Litros da nossa tinta")