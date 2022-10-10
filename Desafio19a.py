#Sorteia um aluno com base em uma lista digitada
from random import choice

a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Dgiite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print('O aluno escolhido foi : {}'.format(escolhido))
