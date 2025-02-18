# Um sistema possui reservado 5 posições de memória para serem utilizado como cache L1 e
# 20 posições como cache L2. Implemente um algoritmo que simule o funcionamento do
# processo de pesquisa no cache e caso ocorra um cache miss ele execute a procura no
# próximo nível de armazenamento.
# Os dados da memoria principal serão números sequenciais de 0 a 1.000.
# • O sistema deve se preocupar com o processo de inclusão e remoção dos elementos no
# cache
# Utilize Orientação Objeto, a mesma função que trata a busca no cache L1 pode ser utilizado
# para consulta no cache L2.
# Para acrescentar um pouco de realidade ao sistema utilize a função sleep no decorrer de
# consultas no cache L2 e lista principal de dados
# Exemplo Funcionamento
# Digite o número procurado? 10
# O número não foi encontrado na L1
# O número não foi encontrado na L2
# O número 10 foi encontrado na memoria principal em 2ms
# Digite o número procurado? 10
# O número foi encontrado na L1 em 0.2ms

import time

cache_l1 = [0, 1, 2, 3, 4]
cache_l2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

def memoria_principal(numero):
    time.sleep(0.002)
    return numero

def busca_sistema(numero, cache_l1, cache_l2):
    if numero in cache_l1:
        print(f'O número {numero} foi encontrado na L1 em 0.2ms')
    elif numero in cache_l2:
        print(f'O número {numero} foi encontrado na L2 em 0.5ms')
        cache_l1.append(numero)
        if len(cache_l1) > 5:
            cache_l1.pop(0)
    else:
        print(f'O número {numero} não foi encontrado na L1')
        print(f'O número {numero} não foi encontrado na L2')
        memoria_principal(numero)
        print(f'O número {numero} foi encontrado na memória principal em 2ms')
        cache_l1.append(numero)
        if len(cache_l1) > 5:
            cache_l1.pop(0)

while True:
    num = int(input("Digite o número procurado? "))
    busca_sistema(num, cache_l1, cache_l2)
