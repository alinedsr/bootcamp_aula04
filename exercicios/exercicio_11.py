#    Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos: list = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for i in produtos:
    print(f'Lista Original: {i}')

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

for i in produtos:
    print(f'Lista Atualizada: {i}')