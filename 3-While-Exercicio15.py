### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = [1, 2, 3, "parar", 4, 5]
n_item = 0

while lista[n_item] != "parar":
    print(f"O item atual é: {lista[n_item]}")
    n_item += 1
print(f'Você chegou no item {n_item + 1} "{lista[n_item]}"')

# No começo só fiquei na dúvida se lista e valor especificio eram fornecidos pelo usuário
# Daí ia colocou lista para mim, resto fiz sozinho e achei fácil