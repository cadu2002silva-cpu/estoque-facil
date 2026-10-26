# Guia 01 — MVP: Terminal e Memória

Este guia documenta a primeira entrega do projeto Estoque Fácil: um programa simples no terminal que cadastra produtos, lista todos e encerra pelo menu. Os dados ficam apenas na memória (somente durante a execução).

---

## Ideia por trás do código

O programa armazena produtos em uma lista chamada `produtos`. Cada produto é um dicionário com duas chaves: `nome` e `quantidade`.

O fluxo é um menu em loop (`while True`) que oferece três opções:

1. **Cadastrar produto** — pede nome e quantidade, valida e adiciona à lista.
2. **Listar produtos** — percorre a lista e imprime cada produto.
3. **Sair** — encerra o programa.

Tudo fica na memória: se fechar o programa, os dados somem. A persistência (JSON, SQLite) vem nas próximas etapas.

---

## Regras decididas para esta etapa

| Regra | Comportamento |
|-------|---------------|
| Nome vazio | Rejeitado com mensagem de erro |
| Quantidade negativa | Rejeitada com mensagem de erro |
| Quantidade não inteira | Rejeitada com mensagem de erro |
| Nome duplicado | Não permite cadastrar o mesmo nome duas vezes |

---

## Código a ser escrito

Arquivo: `main.py`

```python
# Estoque Fácil — MVP (Primeira entrega)
# Produtos ficam apenas na memória (enquanto o programa está rodando).

produtos = []


def cadastrar_produto(nome, quantidade):
    """Cadastra um produto na lista de produtos.

    Regras:
    - O nome não pode estar vazio.
    - A quantidade deve ser um número inteiro maior ou igual a zero.
    - Não permite cadastrar o mesmo nome duas vezes.
    """
    if not nome or not nome.strip():
        print("Erro: o nome do produto não pode ficar vazio.")
        return False

    if quantidade < 0:
        print("Erro: a quantidade não pode ser negativa.")
        return False

    for produto in produtos:
        if produto["nome"].lower() == nome.strip().lower():
            print(f"Erro: o produto '{nome}' já está cadastrado.")
            return False

    produtos.append({"nome": nome.strip(), "quantidade": quantidade})
    print(f"Produto '{nome}' cadastrado com quantidade {quantidade}.")
    return True


def listar_produtos():
    """Exibe todos os produtos cadastrados."""
    if not produtos:
        print("Não há produtos cadastrados.")
        return

    print("\n--- Produtos em estoque ---")
    for produto in produtos:
        print(f"- {produto['nome']}: {produto['quantidade']} unidade(s)")
    print("---------------------------\n")


def menu():
    """Exibe o menu principal e processa a opção escolhida pelo usuário."""
    while True:
        print("\n=== Estoque Fácil ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade_text = input("Quantidade: ")

            try:
                quantidade = int(quantidade_text)
            except ValueError:
                print("Erro: a quantidade deve ser um número inteiro.")
                continue

            cadastrar_produto(nome, quantidade)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
```

---

## Como executar

No terminal, dentro da pasta `estoque-facil`:

```bash
python main.py
```

Exemplo de uso:

```
=== Estoque Fácil ===
1. Cadastrar produto
2. Listar produtos
3. Sair
Escolha uma opção: 1
Nome do produto: Arroz
Quantidade: 10
Produto 'Arroz' cadastrado com quantidade 10.

=== Estoque Fácil ===
1. Cadastrar produto
2. Listar produtos
3. Sair
Escolha uma opção: 2

--- Produtos em estoque ---
- Arroz: 10 unidade(s)
---------------------------

=== Estoque Fácil ===
1. Cadastrar produto
2. Listar produtos
3. Sair
Escolha uma opção: 3
Encerrando o programa. Até logo!
```

---

## O que vem depois

Na próxima etapa (Regras e funções) vamos adicionar:

- Busca por nome
- Entradas e saídas de estoque
- Identificação de estoque baixo
- Testes com `pytest`

Após isso, passaremos para persistência em JSON e depois SQLite.
