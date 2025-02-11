# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de
# turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("Informa a quantidade de turmas: "))
total_alunos = 0

for i in range(1, turmas + 1):
    while True:
        alunos = int(input(f"Informe a quantidade de alunos da {i}ª turma: "))
        if alunos > 40:
            print("A turma não pode ter mais de 40 alunos.")
        else:
            total_alunos += alunos
            break

media = total_alunos / turmas

print(f"A média de alunos por turma é de {media}")