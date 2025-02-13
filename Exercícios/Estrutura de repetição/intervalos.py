# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos
# deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados
# deverá terminar quando for lido um número negativo.

intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0


while True:
    numeros = int(input("Insira o número positivo. Caso queira encerrar, insira um número negativo: "))

    if numeros < 0:
        break

    if 0 <= numeros <= 25:
        intervalo_0_25 += 1

    elif 26 <= numeros <= 50:
        intervalo_26_50 += 1

    elif 51 <= numeros <= 75:
        intervalo_51_75 += 1

    elif 76 <= numeros <= 100:
        intervalo_76_100 += 1

print(f"Intervalo entre 0 e 25: {intervalo_0_25} números")
print(f"Intervalo entre 26 e 50: {intervalo_26_50} números")
print(f"Intervalo entre 51 e 75: {intervalo_51_75} números")
print(f"Intervalo entre 76 e 100: {intervalo_76_100} números")