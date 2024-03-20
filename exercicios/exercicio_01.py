#    Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista: list = [1,2,3,4,5,6,7,8,9,10]

try:
    for numero in lista:
        print(numero ** 2)
except Exception as e:
    print(e)