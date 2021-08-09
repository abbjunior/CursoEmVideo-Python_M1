# Crie um algoritmo que leia quanto deinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar. Considerando US$1,00 = R$3,27

real = float(input('Informe quanto você tem na carteira: R$ '))

conversao = real / 3.27

print('Você pode comprar US$ {}'.format(conversao))
