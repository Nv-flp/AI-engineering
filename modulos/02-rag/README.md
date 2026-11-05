# 02 · RAG (Retrieval-Augmented Generation)

Agente responsável: **Arquiteto-RAG** (`/rag`).

Fazer o Claude responder com base nos **seus** documentos:

```
documentos → pedaços (chunks) → embeddings → busca dos mais parecidos → Claude responde citando os trechos
```

Documentos de exemplo ficam em `dados/`.
