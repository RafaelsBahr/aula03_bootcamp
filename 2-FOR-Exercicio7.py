
# 7. Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]
# numeros é uma variavel do tipo lista
minimo = min(numeros)
# Definiu nova variável minimo como o menor numero da lista numeros - no caso minimo = 10
maximo = max(numeros)
# Definiu nova variável maximo como o maior numero da lista numeros - no caso maximo = 50
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
# normalizados é nova variavel > [colchetes significa que é uma lista]
# (x - minimo) é uma função matematica, mas x é uma variavel que não tem valor ainda
# (maximo - minimo) é outra função, basicamente 50 - 10
# for x in numeros é mesma coisa que para "para cada numero dentro da lista numeros" e cada numero = x
# Logo valor de x é 10, depois 20, depois 30...
# E assim ele preenche a lista
print(normalizados)
# Mostra na tela valor de normalizados