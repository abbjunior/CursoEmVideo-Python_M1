# Crie um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição aparece a primeira vez
# Em que posição aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" aprareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "A" aparece na posição {}'.format(frase.rfind('A')+1))
