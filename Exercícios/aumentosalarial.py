# Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Insira o salário atual: R$ "))

if salario <= 280:
    aumento = 0.20
    salario_aumento = salario * 1.2

elif 280 < salario <= 700:
    aumento = 0.15
    salario_aumento = salario * 1.15

elif 700 < salario <= 1500:
    aumento = 0.10
    salario_aumento = salario * 1.1

else:
    aumento = 0.05
    salario_aumento = salario * 1.05

valor_aumento = salario_aumento - salario

print(f'O salário antes do reajuste era de R$ {salario:.2f}')
print(f'O aumento aplicado foi de {aumento*100}%')
print(f'O valor do aumento foi de R$ {valor_aumento:.2f}')
print(f'O salário após o aumento é de R$ {salario_aumento:.2f}')