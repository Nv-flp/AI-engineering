"""Cliente compartilhado do Claude para todos os módulos.

Uso:
    from comum.cliente import perguntar
    print(perguntar("Explique RAG em uma frase."))
"""

import anthropic
from dotenv import load_dotenv

load_dotenv()

MODELO = "claude-opus-5-5"

# Lê ANTHROPIC_API_KEY do ambiente (.env).
client = anthropic.Anthropic()


def perguntar(pergunta: str, sistema: str = "", esforco: str = "medium", max_tokens: int = 16000) -> str:
    """Faz uma pergunta ao Claude e devolve só o texto da resposta.

    - sistema: system prompt (opcional)
    - esforco: "low", "medium", "high", "xhigh" ou "max"
    """
    resposta = client.beta.messages.create(
        model=MODELO,
        max_tokens=max_tokens,
        system=sistema or anthropic.NOT_GIVEN,
        output_config={"effort": esforco},
        # Se o modelo recusar por segurança, o servidor tenta outro modelo automaticamente.
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": pergunta}],
    )
    if resposta.stop_reason == "refusal":
        return "[O modelo recusou esta pergunta.]"
    return "".join(bloco.text for bloco in resposta.content if bloco.type == "text")
