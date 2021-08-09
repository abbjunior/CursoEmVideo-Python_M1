# Crie um algoritmo que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtd_km = float(input('Digite a quantidade de KMs percorridos: ' ))
qtd_dias = float(input('Digite a quantidade de dias: '))

total_km = 0.15 * qtd_km
total_dias = 60 * qtd_dias

total = total_km + total_dias

print('Valor total a pagar:R$ {:.2f}'.format(total))
