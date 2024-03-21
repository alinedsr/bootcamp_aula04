#    Dado um conjunto de números, calcular a média.

numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 40, 50, 60, 100]
media: float = sum(numeros) / len(numeros)

print(f"Soma: {sum(numeros)}")
print(f"Qtd: {len(numeros)}")
print(f"Média: {media:.2f}")