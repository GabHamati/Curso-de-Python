# Utilizando a biblioteca re do python elabore expressões regulares para
# validar o seguintes tipos de entradas validas para o sistema.
# Email, Telefone Celular, Endereço, Internet, Data, Número inteiro, Número decimal, Nome

import re

def validar_email(email):
    regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(regex_email, email):
        return True
    else:
        return False

def validar_telefone(telefone):
    regex_telefone = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    if re.match(regex_telefone, telefone):
        return True
    else:
        return False

def validar_url(url):
    regex_url = r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(\.[a-zA-Z]{2})?(\S*)?$"
    if re.match(regex_url, url):
        return True
    else:
        return False

def validar_data(data):
    regex_data = r"^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$"
    if re.match(regex_data, data):
        return True
    else:
        return False

def validar_inteiro(numero):
    regex_inteiro = r"^-?\d+$"
    if re.match(regex_inteiro, numero):
        return True
    else:
        return False

def validar_decimal(numero):
    regex_decimal = r"^-?\d+(\.\d+)?$"
    if re.match(regex_decimal, numero):
        return True
    else:
        return False

def validar_nome(nome):
    regex_nome = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$"
    if re.match(regex_nome, nome):
        return True
    else:
        return False

email = input("Digite um endereço de email: ")
if validar_email(email):
    print("O email é válido.")
else:
    print("O email é inválido.")

telefone = input("Digite um número de telefone: ")
if validar_telefone(telefone):
    print("O telefone é válido.")
else:
    print("O telefone é inválido.")

url = input("Digite um endereço de URL: ")
if validar_url(url):
    print("A URL é válida.")
else:
    print("A URL é inválida.")

data = input("Digite uma data no formato dd/mm/aaaa: ")
if validar_data(data):
    print("A data é válida.")
else:
    print("A data é inválida.")

numero_inteiro = input("Digite um número inteiro: ")
if validar_inteiro(numero_inteiro):
    print("O número inteiro é válido.")
else:
    print("O número inteiro é inválido.")

numero_decimal = input("Digite um número decimal: ")
if validar_decimal(numero_decimal):
    print("O número decimal é válido.")
else:
    print("O número decimal é inválido.")

nome = input("Digite um nome: ")
if validar_nome(nome):
    print("O nome é válido.")
else:
    print("O nome é inválido.")