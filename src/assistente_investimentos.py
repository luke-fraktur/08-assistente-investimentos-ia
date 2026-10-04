"""Lógica de demonstração do Assistente de Investimentos Educacional.

O módulo não recomenda compra ou venda. Ele valida o briefing e produz
uma estrutura educativa que pode ser conectada a um LLM no futuro.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class InvestmentRequest:
    question: str
    asset: str = "não informado"
    investor_profile: str = "não informado"
    horizon: str = "não informado"


def validate_request(payload: dict[str, Any]) -> InvestmentRequest:
    question = str(payload.get("question", "")).strip()
    if len(question) < 10:
        raise ValueError("Informe uma pergunta com pelo menos 10 caracteres.")
    return InvestmentRequest(
        question=question,
        asset=str(payload.get("asset") or "não informado").strip(),
        investor_profile=str(payload.get("investor_profile") or "não informado").strip(),
        horizon=str(payload.get("horizon") or "não informado").strip(),
    )


def build_educational_response(request: InvestmentRequest) -> dict[str, Any]:
    return {
        "type": "educational_investment_briefing",
        "disclaimer": (
            "Material educativo. Não constitui recomendação personalizada, promessa de retorno "
            "ou ordem de compra e venda. Verifique dados e fontes antes de qualquer decisão."
        ),
        "request": asdict(request),
        "analysis_framework": [
            "Definir o que está sendo perguntado e quais dados seriam necessários.",
            "Separar fatos, hipóteses, riscos e informações ausentes.",
            "Explicar conceitos relevantes em linguagem acessível.",
            "Apresentar perguntas de diligência para uma análise posterior.",
        ],
        "next_questions": [
            "Qual é a fonte e a data dos dados utilizados?",
            "Quais riscos podem invalidar a hipótese analisada?",
            "Qual é o horizonte e qual seria a tolerância a perdas?",
        ],
    }


def process_payload(payload: dict[str, Any]) -> dict[str, Any]:
    request = validate_request(payload)
    return build_educational_response(request)


if __name__ == "__main__":
    example = {
        "question": "O que devo observar ao estudar um ETF de renda variável?",
        "asset": "ETF hipotético",
        "investor_profile": "estudante",
        "horizon": "longo prazo",
    }
    import json
    print(json.dumps(process_payload(example), indent=2, ensure_ascii=False))
