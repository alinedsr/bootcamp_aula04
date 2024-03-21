#    Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista: list = ["Python", "Java", "C++", "JavaScript"]
print(f'Lista inicial: {lista}')

lista.remove("C++")
print(f'Removido C++.')

lista.append("Ruby")
print(f'Nova lista: {lista}')
