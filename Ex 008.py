""" Conversor de Medidas """

medida = float(input("Me diga uma distancia em metros para fazer a conversão?").strip().replace(',', '.'))
print("-=" * 20)

print(f"""
Km = {medida / 1000}
Hm = {medida / 100}
Dam = {medida / 10}
M = Medida que você passou {medida}
Dm = {medida * 10}
cm = {medida * 100}
mm = {medida * 1000}
""")
