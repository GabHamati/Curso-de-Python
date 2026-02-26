#Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. 
# Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

# Ajude Ana a decidir entre usar um laço for ou while. Escreva o programa usando o laço que você acredita ser mais adequado.

clientes = []

for i in range(1,6):
    nome = input(f"Insira o nome do {i}º cliente:")
    clientes.append(nome)

print(clientes)