# Crie um algoritmo que leia o preço de um produto e moste seu novo preço, com 5% de desconto.

prod = float(input('Digite o preço do produto:R$ '))

pdesc = prod - (prod * 5 / 100)

print('Preço com 5% de desconto:R$ {:.2f}'.format(pdesc))
