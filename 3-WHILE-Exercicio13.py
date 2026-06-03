### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Não sabia como era API paginada, pedi para IA criar isto para mim

dados_api = {
    1: ["João", "Maria", "Pedro"],
    2: ["Ana", "Carlos", "Beatriz"],
    3: ["Lucas", "Fernanda"],
}

# total_paginas = len(dados_api)
# pagina_atual = 1
# while pagina_atual <= total_paginas:
#     print(dados_api[pagina_atual])
#     pagina_atual += 1
# Esta foi a minha solução para o exercício, 
# mas IA pediu para imprimir a lista completa
# Fiz de novo, foi desafiador, mas ficou bom e bem legal

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