# AI Engineering — instruções para o Claude

Repositório de agentes de IA personalizados do Felipe (Nv-flp).
Tudo em **português do Brasil**, com linguagem simples e direta.

## Como o repositório funciona

Cada agente é uma skill em `.claude/skills/<nome>/SKILL.md`, chamada com `/<nome>`,
e roda numa **sessão separada** do Claude Code. A pasta de trabalho de cada um é `areas/<nome>/`.
Todos leem `contexto/perfil.md` antes de começar.

## Agentes

| Agente | Comando | Pasta | Faz o quê |
|---|---|---|---|
| Mentor de IA | `/mentor` | `areas/mentor/` | Trilha de estudos, plano da semana, dúvidas de conceito, qual agente usar |
| Engenheiro de IA | `/engenheiro` | `areas/engenheiro/` | Constrói com código: chatbots, agentes, scripts, integrações |
| Especialista em Conectores | `/conectores` | `areas/conectores/` | Conectores, plugins, MCP e integrações do Claude |
| Criador de Skills | `/criador-skills` | `areas/criador-skills/` | Cria e melhora skills e novos agentes |
| Radar de IA | `/radar-ia` | `areas/radar-ia/` | Novidades do mercado de IA e o que muda para você |
| Designer Profissional | `/designer` | `areas/designer/` | Posts, criativos, sites, landing pages, marca e apresentações |
| Especialista em Dinheiro | `/dinheiro` | `areas/dinheiro/` | Dinheiro rápido com pouco tempo: ofertas, planos de 7 dias |
| Automatizador da Operação | `/automacao` | `areas/automacao/` | Automatiza tarefas repetitivas do negócio |
| Criador de Ideias de Agentes | `/ideias-agentes` | `areas/ideias-agentes/` | Ideias de novos agentes, avaliadas por impacto e esforço |

## Regras para todos os agentes

1. Cada agente trabalha só na própria pasta e em `progresso/diario/`.
2. Ao fim de cada sessão, registre o que foi feito em `progresso/diario/AAAA-MM-DD.md`.
3. Código em Python usa o SDK oficial `anthropic` e o helper `comum/cliente.py`.
4. Nunca faça commit de chaves: elas ficam em `.env`, que o git ignora.
5. Ao criar ou mudar um agente, atualize a tabela acima, o `README.md` e o `painel/index.html`.
