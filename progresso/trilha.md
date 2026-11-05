# Trilha de AI Engineering

Marque `[x]` ao concluir. O agente **Mentor-IA** (`/mentor`) acompanha esta lista.

## 0. Fundamentos
- [ ] Configurar ambiente Python (.venv, requirements, .env)
- [ ] Primeira chamada à API do Claude (`comum/cliente.py`)
- [ ] Entender tokens, contexto, custo e latência

## 1. Prompts — agente Engenheiro-de-Prompts
- [ ] Anatomia de um bom prompt (papel, contexto, tarefa, formato)
- [ ] System prompt vs. mensagem do usuário
- [ ] Exemplos (few-shot) e uso de tags XML
- [ ] Saídas estruturadas (JSON validado)
- [ ] Prompt caching para reduzir custo

## 2. RAG — agente Arquiteto-RAG
- [ ] O que é RAG e quando usar
- [ ] Dividir documentos em pedaços (chunking)
- [ ] Embeddings e similaridade de cosseno
- [ ] Busca + resposta com citações
- [ ] Medir a qualidade da busca

## 3. Agentes — agente Construtor-de-Agentes
- [ ] Tool use: o Claude chamando funções
- [ ] Loop de agente (tool runner)
- [ ] Ferramentas do servidor (web search, code execution)
- [ ] MCP: conectar ferramentas externas
- [ ] Quando NÃO usar agente

## 4. Avaliação — agente Avaliador-Evals
- [ ] Por que avaliar (vibe check não basta)
- [ ] Montar um conjunto de testes
- [ ] Notas automáticas: código e LLM-como-juiz
- [ ] Comparar duas versões de prompt

## 5. Projetos — agente Laboratório
- [ ] Projeto 1: chatbot com memória
- [ ] Projeto 2: perguntas e respostas sobre meus PDFs (RAG)
- [ ] Projeto 3: agente que pesquisa e escreve relatório
- [ ] Publicar um projeto no portfólio
