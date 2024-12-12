""" Verificar dados sobre o que foi passado"""

dado = input("Me Diga algo para vermos suas Espicificações : ")
print("-=" * 20)

print(f"O tipo primitivo é? {type(dado)}")
print(f"É somente espaço? {dado.isspace()}")
print(f'É um número? {dado.isnumeric()}')
print(f'É Somente letras? {dado.isalpha()}')
print(f'É letras e números? {dado.isalnum()}')
print(f'É todo minusculo? {dado.islower()}')
print(f'É todo maiusculo? {dado.isupper()}')
print(f'É capitalizada? {dado.istitle()}')

print("-=" * 20)
