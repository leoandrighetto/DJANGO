from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from .teste import Teste


class Caso(Teste):
    peso = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        default=20,
        help_text="Peso",
    )

    def __str__(self):
        return f"Peso: {self.peso}"
