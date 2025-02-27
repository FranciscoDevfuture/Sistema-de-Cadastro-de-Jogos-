import os

# Lista para armazenar os jogos cadastrados
jogos = []

# Função para carregar os jogos do arquivo txt
def carregar_jogos():
    if os.path.exists('jogos_cadastrados.txt'):
        with open('jogos_cadastrados.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(', ')
                if len(partes) == 4:
                    nome, genero, ano, plataforma = partes
                    jogos.append({
                        "nome": nome.split(': ')[1],
                        "genero": genero.split(': ')[1],
                        "ano": ano.split(': ')[1],
                        "plataforma": plataforma.split(': ')[1]
                    })
        print("Jogos carregados de 'jogos_cadastrados.txt'.")

# Função para cadastrar um novo jogo
def cadastrar_jogo():
    nome = input("Digite o nome do jogo: ")
    genero = input("Digite o gênero do jogo: ")
    ano = input("Digite o ano de lançamento do jogo: ")
    plataforma = input("Digite a plataforma do jogo: ")
    # Dicionário do jogo
    jogo = {
        "nome": nome,
        "genero": genero,
        "ano": ano,
        "plataforma": plataforma
    }

    jogos.append(jogo)
    print(f"Jogo '{nome}' cadastrado com sucesso!")

# Função para visualizar todos os jogos cadastrados
def visualizar_jogos():
    if not jogos:
        print("Nenhum jogo cadastrado.")
    else:
        for i, jogo in enumerate(jogos, start=1):
            print(f"{i}. Nome: {jogo['nome']}, Gênero: {jogo['genero']}, Ano: {jogo['ano']}, Plataforma: {jogo['plataforma']}")

# Função para salvar os jogos cadastrados em um arquivo txt
def salvar_jogos():
    with open('jogos_cadastrados.txt', 'w') as arquivo:
        for jogo in jogos:
            arquivo.write(f"Nome: {jogo['nome']}, Gênero: {jogo['genero']}, Ano: {jogo['ano']}, Plataforma: {jogo['plataforma']}\n")
    print("Jogos salvos em 'jogos_cadastrados.txt'.")

# Menu principal do programa
def menu():
    carregar_jogos()
    while True:
        print("\nMENU:")
        print("1. Cadastrar jogo")
        print("2. Visualizar jogos")
        print("3. Salvar jogos")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_jogo()
        elif opcao == '2':
            visualizar_jogos()
        elif opcao == '3':
            salvar_jogos()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executar o programa
menu()