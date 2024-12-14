
"""Radar Eletronico """

MAX_SPEED = 100
MIN_SPEED = 60

now_speed = int(input("Qual a velocidade que você está andando? ").strip())

if 60 <= now_speed <= 100:
    print(f"\033[92m Está tudo nos conformes {now_speed} KM/h APROVADO")
else:
    print(f"\033[91m Você Levou uma multa seu infeliz {now_speed} KM/h MULTADO")
