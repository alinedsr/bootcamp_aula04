#    Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros: dict = {}

try:
    titulo_livro: str = input("Insira o título do Livro: ")
    livros["Título"] = titulo_livro
    print('-----------------------------------')
    nome_autor: str = input("Insira o nome do Autor: ")
    livros["Autor"] = nome_autor
    print('-----------------------------------')
    ano_lancamento: int = input("Insira o Ano de Lançamento: ")
    livros["Ano de Lançamento"] = ano_lancamento
    print('-----------------------------------')
except Exception as e:
    print(e)

for chave, valor in livros.items():
    print(f"{chave}: {valor}")