# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

media = []

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f"Insira a {j+1}ª nota do {i+1}º aluno: "))
        notas.append(nota)
    media_aluno = sum(notas) / 4
    if media_aluno >= 7:
        media.append(media_aluno)

print(f"A quantidade de alunos com média maior ou igual a 7 é de {len(media)} alunos")