#    Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

s: str = input("Digite o seu nome: ")

def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres(s))