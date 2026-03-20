from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class ProblemaCompeticao(BaseModel):
    label = models.CharField(
        max_length=5, validators=[MinLengthValidator(1)], help_text="Label do Problema"
    )
    pontos = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=100
    )
    ordem = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"Label: {self.label} Pontos: {self.pontos} Ordem: {self.ordem}"
