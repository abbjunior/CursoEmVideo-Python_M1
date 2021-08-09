# Crie um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome

# EX:
# Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite o seu nome completo: ')).strip()

nome = nome.split()

print('Primeiro nome: {}'.format(nome[0]))
print('Segundo nome: {}'.format(nome[len(nome)-1]))
