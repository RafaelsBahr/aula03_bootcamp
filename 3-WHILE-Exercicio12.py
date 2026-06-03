### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
numero_usuario = int(input("Digite um numero entre 5 e 10: "))
while numero_usuario > 10 or numero_usuario < 5:
    print("Errado!")
    numero_usuario = int(input("Digite um numero entre 5 e 10: "))
print(f"Parabéns, {numero_usuario} está entre 5 e 10!")

# Solução do curso/professor
# numero = int(input("Digite um número entre 1 e 10: "))
# while numero < 1 or numero > 10:
#     print("Número fora do intervalo!")
#     numero = int(input("Por favor, digite um número entre 1 e 10: "))

# print("Número válido!")

# Consegui! achei bom esse