# Operadores de comparação
# Uma nota deverá ser informada ao iniciar o programa.
# Condições:
# Nota maior ou igual a 9 - Excelente
# Nota maior ou igual a 7 - Bom
# Nota maior ou igual a 5 - Mediano
# Nota menor que 5 - Reprovado.

nota = float(input('Insira a nota: '))

if nota >= 9:
    print('Excelente')
elif nota >= 7:
    print('Bom')
elif nota >= 5:
    print('Mediano')
else:
    print('Reprovado')