# AI Engineering

Meus agentes de IA personalizados com o Claude. Cada agente roda numa sessão separada do Claude Code.

Painel visual: [`painel/index.html`](painel/index.html)

## Agentes

_Nenhum agente criado ainda._

## Estrutura

```
.claude/skills/   um agente por pasta (SKILL.md)
comum/            cliente do Claude compartilhado
progresso/diario/ registro de cada sessão
painel/           painel visual (HTML)
```

## Começar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # coloque sua ANTHROPIC_API_KEY
```
