"""Primeiro exemplo: o mesmo pedido com um prompt vago e com um prompt bem estruturado."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from comum.cliente import perguntar  # noqa: E402

prompt_vago = "Fala sobre IA."

prompt_bom = """<papel>Você é um professor de tecnologia para iniciantes.</papel>
<tarefa>Explique o que é um modelo de linguagem (LLM).</tarefa>
<formato>
- No máximo 5 frases.
- Uma analogia do dia a dia.
- Termine com um exemplo de uso prático.
</formato>"""

for titulo, prompt in [("PROMPT VAGO", prompt_vago), ("PROMPT ESTRUTURADO", prompt_bom)]:
    print(f"\n===== {titulo} =====")
    print(perguntar(prompt, esforco="low"))
