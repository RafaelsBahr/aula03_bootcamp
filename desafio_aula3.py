# Desafio Aula 03
# Integre na solução anterior um fluxo de While
# que repita o fluxo até que o usuário insira as informações corretas

# Não consegui adicionar while na minha solução do desafio 2 e peguei solução do curso/professor
# Descobri que solução do professor aceita espaços como nome valido, corrigido.
# ---- Solução anterior (Desafio Aula 02) ----

# Solicita ao usuário que digite seu nome
nome_valido = False
salario_valido = False
bonus_valido = False
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")

        if not nome.strip():
            raise ValueError("Nome não pode ser vazio ou apenas espaços.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float
while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            print("Salario válido:", salario)
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            print("Bonus válido:", bonus)
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
bonus_recebido = 1000 + (salario * bonus)

print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

# Usando a solução do desafio 2 do professor para elaborar desafio 3 ficou fácil