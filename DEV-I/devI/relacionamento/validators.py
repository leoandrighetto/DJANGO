import re
from django.core.exceptions import ValidationError


def validacao_cpf(value):
    padrao_cpf = r"^\d{3}\d{3}\d{3}\d{2}$"
    if not re.fullmatch(padrao_cpf, value):
        raise ValidationError(
            "Formato de CPF inválido! O padrão correto é 000.000.000-00 ."
        )