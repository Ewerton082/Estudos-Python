""" Retirando os numeros que ficam após a virgula """
from math import trunc

valor_quebrado = float(input("Me diga um numero que irei tirar os numeros flutuantes : ").strip().replace(',', '.'))
print(f"O valor que foi passado é de {valor_quebrado} | Sua porção inteira é de: {trunc(valor_quebrado)}".replace('.', ','))