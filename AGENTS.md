# Orientações para agentes — Estoque Fácil

## Objetivo

Este é um projeto educacional em Python 3 para controlar o estoque de uma loja fictícia. O aprendizado começa no terminal e evolui gradualmente para uma interface gráfica local. Priorize a compreensão do aluno e soluções que ele consiga explicar e modificar.

## Como colaborar

- Responda em português, com explicações claras e exemplos pequenos.
- Em atividades de aprendizado, ajude a descrever a solução, ofereça pistas e revise a tentativa do aluno. Quando houver um pedido explícito de implementação, execute o escopo solicitado e explique as mudanças.
- Não antecipe etapas nem acrescente funcionalidades, dependências ou abstrações sem necessidade concreta.
- Preserve o trabalho existente. Informe o que mudou, como foi verificado e quais dúvidas permanecem.

## Escopo e progressão

- Cada produto começa com nome e quantidade.
- Primeira entrega: cadastrar vários produtos, listar todos e encerrar pelo menu, mantendo os dados em memória.
- Depois: buscar por nome, registrar entradas e saídas, validar dados e identificar estoque baixo. Uma saída não pode exceder a quantidade disponível.
- Evolução prevista: terminal e memória → regras e funções com pytest → JSON → SQLite → Tkinter com ttk.
- Critérios ainda não definidos, como duplicidade de nomes e limite de estoque baixo, devem ser explicitados antes de implementar a regra correspondente.

## Organização do código

- Comece em `main.py`. Crie módulos conforme surgir uma necessidade real.
- Separe progressivamente interface, regras de estoque e persistência, para reutilizar as regras na interface gráfica.
- Introduza classes apenas quando ajudarem a resolver uma necessidade concreta.
- Use `json`, `sqlite3` e Tkinter nas etapas previstas; use `venv` e `pip` quando houver configuração de ambiente e dependências.
- Não invente comandos de execução ou testes: confirme os arquivos e ferramentas presentes no projeto.

## Verificação e revisão

- Verifique o comportamento da etapa em desenvolvimento, incluindo entradas válidas e inválidas.
- Ao introduzir funções de domínio, use pytest para verificar regras, especialmente movimentações e prevenção de saldo negativo.
- Na primeira entrega, confira cadastro de vários produtos, listagem e encerramento do menu. Persistência ainda não é requisito.
- Mantenha alterações pequenas e explique seu propósito. Não faça commit ou publicação sem solicitação.

## Documentação e versionamento

- Este `AGENTS.md` deve ser versionado e conter as orientações essenciais mesmo quando `docs/` não estiver disponível.
- A base de planejamento é `plano-estoque-facil.md`. Consulte-a quando disponível; não presuma que esteja presente em todo clone.
- `docs/` contém documentação local e não deve ser versionado. Não force sua inclusão no Git.
- Documentos locais previstos: `docs/PLANO.md`, `docs/METODOLOGIA.md` e `docs/ENCONTROS.md`.
- Quando existir, mantenha o `README.md` coerente com funcionalidades efetivamente disponíveis e instruções reais de execução.
- Atualize estas orientações junto com o aluno conforme o aprendizado e as decisões do projeto evoluírem.
