# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    nota = float(input(f"Insira a {i+1}º nota: "))
    notas.append(nota)

media = sum(notas) / 4

print(f"As notas informadas foram {notas} e a média é {media}")