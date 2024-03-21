#    Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario: dict = {"Karol G" "" : 33, "Sia"  : 48, "Jessie J"  : 35, "Lady Gaga"  : 37, "Demi Lovato"  : 31, "Taylor Swif"  : 34, "Rihanna"  : 36, "Shakira"  : 47}
nomes: list = list(dicionario.keys())
idades: list = list(dicionario.values())

for nome in nomes:
    print("Nome: ", nome)

for idade in idades:
    print("Idade: ", idade)