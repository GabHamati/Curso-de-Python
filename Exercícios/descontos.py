# Operadores de comparação
# 3) O valor da compra deverá ser solicitado ao iniciar o código
# Condições:
# Compra abaixo de R$ 100,00 - 5% de desconto
# Compras acima de R$ 100,00 - 10% de desconto
# Compras acima de R$ 200,00 - 20% de desconto

compra = float(input('Digite o valor da compra: '))

if compra < 100:
    desconto = compra * 0.95
    print(f'O valor com desconto é de R$ {desconto:.2f}')
elif compra < 200:
    desconto = compra * 0.9
    print(f'O valor com desconto é de R$ {desconto:.2f}')
else:
    desconto = compra * 0.8
    print(f'O valor com desconto é de R$ {desconto:.2f}')