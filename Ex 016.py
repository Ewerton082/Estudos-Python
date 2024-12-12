""" Retirando os numeros que ficam após a virgula """
from math import trunc

valor_quebrado = float(input("Me diga um numero que irei tirar os numeros flutuantes : ").strip().replace(',', '.'))
print(f"{trunc(valor_quebrado)}")