from datetime import datetime
from django.core.exceptions import ValidationError

def data_minima(value):

    hoje = datetime.today()
    data_minima = hoje.year - 10
    print(f"\n\n\n{data_minima}")

    if value.year > data_minima:
        raise ValidationError(f"A idade mínima é de 10 anos.")

    