# Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo, ela percebeu que usou a palavra "bom" 
# repetidamente, quando queria expressar algo mais forte, como "ótimo". Para economizar tempo, Nathalia quer substituir automaticamente 
# todas as ocorrências da palavra "bom" por "ótimo" no texto.

# Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir 
# o texto com as alterações aplicadas.

import re

texto = input("Insira o texto que deseja revisar: ")
palavra_antiga = input("Insira a palavra que deseja substituir: ")
palavra_nova = input("Insira a palavra que irá substituir: ")

texto_final = re.sub(rf"\b{palavra_antiga}", palavra_nova, texto)

print(texto_final)