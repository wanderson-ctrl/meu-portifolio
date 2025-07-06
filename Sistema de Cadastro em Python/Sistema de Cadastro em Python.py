# Mensagem de boas-vindas com meu nome
print("Bem-vindo a livraria do Wanderson Nogueira")

# Lista onde serão armazenados os livros (cada livro será um dicionário)
lista_livro = []

# ID global que será incrementado automaticamente
id_global = 0


# Função para cadastrar um novo livro
def cadastrar_livro(id):
    print("\nCadastro de novo livro:")
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")

    # Criação de um dicionário para armazenar os dados do livro
    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    # Adiciona o livro na lista
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!\n")


# Função para consultar livros
def consultar_livro():
    while True:
        print("\nConsulta de Livros")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar por ID")
        print("3 - Consultar por Autor")
        print("4 - Retornar ao Menu Principal")

        opcao = input("Escolha a opção desejada: ")

        if opcao == '1':
            # Exibir todos os livros
            print("\nTodos os livros cadastrados:")
            for livro in lista_livro:
                print(livro)

        elif opcao == '2':
            # Consultar por ID
            try:
                id_livro = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_livro:
                        print(livro)
                        encontrado = True
                if not encontrado:
                    print("ID não encontrado.")

            except ValueError:
                print("ID inválido. Digite um número.")

        elif opcao == '3':
            # Consultar por Autor
            autor_livro = input("Digite o nome do autor: ")
            encontrados = False
            for livro in lista_livro:
                if livro['autor'].lower() == autor_livro.lower():
                    print(livro)
                    encontrados = True
            if not encontrados:
                print("Nenhum livro encontrado para este autor.")

        elif opcao == '4':
            # Retorna ao menu principal
            break

        else:
            print("Opção inválida. Tente novamente.")


# Função para remover livro
def remover_livro():
    while True:
        try:
            id_livro = int(input("Digite o ID do livro que deseja remover: "))
            for livro in lista_livro:
                if livro['id'] == id_livro:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("ID inválido. Tente novamente.")

        except ValueError:
            print("Entrada inválida. Digite um número.")


# Menu principal do sistema
while True:
    print("\nMenu Principal:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Sair")

    opcao_menu = input("Escolha a opção desejada: ")

    if opcao_menu == '1':
        # Incrementa o ID e chama a função de cadastro
        id_global += 1
        cadastrar_livro(id_global)

    elif opcao_menu == '2':
        consultar_livro()

    elif opcao_menu == '3':
        remover_livro()

    elif opcao_menu == '4':
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
