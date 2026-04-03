from django.core.exceptions import ValidationError

# Validadores de função não devem receber parâmetros adicionais
def validar_tamanho_memoria(valor_campo):
    tamanhos_validos = [8,16,32,64,128,256]
    try:
        if int(valor_campo) not in tamanhos_validos:
            raise ValidationError(
                message="Valor inválido para o tamanho "
                        "da memória. O valor deve ser "
                        "8, 16, 32, 64, 128 ou 256.",
                params={
                    "value": valor_campo
                },
            )
    except ValueError:
        raise ValidationError(
            message="O valor deve ser um número inteiro.",
            params ={
                "value": valor_campo
            },
        )