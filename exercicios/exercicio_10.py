#    Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 40, 50, 60, 100]

numeros_pares: list = [numero for numero in numeros if numero %  2 == 0]
numeros_impares: list = [numero for numero in numeros if numero %  2 != 0]

print(f'Números pares: {numeros_pares}')

print(f'Números impares: {numeros_impares}')