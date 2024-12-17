""" Contagem Regressiva para fogos """
from time import sleep

print("Preparando contagem para fim de ano")
print("-=-" * 15)
for i in range (10, 0,-1):
    print(f"\033[9{i}m{i}\033[0m")
    sleep(1)

print("\nFeliz Ano Novo!!!")
