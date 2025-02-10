# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for num in range (1, 6):
    numero = float(input(f"Insira o {num}º número: "))
    soma += numero

media = soma / 5

print(f"Soma: {soma}")
print(f"Média: {media}")