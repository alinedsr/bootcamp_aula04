#    Dada uma string, contar a frequência de cada caractere usando um dicionário.

# Definir a string
nome: str = input("Digite o seu nome: ")

# Inicializar um dicionário para armazenar a contagem de cada caractere
frequencia_caracteres = {}

# Iterar sobre a string e atualizar a contagem de cada caractere no dicionário
for caractere in nome:
    if caractere in frequencia_caracteres:
        frequencia_caracteres[caractere] += 1
    else:
        frequencia_caracteres[caractere] = 1

# Imprimir o dicionário de frequência de caracteres
print("Frequência de cada caractere:")

for caractere, frequencia in frequencia_caracteres.items():
    print(f"{caractere}: {frequencia}")