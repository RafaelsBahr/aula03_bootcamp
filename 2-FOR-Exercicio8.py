# 8. Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]
# usuarios_validos é nova variavel, começa com [colchete] então é tipo lista
# Esta lista vai ser construida com o que tem dentro do colchetes, que está dividido em 3 partes
# 1 - usuario = o que vai entrar na nova lista
# 2 - for usuario in usuarios = loop que vai analisar cada usuario da lista usuários
# 3 - if usuario["email"] = Condicional que só vai permitir que adicione usuarios que tem "email" = True. Como é string, True só precisa qualquer valor, string vazia é False 
print(usuarios_validos)
# Mostra na tela a nova lista criada