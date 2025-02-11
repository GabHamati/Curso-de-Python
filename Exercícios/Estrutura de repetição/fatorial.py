# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Insira o número: "))
num += 1
resultado = 1

for numero in range(1, num):
    resultado *= numero

print(f"O fatorial é {resultado}")