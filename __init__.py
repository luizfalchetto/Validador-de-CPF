import logging
import azure.functions as func
import re

def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processando solicitação de validação de CPF.')

    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
            cpf = req_body.get('cpf')
        except ValueError:
            return func.HttpResponse(
                "Por favor, forneça um CPF.",
                status_code=400
            )

    if not cpf:
        return func.HttpResponse(
            "CPF não fornecido.",
            status_code=400
        )

    if validar_cpf(cpf):
        return func.HttpResponse(f"CPF {cpf} é válido.", status_code=200)
    else:
        return func.HttpResponse(f"CPF {cpf} é inválido.", status_code=400)
