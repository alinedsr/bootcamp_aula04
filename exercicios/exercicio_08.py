#    Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

def ordernar_lista_por_nome(e):
  return e["nome"]

#tamanho do nome: len(e["nome"])

lista_pessoas: list = [
    {"nome" : "Karol G", "idade" : 33},
    {"nome" : "Sia", "idade" : 48},
    {"nome" : "Jessie J", "idade" : 35},
    {"nome" : "Lady Gaga", "idade" : 37},
    {"nome" : "Demi Lovato", "idade" : 31},
    {"nome" : "Taylor Swift", "idade" : 34},
    {"nome" : "Rihanna", "idade" : 36},
    {"nome" : "Shakira", "idade" : 47}
]

# Decrescente
# lista_pessoas.sort(reverse=True, key=ordernar_lista_por_nome) 
lista_pessoas.sort(reverse=False, key=ordernar_lista_por_nome)

for pessoa in lista_pessoas:
    print(pessoa)