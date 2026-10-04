# Arquitetura técnica

O MVP possui três camadas. A primeira é a entrada, representada pelo Webhook n8n. A segunda é o processamento, realizado pelo endpoint preparado no Google Colab, com validação e estruturação do briefing. A terceira é a entrega, em que o n8n formata o resultado e envia a mensagem pelo Gmail.

O workflow está desligado por padrão e não contém segredos. Depois da importação, o avaliador deve substituir a URL de demonstração do nó HTTP, configurar a credencial Gmail e revisar os endereços de remetente e destinatário.

## Contrato de entrada

```json
{
  "question": "O que observar ao estudar um ETF?",
  "asset": "ETF hipotético",
  "investor_profile": "iniciante",
  "horizon": "longo prazo"
}
```

## Contrato de saída

A saída contém o briefing educativo, o aviso de limitação, a pergunta original, o ativo informado, o perfil, o horizonte e perguntas para aprofundamento. O sistema não executa ordens e não produz promessa de retorno.
