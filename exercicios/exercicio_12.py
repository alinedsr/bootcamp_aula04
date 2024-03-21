#    Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1: dict = {"a": 1, "c": 3, "b": 2}
# dicionario2: dict = {"d": 4}

# dicionario_fundido: dict = {**dicionario1, **dicionario2}

# print(dicionario_fundido)

dicionario_01: dict = {"a": 1, "b": 2, "c": 3}
dicionario_02: dict = {"d": 3, "e": 2, "f": 1}

novo_dicionario = {}
novo_dicionario.update(dicionario_01)
novo_dicionario.update(dicionario_02)

for chave, valor in novo_dicionario.items():
    print(chave, valor)



# ___________________________________________________ #
#Explicação Chat GPT

# # Se estivermos comparando o desempenho entre a atualização de dicionários usando o método update() 
#     e o uso do operador de unpacking (**) para combinar grandes volumes de dados em Python, 
#     as diferenças de desempenho geralmente são mínimas.

# # Ambos os métodos têm complexidade de tempo O(n), onde n é o número de elementos nos dicionários a serem combinados. 
# Eles iteram sobre os elementos dos dicionários e adicionam ou atualizam os pares chave-valor no dicionário de destino.

# # No entanto, há algumas considerações a serem feitas:

# #     Uso de memória: O operador de unpacking (**) cria um novo dicionário
#  contendo todos os pares chave-valor dos dicionários originais, enquanto o método update() 
# atualiza o dicionário de destino inplace. Isso significa que o operador de unpacking pode
# exigir mais memória, pois cria um novo dicionário, enquanto update() apenas modifica o dicionário existente.

# #     Clareza do código: O operador de unpacking (**) é frequentemente considerado mais legível 
# e conciso do que o método update(), especialmente quando você está combinando mais de dois dicionários.

# # Em termos de desempenho puro, em muitos casos, a diferença é tão pequena que não é perceptível. 
# A escolha entre update() e operador de unpacking (**) geralmente se resume a preferências de 
# estilo de código e a necessidades específicas do seu programa em relação ao uso de memória. 
# Se você está lidando com grandes volumes de dados e a eficiência de memória é crítica, 
# pode ser útil realizar testes de desempenho em seu contexto específico para determinar qual método é mais adequado.