from django.core.validators import MinLengthValidator
from django.db import models

from wrapper.models import BaseModel


class Cidade(BaseModel):
    nome = models.CharField(max_length=100,
                            validators=[MinLengthValidator(2)],
                            help_text="Nome para a cidade")
    estado = models.CharField(max_length=2,
                              validators=[MinLengthValidator(2)],
                              help_text="Insira a sigla do estado")

    def __str__(self):
        return f"{self.nome}/{self.estado}"