# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input("Insira a quantidade de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range (eleitores):
    voto = int(input("Informe em qual candidato deseja votar (1, 2 ou 3): "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print("Número errado. O número deve ser 1, 2 ou 3")

print(f"O candidato 1 teve {candidato1} voto(s)")
print(f"O candidato 2 teve {candidato2} voto(s)")
print(f"O candidato 3 teve {candidato3} voto(s)")