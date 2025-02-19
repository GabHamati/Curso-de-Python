# 1) Faça um programa que pergunte o preço de três produtos e informe
# qual produto você deve comprar, sabendo que a decisão é sempre o mais barato.

produto1 = float(input("Digite o valor do produto 1: "))
produto2 = float(input("Digite o valor do produto 2: "))
produto3 = float(input("Digite o valor do produto 3: "))

if produto1 <= produto2 and produto1 <= produto3:
    print("O produto que deve ser comprado é o produto 1")

elif produto2 <= produto1 and produto2 <= produto3:
    print("O produto que deve ser comprado é o produto 2")

else:
    print("O produto que deve ser comprado é o produto 3")