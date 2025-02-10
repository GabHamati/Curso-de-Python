# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# No final mostre a soma dos números.

num1 = int(input("Insira o menor número: "))
num2 = int(input("Insira o maior número: "))
num1 += 1
soma = 0

if num1 > num2:
    print("Erro: O primeiro número deve ser menor que o segundo.")

for num in range (num1, num2):
    print(num)
    soma += num

print(f"A soma dos números é {soma}")
