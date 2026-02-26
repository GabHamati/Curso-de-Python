# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:
# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
# O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

renda = float(input("Insira sua renda mensal: "))
parcela_desejada = float(input("Insira o valor da parcela desejada: "))

if renda > 2000 and renda * 0.3 >= parcela_desejada:
    print("Empréstimo aprovado.")
elif renda <= 2000:
    print("Empréstimo negado por renda insuficente.")
else:
    print("Empréstimo negado: Parcela acima de 30% da renda")