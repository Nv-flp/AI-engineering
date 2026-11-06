# AI Engineering

Meus agentes de IA personalizados com o Claude. Cada agente roda numa sessão separada do Claude Code.

Painel visual: [`painel/index.html`](painel/index.html)

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

## Estrutura

```
.claude/skills/   os 9 agentes (um SKILL.md cada)
areas/            pasta de trabalho de cada agente
contexto/         perfil do Felipe e do negócio (todos leem)
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
