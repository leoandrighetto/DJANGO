from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .base_model import BaseModel


class Revista(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5)],
        verbose_name="Nome da Revista",
    )
    edicao = models.IntegerField(
        verbose_name="Edição da Revista",
        help_text="Número da edição da revista",
        validators=[MinValueValidator(1)],
    )

    class Meta:
        unique_together = ("nome", "edicao")

    def __str__(self):
        return self.nome
