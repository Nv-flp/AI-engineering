# AI Engineering — instruções para o Claude

Repositório de agentes de IA personalizados do Felipe (Nv-flp).
Tudo em **português do Brasil**, com linguagem simples e direta.

## Como o repositório funciona

Cada agente é uma skill em `.claude/skills/<nome>/SKILL.md`, chamada com `/<nome>`,
e roda numa **sessão separada** do Claude Code.

## Agentes

_Nenhum agente criado ainda._

## Regras para todos os agentes

1. Cada agente trabalha só na própria pasta e em `progresso/diario/`.
2. Ao fim de cada sessão, registre o que foi feito em `progresso/diario/AAAA-MM-DD.md`.
3. Código em Python usa o SDK oficial `anthropic` e o helper `comum/cliente.py`.
4. Nunca faça commit de chaves: elas ficam em `.env`, que o git ignora.
5. Ao criar ou mudar um agente, atualize a tabela acima, o `README.md` e o `painel/index.html`.
