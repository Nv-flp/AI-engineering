"""Primeiro agente: o Claude decide quando usar uma ferramenta (calculadora de custo da API)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from anthropic import beta_tool  # noqa: E402

from comum.cliente import MODELO, client  # noqa: E402

PRECO_POR_MILHAO = {"entrada": 4.00, "saida": 20.00}  # US$, claude-opus-5-5


@beta_tool
def calcular_custo(tokens_entrada: int, tokens_saida: int) -> str:
    """Calcula o custo em dólares de uma chamada ao claude-opus-5-5.

    Args:
        tokens_entrada: quantidade de tokens enviados ao modelo.
        tokens_saida: quantidade de tokens gerados pelo modelo.
    """
    custo = (tokens_entrada * PRECO_POR_MILHAO["entrada"] + tokens_saida * PRECO_POR_MILHAO["saida"]) / 1_000_000
    return f"US$ {custo:.4f}"


runner = client.beta.messages.tool_runner(
    model=MODELO,
    max_tokens=16000,
    tools=[calcular_custo],
    messages=[{
        "role": "user",
        "content": "Quanto custam 1.000 chamadas com 2.000 tokens de entrada e 500 de saída cada?",
    }],
)

for mensagem in runner:
    for bloco in mensagem.content:
        if bloco.type == "tool_use":
            print(f"[ferramenta] {bloco.name}({bloco.input})")
        elif bloco.type == "text":
            print(bloco.text)
