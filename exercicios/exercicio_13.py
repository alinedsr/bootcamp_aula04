#    Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 1}

estoque_positivo: dict = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

try:
    for produto, quantidade in estoque_positivo.items():
        print(f'Produto: {produto} - Quantidade em estoque: {quantidade}')
except:
    pass