""" Converter Celcius em kevin e Fahrenheit"""

celcius = float(input("ME Digite uma temperatura em Cº : ").strip().replace(',', '.'))
fahrenheit = (celcius * 1.8) + 32
kevin = celcius + 273

print(f"""
A Temperatura de {celcius:.2f} Cº\n
Em Kevin é de {kevin:.2f} K
Em Fahrenheit é de {fahrenheit:.2f} F""")
