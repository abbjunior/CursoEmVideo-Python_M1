# Crie um programa que leia um nome completo de uma pessoa e mostre:
# 1- O nome com todas as letras maiúsculas
# 2- O nome com todas as letras minúsculas
# 3- Quantas letras ao todo (Sem considerar os espaços)
# 4- Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Maiúsculas:',nome.upper())
print('Minusculas:',nome.lower())

print('Total de letras do seu nome:',len(nome) - nome.count(' '))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
