# CPF Validator Service

## Descrição
Microsserviço eficiente, escalável e econômico para validação de CPFs, construído com arquitetura serverless no Azure Functions. O serviço garante alta disponibilidade, baixo custo operacional e facilidade de manutenção.

## Funcionalidades
- Valida CPF informado via query string ou JSON.
- Retorna status HTTP 200 para CPFs válidos e 400 para inválidos.
- Serverless, escalável automaticamente conforme demanda.
- Baixo custo: paga apenas pelo tempo de execução da função.

## Endpoints
- `GET /api/validatecpf?cpf=12345678909`
- `POST /api/validatecpf` com JSON `{ "cpf": "12345678909" }`
