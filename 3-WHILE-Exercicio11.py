### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
palavra_chave = input("Escreva sua palavra_chave: ")
while palavra_chave != "sair":
    palavra_chave = input("Escreva outra palavra_chave até sair: ")
print("Parabéns, você saiu.")

# dados = []
# entrada = ""
# while entrada.lower() != "sair":
#     entrada = input("Digite um valor (ou 'sair' para terminar): ")
#     if entrada.lower() != "sair":
# print(dados)
# Minha solução está diferente do curso
# - Curso armazena todas entradas até "sair"
# - Boa pratica de .lower() para facilitar "sair" quando usuario digita