# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for i in range(5):
    num = int(input(f"Insira o {i+1}º número: "))
    numeros.append(num)

print(f"O números inseridos foram {numeros}")