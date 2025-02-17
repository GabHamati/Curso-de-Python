# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
# O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que
# receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a
# média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
# calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem
# da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome
# do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

nome = input("Insira o nome do atleta: ")
saltos = []
melhor_salto = 0
pior_salto = 1000

for i in range(5):
    salto = float(input(f"Insira a distância do {i + 1}º salto: "))
    if salto > melhor_salto:
        melhor_salto = salto
    if salto < pior_salto:
        pior_salto = salto
    saltos.append(salto)

print(f"Atleta: {nome}")
print(f"Primeiro salto: {saltos[0]}")
print(f"Segundo salto: {saltos[1]}")
print(f"Terceiro salto: {saltos[2]}")
print(f"Quarto salto: {saltos[3]}")
print(f"Quinto salto: {saltos[4]}")
print(f"Melhor salto: {melhor_salto}")
print(f"Pior salto: {pior_salto}")

saltos.remove(melhor_salto)
saltos.remove(pior_salto)

media = sum(saltos) / 3

print(f"Média dos demais saltos: {media}")


