# Faça um programa que implemente uma caixa registradora rudimentar.
# O programa deverá receber um número desconhecido de valores referentes
# aos preços das mercadorias. Um valor zero deve ser informado pelo operador
# para indicar o final da compra. O programa deve então mostrar o total da compra e
# perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar
# o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para
# registrar a próxima compra.

valor_compra = 0

while True:
    operacao = float(input("Insira o valor do produto ou 0 para encerrar a compra: R$ "))
    if operacao == 0:
        break
    else:
        valor_compra += operacao

print(f"O total da compra é de R$ {valor_compra:.2f}")

while True:
    pagamento = float(input("Insira o valor pago pelo cliente: R$ "))
    if pagamento >= valor_compra:
        troco = pagamento - valor_compra
        print(f"Compra efetuada. O troco é de R$ {troco}")
        break
    else:
        print("O valor pago pelo cliente é insuficiente.")




















