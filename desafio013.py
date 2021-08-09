# Crie um algoritmo que leia o salário de um funcionário e moste o seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário:R$ '))

salAumento = salario + (salario * 15 / 100)

print('Seu salário com aumento de 15% será: R${:.2f}'.format(salAumento))
