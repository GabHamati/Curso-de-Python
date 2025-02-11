# Faça um programa que imprima na tela apenas os números ímpares entre o intervalo de números inteiros fornecidos pelo usuário.

num1 = int(input("Insira o menor número: "))
num2 = int(input("Insira o maior número: "))
num1 += 1

if num1 > num2:
    print("O primeiro valor deve ser menor que o segundo valor.")

else:
    for numeros in range(num1, num2):
        if numeros % 2 != 0:
            print(numeros)
