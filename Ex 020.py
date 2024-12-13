""" Sorteando nomes de uma lista """
from random import shuffle

alunos_lista = []

for i in range(1,5):
    aluno = str(input(f"{i}º Aluno: ").strip())
    alunos_lista.append(aluno)

shuffle(alunos_lista)
print(f" A ordem de apresentação será {alunos_lista}")
