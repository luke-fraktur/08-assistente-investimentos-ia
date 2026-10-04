# Assistente Educacional de Investimentos com IA

> MVP técnico de **Lucas Oliveira Soares de Freitas** para a Agência Escala Pro.

## Visão geral

MVP educacional que recebe um perfil de investidor, organiza respostas orientativas e expõe uma API Flask para integração com um workflow n8n. A solução foi desenhada para demonstração e aprendizagem, sem recomendar operações financeiras personalizadas.

- **Aluno:** Lucas Oliveira Soares de Freitas
- **Data:** 04/09/2026
- **Tecnologias:** Python, Flask, Google Colab e n8n

## Componentes

- `src/assistente_investimentos.py` — lógica principal do assistente.
- `notebooks/assistente_investimentos_colab.ipynb` — notebook para executar e demonstrar a API no Google Colab.
- `n8n/workflow_assistente_investimentos.json` — workflow importável no n8n.
- `docs/` — arquitetura, roteiro de testes e roteiro de apresentação.
- `.env.example` — referência de configuração sem segredos.

## Execução rápida

```bash
python -m venv .venv
source .venv/bin/activate
pip install flask flask-cors
python src/assistente_investimentos.py
```

Depois, importe `n8n/workflow_assistente_investimentos.json` no n8n e ajuste apenas a URL do endpoint conforme o ambiente.

## Limites e segurança

O projeto tem finalidade exclusivamente educacional. Não contém tokens reais, não executa ordens e não deve ser usado como recomendação de investimento.
