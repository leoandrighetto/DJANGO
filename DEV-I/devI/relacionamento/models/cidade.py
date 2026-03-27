from django.db import models
from relacionamento.models import BaseModel

from django.core.validators import MinLengthValidator


class Cidade(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text="Nome para a cidade",
    )
    estado = models.CharField(
        max_length=2, validators=[MinLengthValidator(2)], help_text="Sigla para o estado"
    )

    def __str__(self):
        return "Nome: {self.nome}"
