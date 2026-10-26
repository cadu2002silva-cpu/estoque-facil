# Plano — Estoque Fácil

Base: `plano-estoque-facil.md`. Documento local, não versionado.

## Objetivo

Construir um controle de estoque de uma loja fictícia, revisando Python básico e introduzindo organização de código, persistência, testes e colaboração. O ritmo depende da compreensão do aluno; cada etapa pode ocupar mais de um encontro.

## 1. Terminal e memória

**Conceitos:** variáveis, conversões, condicionais, loops, listas e dicionários.

Começar em `main.py`, com produtos contendo nome e quantidade. Criar um menu para cadastrar vários produtos, listar todos e encerrar. Os dados existem somente durante a execução.

**Critérios de conclusão:** cadastrar mais de um produto, conferir nomes e quantidades na listagem, retornar ao menu e encerrar. O aluno explica a estrutura de dados e o fluxo do programa.

## 2. Regras e funções

**Conceitos:** funções, parâmetros, retornos, validações, tratamento de erros e testes com pytest.

Adicionar busca por nome, entradas, saídas e identificação de estoque baixo. Uma saída deve respeitar a quantidade disponível. Discutir nomes duplicados, campos vazios, valores inválidos, quantidades negativas e limite de estoque baixo antes de consolidar essas regras.

**Critérios de conclusão:** movimentações atualizam o produto correto; saída acima do saldo é rejeitada sem alterar o estoque; entradas inválidas são tratadas; as regras acordadas possuem testes. O aluno consegue explicar e adaptar as funções.

## 3. JSON

**Conceitos:** arquivos, módulo `json` e organização em módulos.

Salvar e recuperar os produtos em arquivo. Definir o comportamento para arquivo inexistente ou inválido, evitando sobrescrever dados silenciosamente em caso de erro.

**Critérios de conclusão:** dados salvos são recuperados após reiniciar; erros previstos são tratados; regras de estoque continuam funcionando.

## 4. SQLite

**Conceitos:** banco local, SQL, conexões e transações com `sqlite3`.

Transferir o armazenamento principal para SQLite. Definir a estrutura das tabelas e discutir se os dados JSON existentes precisam ser importados.

**Critérios de conclusão:** cadastro, consultas e movimentações usam o banco; dados permanecem após reiniciar; regras anteriores continuam válidas.

## 5. Tkinter

**Conceitos:** janela, campos, botões, tabela e eventos com Tkinter e `ttk`.

Construir uma interface local reaproveitando as regras e a persistência já existentes.

**Critérios de conclusão:** operações de estoque funcionam pela interface; a tabela reflete alterações; erros são apresentados de forma compreensível; as regras não ficam duplicadas nos eventos da janela.

## Preparação e decisões pendentes

- Pasta e repositório previstos: `estoque-facil`, no GitHub do aluno, com participação do instrutor.
- Ferramentas: Python 3, VS Code, extensão Python e Live Share; Git desde o início.
- Usar `venv` e `pip` para ambiente e dependências; registrar comandos quando a configuração real existir.
- Introduzir branches, Pull Requests e classes gradualmente.
- Confirmar a etapa atual e registrar as decisões de negócio no encontro correspondente.

Este plano descreve o trabalho previsto; não comprova funcionalidades implementadas.
