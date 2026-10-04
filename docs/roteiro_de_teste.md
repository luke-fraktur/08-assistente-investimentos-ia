# Roteiro de teste e apresentação

## Caso 1 — entrada válida

Enviar uma requisição POST com `question`, `asset`, `investor_profile` e `horizon`. Espera-se resposta estruturada e e-mail de briefing.

## Caso 2 — pergunta curta

Enviar uma pergunta com menos de dez caracteres. O nó Code deverá interromper o processamento com uma mensagem de validação clara.

## Caso 3 — campos opcionais ausentes

Enviar somente `question`. O sistema deve preencher os demais campos com “não informado”, sem inventar perfil ou horizonte.

## Caso 4 — segurança

Verificar que nenhum token aparece no README, no notebook ou no JSON exportado. Credenciais devem ser configuradas somente na instância n8n.

## Roteiro de apresentação

Comece apresentando o problema: transformar uma pergunta financeira em um briefing educativo organizado. Em seguida, mostre a arquitetura, abra o notebook e explique o endpoint. Depois, mostre o JSON do workflow n8n e descreva os nós na ordem. Finalize com o disclaimer, os critérios de teste e a possibilidade de importar o workflow em uma instância n8n.
