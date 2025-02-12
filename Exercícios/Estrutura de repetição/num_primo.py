# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que
# peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input("Insira o número: "))

for i in range (2, numero):
    if numero % i == 0:
        print("Não é um número primo")
        break

else:
    print("O número é primo")
