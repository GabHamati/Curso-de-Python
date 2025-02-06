# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litros = area / 6

latas = math.ceil(litros / 18)
valor_lata = latas * 80

galoes = math.ceil(litros / 3.6)
valor_galao = galoes * 25

latas_mistura = int(litros // 18)
resto_litros = litros % 18
galoes_mistura = math.ceil(resto_litros / 3.6)
valor_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print(f'A quantidade de litros a serem comprados é: {litros:.2f}')
print(f'Em latas de 18L, o preço seria de R$ {valor_lata:.2f}')
print(f'Em galões de 3,6L, o preço seria de R$ {valor_galao:.2f}')
print(f'Uma combinação de {latas_mistura} latas de 18L e {galoes_mistura} galões de 3,6L, o preço seria de R$ {valor_mistura:.2f}')
