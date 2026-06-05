### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
max_tentativas = int(input("Digite o número máximo de tentativas de conexão: "))
tentativas = 0
while tentativas <= max_tentativas:
    teste_conexão = input("A conexão funcionou (s/n)? ")
    if teste_conexão == "s":
        tentativas += 1
        print(f"Parabéns, precisou de {tentativas} tentativa(s)!")
        break
    else:
        tentativas += 1
        print(f"Você não conseguiu conectar, você ainda tem {max_tentativas - tentativas} tentativas!")
# Achei facil e ainda aprendi break