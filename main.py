produtos = []


def cadastrar_produto(nome, quantidade):
    if not nome or not nome.strip():
        print('Erro: o nome do produto não pode ficar vazio.')
        return False

    if quantidade < 0:
        print('Erro, a quantidade não pode ser negativa.')
        return False

    for produto in produtos:
        if produto["nome"].lower() == nome.strip().lower():
            print(f"Erro: o produto '{nome}' já está cadastrado.")
            return False

    produtos.append({'nome': nome.strip(), 'quantidade': quantidade})
    print(f'Produto '{nome}' cadastrado com sucesso.')
    return True


def listar_produtos():
    if not produtos:
        print("Não há produtos cadastrados.")
        return

    print('\n--- Produtos em estoque ---')
    for produto in produtos:
        print(f'- {produto["nome"]}: {produto["quantidade"]} unidade(s)')
    print('----------------------------\n')

def menu():
    while true:
        print('\n=== Estoque Fácil ===')
        print('1. Cadastrar produto')
        print('2. Listar produtos')
        print('3. Sair')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            nome = input('Nome do produto; ')
            quantidade_text = input('Quantidade: ')

            try:
                quantidade = int(quantidade_text)
            except ValueError:
                print('Erro: a quantidade dever ser um número inteiro.')
                continue

        elif opcao =='2':
            listar_produtos()

        elif opcao == '3':
            print('Encerrando o programa. Até logo!')
            breako

        else:
            print('Opção inválida. Tente novamente.')

    if __namw__ == '__main__':
        menu()

                

        