# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e 
# R$0,45 para viagens mais longas.

distancia = int(input('Digite a distância da sua viagem (Km): '))

if distancia <= 200:
   valor = distancia * 0.50
else:
   valor = distancia * 0.45

print('Sua passagem vai custar: R$ {}'.format(valor))
