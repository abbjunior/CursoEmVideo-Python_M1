# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero = random.randint(0,5)

print('JOGO DA ADIVINHAÇÃO')
print('')

numeroUser = int(input('Digite um número de 0 a 5: '))

if numero == numeroUser:
    print('Voce acertou !')
else: 
    print('Você errou !')
print('Número Sorteado: {}'.format(numero))
