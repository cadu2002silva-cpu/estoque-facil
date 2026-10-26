# Estoque Fácil — plano do projeto

## Objetivo e preparação

Construir um controle de estoque de uma loja fictícia, começando no terminal e evoluindo até uma interface gráfica local. O projeto revisará Python básico e introduzirá organização de código, persistência, testes e colaboração.

- **Pasta e repositório:** `estoque-facil`.
- **Repositório no GitHub do aluno**, com participação do instrutor.
- **Encontros:** quintas-feiras, usando VS Code e Live Share.
- **Primeiro arquivo de código:** `main.py`; outros módulos surgirão conforme a necessidade.

## Funcionalidades

Cadastrar e listar produtos, buscar por nome, registrar entradas e saídas e identificar estoque baixo. Inicialmente, cada produto terá nome e quantidade. Uma saída deverá respeitar a quantidade disponível.

**Primeira entrega:** cadastrar vários produtos, listar todos e encerrar pelo menu.

## Tecnologias

| Tecnologia | Uso |
| --- | --- |
| Python 3 | Lógica e regras do estoque |
| VS Code + extensão Python + Live Share | Desenvolvimento em dupla |
| Git + GitHub | Histórico, branches e Pull Requests |
| `venv` + `pip` | Ambiente virtual e dependências |
| JSON, com `json` | Primeira persistência em arquivo |
| SQLite, com `sqlite3` | Banco local e prática de SQL |
| Tkinter + `ttk` | Janela, campos, botões e tabela |
| pytest | Testes automatizados das regras |

## Evolução

1. **Terminal e memória:** menu, cadastro e listagem; variáveis, conversões, condicionais, loops, listas e dicionários.
2. **Regras e funções:** buscas, movimentações, validações e tratamento de erros. Introduzir testes com pytest.
3. **JSON:** salvar e recuperar dados, praticando arquivos e módulos.
4. **SQLite:** transferir o armazenamento principal para o banco e praticar SQL.
5. **Tkinter:** construir a interface reaproveitando as regras já existentes.

Cada etapa pode ocupar mais de um encontro. Avançar conforme a compreensão. Introduzir classes quando ajudarem a resolver uma necessidade concreta.

## Metodologia e fluxo

O aluno conduz a maior parte da programação e explica seu raciocínio. O instrutor acompanha pelo Live Share, faz perguntas, revisa e demonstra exemplos curtos quando necessário.

Em cada encontro:

1. Revisar o aprendizado anterior com uma pequena alteração.
2. Escolher uma entrega e ler somente a etapa correspondente do guia.
3. Descrever a solução em português e escrever uma tentativa à mão.
4. Executar, experimentar entradas válidas e inválidas e corrigir.
5. Solicitar revisão da IA e discutir as sugestões.
6. Explicar e adaptar o código, registrar dúvidas e fazer um commit.

A IA apoia planejamento, explicações, pistas e revisão. O guia apresenta objetivos, conceitos, comportamento esperado e critérios de conclusão. Usar Git desde o início; introduzir branches e Pull Requests gradualmente.

## Organização da documentação

- `README.md`: apresentação, tecnologias, funcionalidades disponíveis e execução.
- `docs/PLANO.md`: etapas, conceitos e critérios de conclusão.
- `docs/METODOLOGIA.md`: dinâmica dos encontros, revisão, Git e uso de IA.
- `docs/ENCONTROS.md`: entrega, aprendizados, dificuldades individuais e próximo passo.

Ampliar a documentação conforme o projeto evoluir. Separar progressivamente interface, regras e persistência, para reaproveitar a lógica do terminal na interface gráfica.

## AGENTS.md — elaboração durante o aprendizado

> **O aluno criará o `AGENTS.md` na raiz do repositório ao iniciar o projeto, com orientação do instrutor e apoio na definição da arquitetura de software. Escrever esse documento será parte do exercício. Este plano não fornece um modelo nem estabelece regras prontas para ele.**
>
> **Ideias para discutir:** objetivo educacional, nível atual, responsabilidades da IA, forma de pedir ajuda, organização do código, documentos de referência e critérios de revisão. O aluno redigirá as instruções a partir dessas decisões.
