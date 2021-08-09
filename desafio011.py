# Crie um algoritmo que leia a largura e altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: ' ))

area = larg * alt

print('Sua parede tem a dimensão de {} x {}\nsua área é de {}m²\n'.format(larg, alt, area))

tinta = area / 2

print('Para pintar essa parede, você precisará de {} litros de tinta'.format(tinta))
