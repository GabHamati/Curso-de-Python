# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final
# da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
# do mais baixo, do com maior peso e do com menor peso, além da média das alturas e dos pesos dos clientes

qtd_pessoas = 0
altura_total = 0
peso_total = 0

mais_alto = 0
mais_baixo = 1000
maior_peso = 0
menor_peso = 1000

cod_alto = 0
cod_baixo = 0
cod_maior_peso = 0
cod_menor_peso = 0

while True:
    codigo = int(input("Insira seu código ou '0' para encerrar: "))
    if codigo == 0:
        break
        
    else:
        altura = int(input("Insira sua altura em centímetros: "))
        peso = float(input("Insira seu peso: "))
        altura_total += altura
        peso_total += peso
        qtd_pessoas += 1

    if altura > mais_alto:
        mais_alto = altura
        cod_alto = codigo

    if altura < mais_baixo:
        mais_baixo = altura
        cod_baixo = codigo

    if peso > maior_peso:
        maior_peso = peso
        cod_maior_peso = codigo

    if peso < menor_peso:
        menor_peso = peso
        cod_menor_peso = codigo

if qtd_pessoas > 0:
    media_altura = altura_total / qtd_pessoas
    media_peso = peso_total / qtd_pessoas

    print(f"Pessoa mais alta: Código {cod_alto} com {mais_alto} cm")
    print(f"Pessoa mais baixa: Código {cod_baixo} com {mais_baixo} cm")
    print(f"Pessoa com maior peso: Código {cod_maior_peso} com {maior_peso} kg")
    print(f"Pessoa com menor peso: Código {cod_menor_peso} com {menor_peso} cm")
    print(f"Média de altura: {media_altura} cm")
    print(f"Média de peso: {media_peso} kg")

else:
    print("Nenhuma pessoa foi inserida.")














