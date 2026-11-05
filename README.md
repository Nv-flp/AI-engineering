# AI Engineering

Meus estudos e projetos de **engenharia de IA** com o Claude, organizados em **6 agentes**.
Cada agente roda numa sessão separada do Claude Code e cuida de uma área.

| Agente | Comando | Pasta | Faz o quê |
|---|---|---|---|
| Mentor-IA | `/mentor` | `progresso/` | Trilha, plano da semana, diário |
| Engenheiro-de-Prompts | `/prompts` | `modulos/01-prompts/` | Técnicas de prompt |
| Arquiteto-RAG | `/rag` | `modulos/02-rag/` | IA respondendo com base nos meus documentos |
| Construtor-de-Agentes | `/agentes` | `modulos/03-agentes/` | Tool use, loops, MCP |
| Avaliador-Evals | `/evals` | `modulos/04-evals/` | Medir qualidade |
| Laboratório | `/laboratorio` | `projetos/` | Projetos completos para o portfólio |

O painel visual com tudo está em [`painel/index.html`](painel/index.html).

## Estrutura

```
.claude/skills/   os 6 agentes (um SKILL.md cada)
comum/            cliente do Claude compartilhado
modulos/          01-prompts · 02-rag · 03-agentes · 04-evals
projetos/         projetos práticos
progresso/        trilha.md + diário de estudos
painel/           painel visual (HTML)
```

## Começar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # coloque sua ANTHROPIC_API_KEY
python modulos/01-prompts/exemplo.py
```

No Claude Code, abra uma sessão com este repositório e digite o comando do agente (ex.: `/mentor`).
