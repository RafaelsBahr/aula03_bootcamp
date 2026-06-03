# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

# Objetivo: categorias = {"Eletrônicos": 2000, "Livros", 200}

valor_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria not in valor_categoria:
        valor_categoria[categoria] = valor
    else:
        valor_categoria[categoria] += valor

print(valor_categoria)

# Este foi dificil, e sem ajuda da IA diretamente