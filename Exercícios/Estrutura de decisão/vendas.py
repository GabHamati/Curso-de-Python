# 8) Faça um programa utilizando python que receba os valores das vendas dos meses de janeiro, fevereiro, março e abril
# e calcule a média ponderada das vendas dos quatro meses, considerando que janeiro e março tem peso 1, fevereiro e abril
# tem peso 4 cada. No final mostrar as vendas dos quatro meses e a média ponderada calculada; se as vendas de determinado mês
# forem superiores à média calculada, apresentar mensagem “Vendas do mês xxxxxxx superior à média do período”.

vendasjan = int(input("Insira os valores das vendas de Janeiro: "))
vendasfev = int(input("Insira os valores das vendas de Fevereiro: "))
vendasmar = int(input("Insira os valores das vendas de Março: "))
vendasabr = int(input("Insira os valores das vendas de Abril: "))

mediapond = ((vendasjan * 1) + (vendasfev * 4) + (vendasmar * 1) + (vendasabr * 4) / 10)

if vendasjan > mediapond:
    print("Vendas do mês de Janeiro superior à média do período")

elif vendasfev > mediapond:
    print("Vendas do mês de Fevereiro superior à média do período")

elif vendasmar > mediapond:
    print("Vendas do mês de Março superior à média do período")

if vendasabr > mediapond:
    print("Vendas do mês de Abril superior à média do período")

else:
    print("Vendas em Janeiro: ", vendasjan, "\n Vendas em Fevereiro: ", vendasfev, "\n Vendas em Março: ", vendasmar, "\n Vendas em Abril: ", vendasabr, "\n Média ponderada: ", mediapond)