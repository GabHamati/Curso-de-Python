# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro.
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input("Insira o tipo de combustível (A - álcool, G - gasolina): ")
litros_vendidos = float(input("Insira quantos litros foram vendidos: "))

if combustivel == "A":
    if litros_vendidos <= 20:
        desconto = 1.9 * 0.97
        valor_final = litros_vendidos * desconto
        print(f'O valor com desconto a ser pago é de R$ {valor_final:.2f}')

    else:
        desconto = 1.9 * 0.95
        valor_final = litros_vendidos * desconto
        print(f'O valor com desconto a ser pago é de R$ {valor_final:.2f}')

else:
    if litros_vendidos <= 20:
        desconto = 2.5 * 0.96
        valor_final = litros_vendidos * desconto
        print(f'O valor com desconto a ser pago é de R$ {valor_final:.2f}')

    else:
        desconto = 2.5 * 0.94
        valor_final = litros_vendidos * desconto
        print(f'O valor com desconto a ser pago é de R$ {valor_final:.2f}')