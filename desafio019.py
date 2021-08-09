# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random

aluno1 = str(input('Digite o nome do aluno 01: '))
aluno2 = str(input('Digite o nome do aluno 02: '))
aluno3 = str(input('Digite o nome do aluno 03: '))
aluno4 = str(input('Digite o nome do aluno 04: '))

alunos = [aluno1, aluno2, aluno3, aluno4] # Cria uma lista com os alunos 

escolhido = random.choice(alunos) # Randomiza a lista

print('O aluno escolhido foi o/a: {}'.format(escolhido))
