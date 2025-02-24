# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(10):
    num = float(input(f"Insira o {i+1}º número: "))
    numeros.append(num)

numeros.reverse()

print(f"Os número inseridos em ordem inversa são {numeros}")
