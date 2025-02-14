# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0

while True:
    voto = int(input(
        "Insira um número de 1 a 4 para votar em um dos candidatos de acordo com seu número, 5 para nulo ou 6 para votar em branco. Aperte 0 para encerrar: "))
    if voto == 0:
        break

    if voto == 1:
        candidato1 += 1

    elif voto == 2:
        candidato2 += 1

    elif voto == 3:
        candidato3 += 1

    elif voto == 4:
        candidato4 += 1

    elif voto == 5:
        nulo += 1

    elif voto == 6:
        branco += 1

    else:
        print("Número inválido.")

total_votos = candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco


if total_votos == 0:
    percentual_nulo = 0
    percentual_branco = 0
else:
    percentual_nulo = (nulo / total_votos) * 100
    percentual_branco = (branco / total_votos) * 100

print(f"Candidato 1: {candidato1}")
print(f"Candidato 2: {candidato2}")
print(f"Candidato 3: {candidato3}")
print(f"Candidato 4: {candidato4}")
print(f"Votos nulos: {nulo}")
print(f"Votos em branco: {branco}")
print(f"Percentual de votos nulos: {percentual_nulo:.2f}%")
print(f"Percentual de votos em branco: {percentual_branco:.2f}%")











