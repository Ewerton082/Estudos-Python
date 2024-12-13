""" Separando as casa de um número """

valor = int(input("Me diga um número para separarmos :"))
unidade = valor % 10
dezena = (valor // 10) % 10
centena = (valor // 100) % 10
milhar = (valor // 1000) % 10
dezena_milhar = (valor // 10000) % 10

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
print(f"Dezena de Milhar: {dezena_milhar}")
