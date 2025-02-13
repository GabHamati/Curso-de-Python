# O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00

# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

valor_100 = 0
valor_101 = 0
valor_102 = 0
valor_103 = 0
valor_104 = 0
valor_105 = 0

while True:
    codigo = int(input("Insira o código do item pedido ou 0 para encerrar o pedido: "))

    if codigo == 0:
        break

    if codigo == 100:
        quantidade = int(input("Insira quantidade de cachorro quente que foi comprado: "))
        valor_100 += quantidade * 1.2

    if codigo == 101:
        quantidade = int(input("Insira quantidade de bauru simples que foi comprado: "))
        valor_101 += quantidade * 1.3

    if codigo == 102:
        quantidade = int(input("Insira quantidade de bauru com obo que foi comprado: "))
        valor_102 += quantidade * 1.5

    if codigo == 103:
        quantidade = int(input("Insira quantidade de hambúrguer que foi comprado: "))
        valor_103 += quantidade * 1.2

    if codigo == 104:
        quantidade = int(input("Insira quantidade de cheeseburguer que foi comprado: "))
        valor_104 += quantidade * 1.3

    if codigo == 105:
        quantidade = int(input("Insira quantidade de refrigerante que foi comprado: "))
        valor_105 += quantidade * 1

total_compra = sum((valor_100, valor_101, valor_102, valor_103, valor_104, valor_105))

print(f"O valor em cachorro quente é de: R$ {valor_100:.2f}")
print(f"O valor em bauru simples é de: R$ {valor_101:.2f}")
print(f"O valor em bauru com ovo é de: R$ {valor_102:.2f}")
print(f"O valor em hambúrguer é de: R$ {valor_103:.2f}")
print(f"O valor em cheeseburguer é de: R$ {valor_104:.2f}")
print(f"O valor em refrigerante é de: R$ {valor_105:.2f}")
print(f"O valor total do pedido é de: R$ {total_compra:.2f}")

