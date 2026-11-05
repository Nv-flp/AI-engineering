# AI Engineering — instruções para o Claude

Repositório de estudos e projetos de **AI Engineering** do Felipe (Nv-flp).
Tudo em **português do Brasil**, com linguagem simples e direta.

## Como o repositório funciona

Cada área tem um **agente** próprio, que roda numa **sessão separada** do Claude Code.
O agente é uma skill em `.claude/skills/<nome>/SKILL.md`, chamada com `/<nome>`.

| Agente | Skill | Pasta de trabalho | Papel |
|---|---|---|---|
| Mentor-IA | `/mentor` | `progresso/` | Trilha, plano da semana, diário, próximos passos |
| Engenheiro-de-Prompts | `/prompts` | `modulos/01-prompts/` | Técnicas de prompt e system prompts |
| Arquiteto-RAG | `/rag` | `modulos/02-rag/` | Embeddings, busca, RAG |
| Construtor-de-Agentes | `/agentes` | `modulos/03-agentes/` | Tool use, loops de agente, MCP |
| Avaliador-Evals | `/evals` | `modulos/04-evals/` | Avaliações, métricas, testes de qualidade |
| Laboratório | `/laboratorio` | `projetos/` | Projetos práticos completos para o portfólio |

## Regras para todos os agentes

1. **Fique na sua pasta.** Cada agente escreve só na própria pasta de trabalho
   e em `progresso/diario/`. Para mexer em outra área, sugira usar o agente dela.
2. **Registre o que foi feito.** Ao fim de cada sessão, acrescente uma entrada em
   `progresso/diario/AAAA-MM-DD.md` com: agente, o que foi estudado/feito, próximo passo.
3. **Atualize a trilha.** Ao concluir um item, marque `[x]` em `progresso/trilha.md`.
4. **Código executável.** Exemplos em Python, usando o SDK oficial `anthropic`
   e o helper `comum/cliente.py`. Modelo padrão: `claude-opus-5-5`.
5. **Explique antes de codar.** O Felipe está aprendendo: explique o conceito em
   poucas linhas, depois mostre o código, depois proponha um exercício.
6. **Nunca faça commit de chaves.** A chave fica em `.env` (ignorado pelo git).
7. **Painel.** Se criar um módulo, projeto ou agente novo, atualize `painel/index.html`.

## Comandos úteis

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # e preencha ANTHROPIC_API_KEY
python modulos/01-prompts/exemplo.py
```
