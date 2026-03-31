from django.db import models
from relacionamento.models import BaseModel
from django.core.validators import MinLengthValidator


class Esporte(BaseModel):
    name = models.CharField(
        max_length=20, validators=[MinLengthValidator(4)], help_text="Nome para o esporte"
    )

    def __str__(self):
        return f"{self.name}"
