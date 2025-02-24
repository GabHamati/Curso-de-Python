# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

consoantes = []

for i in range(10):
    caracter = input(f"Insira o {i+1}º caracter: ").lower()
    if caracter not in ['a', 'e', 'i', 'o', 'u']:
        consoantes.append(caracter)

print(f"Foram informadas {len(consoantes)} consoantes. As consoantes informadas foram {consoantes}")
