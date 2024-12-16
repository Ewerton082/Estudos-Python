""" Calcular média e dzer a situação"""

nota1 = float(input("Qual a primeira nota?").strip().replace(',', '.'))
nota2 = float(input("Qual a segunda nota?").strip().replace(',', '.'))

media = (nota1 + nota2) / 2

if media >= 7:
    print("\033[92mParabêns você está aprovado")
elif media >= 5.9:
    print("\033[93mEstá de Recuperação")
else:
    print("\033[91mVocê foi reprovado!!")

