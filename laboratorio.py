dados_api = {
    1: ["João", "Maria", "Pedro"],
    2: ["Ana", "Carlos", "Beatriz"],
    3: ["Lucas", "Fernanda"],
}

lista_completa = []
total_paginas = len(dados_api)
pagina_atual = 1
while pagina_atual <= total_paginas:
    item_atual = 0
    total_itens = len(dados_api[pagina_atual])
    while item_atual < total_itens:
        lista_completa.append(dados_api[pagina_atual][item_atual])
        item_atual += 1
    pagina_atual += 1
print(lista_completa)



# total_paginas = len(dados_api)
# pagina_atual = 1
# lista_completa = []
# while pagina_atual <= total_paginas:
#         itens_na_lista = len(dados_api[pagina_atual])
#         item_atual = 0
#         while item_atual <= itens_na_lista:
#                 lista_completa.append(item_atual)