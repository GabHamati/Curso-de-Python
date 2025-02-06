# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem
# ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

def triangulo():
    a = float(input("Digite o primeiro lado: "))
    b = float(input("Digite o segundo lado: "))
    c = float(input("Digite o terceiro lado: "))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Os valores fornecidos não formam um triângulo."

print(triangulo())

