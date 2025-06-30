usuarios = []
proximo_id = 1

def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.\n")
    for u in usuarios:
        print(f"ID: {u['id']} | Nome: {u['nome']} | Email: {u['email']} | Cidade: {u['cidade']}")

def criar_usuario():
    global proximo_id
    nome = input("Nome: ")
    email = input("Email: ")
    cidade = input("Cidade: ")
    usuario = {
        'id': proximo_id,
        'nome': nome,
        'email': email,
        'cidade': cidade
    }
    usuarios.append(usuario)
    proximo_id += 1
    print("Usuário criado com sucesso!\n")

def editar_usuario():
    id_editar = int(input("ID do usuário para editar: "))
    for u in usuarios:
        if u['id'] == id_editar:
            u['nome'] = input(f"Novo nome ({u['nome']}): ") or u['nome']
            u['email'] = input(f"Novo email ({u['email']}): ") or u['email']
            u['cidade'] = input(f"Nova cidade ({u['cidade']}): ") or u['cidade']
            print("Usuário atualizado com sucesso!\n")
            return
    print("Usuário não encontrado.\n")

def excluir_usuario():
    id_excluir = int(input("ID do usuário para excluir: "))
    for u in usuarios:
        if u['id'] == id_excluir:
            usuarios.remove(u)
            print("Usuário excluído com sucesso!\n")
            return
    print("Usuário não encontrado.\n")

def menu():
    while True:
        print("=== MENU ===")
        print("1 - Listar usuários")
        print("2 - Criar usuário")
        print("3 - Editar usuário")
        print("4 - Excluir usuário")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            criar_usuario()
        elif opcao == '3':
            editar_usuario()
        elif opcao == '4':
            excluir_usuario()
        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == '__main__':
    menu()
