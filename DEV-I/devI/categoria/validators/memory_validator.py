from django.core.exceptions import ValidationError
from pyexpat.errors import messages


def validar_tamanho_memoria(valor_campo):
    tamanhos_validos = [8,16,32,64,128,256]
    try:
        if int(valor_campo) not in tamanhos_validos:
            raise ValidationError(message='Valor invalido para o tamanho da memoria. O valor deve ser: 8, 16, 32, 64, 128 ou 256 MB',
                                  params={'value': valor_campo},)
    except ValueError:
        raise ValidationError(message='Valor deve ser inteiro',
                                params={'value': valor_campo},)
