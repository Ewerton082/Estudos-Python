""" Calcular média aritimetica """

nota1 = float(input("Qual a primeira nota do aluno:").replace(',', '.'))
nota2 = float(input("Qual a segunda nota do aluno:").replace(',', '.'))
media = (nota1 + nota2) / 2
print("-=" * 20)

if media >= 5:
    print(f"Você está aprovado com a media de {media}")
else:
    print(f"Você Foi Reprovado com a media de {media}")
