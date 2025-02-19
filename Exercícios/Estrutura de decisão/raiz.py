# 3) Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

num = float(input("Insira o número: "))

raiz = num ** 0.5

if num < 0:
    print("Número inválido")

else:
    print("A raiz quadrada do número é: ", raiz)