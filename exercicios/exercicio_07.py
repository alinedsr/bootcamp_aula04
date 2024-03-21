#    Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

idades_validas: list = [idade for idade in idades if idade >= 18]

for i in idades_validas:
    print(i)