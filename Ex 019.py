""" Sorteando nomes de uma lista """
from random import choice

alunos_lista = []

for i in range(1,5):
    aluno = str(input(f"{i}º Aluno: ").strip())
    alunos_lista.append(aluno)

print(f"Os alunos da lista são: {alunos_lista}")
print(f" O aluno escolhido foi {choice(alunos_lista)}")
