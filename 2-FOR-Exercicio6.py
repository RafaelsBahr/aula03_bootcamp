# 6. Contagem de Palavras em Textos
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "a raposa marrom salta sobre o cachorro preguiçoso"
# texto é uma string que é uma frase comprida
palavras = texto.split()
# palavras é uma lista de palavras
print(palavras)
print(type(palavras))

contagem_palavras = {}
# O dicionário vai ser necessário e começa vazio

for palavra in palavras:
    # palavra é tipo uma variavel "criada" para usar durante "for"
    # Significa "para cada palavra dentro da lista de palavras..."
    if palavra in contagem_palavras:
        # Se a palavra "da vez" está no dicionário contagem_palavras
        contagem_palavras[palavra] += 1 
        # +1 no valor dela
    else:
        # Se a palavra "da vez" NÃO está no disicionário contagem_palavras
        contagem_palavras[palavra] = 1
        # Adicona a palavra como chave no dicionário e define valor como 1
print(contagem_palavras)
# Depois de repetir o "FOR" para todas palavras da frase, vai mostrar dicionário
# com todas palavras e quantidade de vezes que repete
