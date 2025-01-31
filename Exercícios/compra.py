# Enviar os detalhes de uma compra com um
# maximo de 3 tentativas para compras confirmadas.
# O usuário deve inserir o valor da compra
# Enviar uma mensagem de confirmação de compra e entrega
# Enviar mensagem confirmando o envio dos detalhes.

confirmacao_compra = True
valor_compra = float(input('Digite o valor da compra: '))

for enviar in range(3):
    if confirmacao_compra:
        print(f'Compra no valor de R$ {valor_compra:.2f} e entrega confirmadas.')
        print('Detalhe enviado para seu email.')
        break

else:
    print('Erro na compra.')