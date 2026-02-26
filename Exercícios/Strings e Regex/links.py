# Renan está desenvolvendo um sistema que verifica se os links de sites parceiros começam com https:// e terminam com .com. 
# Esses critérios são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan a criar um programa que realize 
# essa validação de forma automática.

url = input("Insira a URL: ")

if url.startswith("https://") and url.endswith(".com"):
    print("URL válida!")
else:
    print("URL inválida!")


# Pode ser usado para encontrar em qualquer parte da URL, ao invés de procurar no início e no fim: 
# if "https://" in url and ".com" in url:
#    print("O site é válido.")
# else:
#    print("O site é inválido.")