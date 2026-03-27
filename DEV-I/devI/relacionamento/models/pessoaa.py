from .cidade import Cidade
from django.db import models
from relacionamento.models import BaseModel
from .time import Time
from .esporte import Esporte

from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from .sexo import Sexo


class Pessoaa(BaseModel):
    nome = models.CharField(
        max_length=40, validators=[MinLengthValidator(3)], help_text="Nome da pessoa"
    )
    sexo = models.CharField(
        max_length=1,
        validators=[MinLengthValidator(1)],
        choices=Sexo,
        help_text="Sexo da pessoa",
    )
    idade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    renda = models.DecimalField(
        decimal_places=1,
        max_digits=10,
        validators=[MinValueValidator(0)],
        help_text="Insira a renda da pessoa",
    )

    time_torce = models.ForeignKey(
        Time, on_delete=models.RESTRICT, help_text="Selecione o seu time de torcida"
    )
    esporte_favotiro = models.ForeignKey(
        Esporte,
        on_delete=models.RESTRICT,
        help_text="Selecione o seu esporte de torcida",
    )
    cidade = models.ForeignKey(
        Cidade, on_delete=models.CASCADE, help_text="Seleciona a cidade"
    )
