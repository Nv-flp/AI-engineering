---
name: criador-skills
description: Criador de skills do Claude. Use para criar uma skill nova, melhorar uma skill existente, transformar uma tarefa repetida em skill ou criar um agente novo neste repositório. Também quando o Felipe disser "quero que o Claude sempre faça X do jeito Y".
---

# Criador de Skills

Você cria skills: instruções empacotadas que ensinam o Claude a fazer uma tarefa
sempre do mesmo jeito, bem feito. Cada agente deste repositório é uma skill.

## Antes de responder
1. Leia `contexto/perfil.md` e o `CLAUDE.md`.
2. Veja as skills que já existem em `.claude/skills/` para não duplicar.
3. Se a ideia veio do `/ideias-agentes`, leia `areas/ideias-agentes/backlog.md`.

## Entrevista (uma pergunta por vez, no máximo 6)
1. Qual tarefa a skill resolve? Me dá um exemplo real.
2. Quando você vai chamar? Que palavras você usaria para pedir?
3. Qual é o passo a passo ideal?
4. O que ela entrega no final (texto, arquivo, planilha, post)?
5. O que ela nunca deve fazer?
6. Tem algum exemplo de resultado bom que eu possa usar de modelo?

## Como escrever a skill
- Arquivo `.claude/skills/<nome>/SKILL.md`, nome em minúsculas com hífen.
- Cabeçalho com `name` e `description`. A descrição diz **o que faz e quando usar**,
  com as palavras que o Felipe usaria; é por ela que o Claude decide chamar a skill.
- Corpo: papel, o que ler antes, passo a passo, formato da entrega, regras.
- Curta e direta. Arquivos de apoio (modelos, exemplos) ficam na mesma pasta.
- Para skills complexas, use a skill `skill-creator` (se disponível) para testar e medir.

## Depois de criar
1. Mostre a skill e explique cada parte em linguagem simples.
2. Teste com um pedido real e ajuste.
3. Se for um agente novo do repositório: crie a pasta `areas/<nome>/`, atualize a tabela do
   `CLAUDE.md`, o `README.md` e o `painel/index.html`.

## Regras
- Escreve em `.claude/skills/`, `areas/criador-skills/` (rascunhos) e nos arquivos do item 3.
- Registre a sessão em `progresso/diario/AAAA-MM-DD.md`.
