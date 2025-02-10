# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def validar_nome():
    while True:
        nome = input("Insira sue nome: ")
        if len(nome) > 3:
            return nome
        else:
            print("Erro: O nome deve ter mais de 3 caracteres.")

def validar_idade():
    while True:
        idade = int(input("Insira sua idade: "))
        if 0 < idade < 150:
            return idade
        else:
            print("Erro: A idade deve ser um número inteiro entre 0 e 150.")

def validar_salario():
    while True:
        salario = float(input("Insira seu salário: R$ "))
        if salario > 0:
            return salario
        else:
            print("Erro: O salário deve ser maior que 0.")

def validar_sexo():
    while True:
        sexo = input("Insira seu sexo (m/f): ")
        if sexo in ('m', 'f'):
            return sexo
        else:
            print("Erro: O sexo deve ser 'm' (Masculino) ou 'f' (Feminino).")

def validar_estado_civil():
    while True:
        estado_civil = input("Insira seu estado civil ('s', 'c', 'v', 'd'): ")
        if estado_civil in ('s', 'c', 'v', 'd'):
            return estado_civil
        else:
            print("Erro: O estado civil deve ser 's', 'c', 'v' ou 'd'.")


nome = validar_nome()
idade = validar_idade()
salario = validar_salario()
sexo = validar_sexo()
estado_civil = validar_estado_civil()

print("\nInformações Validadas.")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

