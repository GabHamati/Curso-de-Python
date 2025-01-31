# O programa deve calcular a quantidade de latas de tinta para pintar uma parede
# O usuário deverá informar o rendimento da lata de tinta, altura e largura.

import math

rend = int(input("Informe o rendimento da lata de tinta: "))
altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))

qtd_latas = math.ceil((altura * largura) / rend)

print(f'Serão necessárias {qtd_latas} de tinta.')