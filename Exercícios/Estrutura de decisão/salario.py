# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 8% para o INSS, 5% para o sindicato,
# e o IR conforme a tabela abaixo:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# faça um programa que nos informe  :
# salário bruto.
# quanto pagou de IR.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

salario_hora = float(input("Insira seu salário por hora: R$ "))
horas_mensais = int(input("Insira quantas horas você trabalhou no mês: "))

salario_bruto = salario_hora * horas_mensais

if salario_bruto <= 900:
    IR = 0

elif 900 < salario_bruto <= 1500:
    IR = salario_bruto * 0.05

elif 1500 < salario_bruto <= 2500:
    IR = salario_bruto * 0.1
else:
    IR = salario_bruto * 0.2

INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - INSS - IR - sindicato

print(f'Salário bruto: R$ {salario_bruto:.2f}')
print(f'Desconto de Imposto de Renda: R$ {IR:.2f}')
print(f'Desconto de INSS: R$ {INSS:.2f}')
print(f'Desconto de sindicato: R$ {sindicato:.2f}')
print(f'Salário líquido: R$ {salario_liquido:.2f}')