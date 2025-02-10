# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
# inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
# tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

numero = int(input("Insira o número que deseja ver a tabuada: "))

if numero < 1 or numero > 10:
    print("O número deve ser entre 1 e 10.")

else:
    print(f"Tabuada do {numero}:")
    for num in range (1, 11):
        resultado = numero * num
        print(f"{numero} x {num} = {resultado}")