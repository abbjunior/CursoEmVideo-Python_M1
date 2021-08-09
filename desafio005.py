# Crie um algoritimo que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número INTEIRO: '))

ant = numero - 1
suc = numero + 1

print('O antecessor é: {} O Sucessor é: {}'.format(ant, suc))
