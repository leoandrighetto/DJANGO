from datetime import date
from django.db import models
from .base_model import BaseModel
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.core.exceptions import ValidationError
from .revista import Revista


class Reportagem(BaseModel):
    titulo = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3)],
        verbose_name="Título",
        help_text="Título da reportagem",
    )

    data_publicacao = models.DateField(
        verbose_name="Data de Publicação",
        help_text="Data de publicação da reportagem",
        validators=[MinValueValidator(date.today), MaxValueValidator(date.today)],
    )

    # field para relacionamento n:n simples:

    revistas = models.ManyToManyField(
        Revista, help_text="Selecione as revistas relacionadas a reportagem"
    )

    def __str__(self):
        return f"{self.titulo}"

    class Meta:
        verbose_name_plural = 'Reportagens'