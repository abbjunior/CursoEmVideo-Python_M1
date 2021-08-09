# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Informe a velocidade: '))

if velocidade > 80:
    print('Você foi multado ! {}Km/h'.format(velocidade))
    print('O valor da sua multa é calculada R$ 7,00 a cada KM acima do limite')
    multa = (velocidade - 80) * 7
    print('O valor a pagar é de R$ {},00'.format(multa))
else:
    print('Sua velocidade é: {}Km/h'.format(velocidade))
