# Roteiro de fala para a apresentação

Este projeto é um MVP de Assistente de Investimentos Educacional com IA. Ele recebe uma pergunta, organiza o contexto do usuário, prepara uma análise estruturada e entrega o resultado por e-mail. O foco não é recomendar ativos, mas demonstrar uma integração segura entre entrada por webhook, processamento, automação e comunicação.

A solução foi separada para que o Google Colab funcione como ambiente de demonstração do processamento e o n8n como orquestrador. Assim, o workflow pode ser importado posteriormente sem que o repositório dependa de uma instância n8n ativa durante a avaliação.

A principal decisão de segurança foi não armazenar segredos no GitHub. O JSON do workflow contém apenas referências de configuração, e as credenciais devem ser adicionadas diretamente no n8n.
