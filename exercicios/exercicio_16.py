#    Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def soma_lista(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# Exemplo de uso da função
lista_numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 40, 50, 60, 100]
resultado: float = soma_lista(lista_numeros)
print(f"A soma dos números na lista é: {resultado:.2f}")