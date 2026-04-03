from django.core.validators import MinLengthValidator
from django.db import models

from wrapper.models import BaseModel


class Esporte(BaseModel):
    nome = models.CharField(max_length=20,
                            validators=[MinLengthValidator(4)],
                            help_text="Nome para o esporte")

    def __str__(self):
        return f"{self.nome}"