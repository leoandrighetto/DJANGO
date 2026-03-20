from .base_model import BaseModel
from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Exemplo(BaseModel):
    ordem = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], unique=True, help_text="Ordem")

    def __str__(self):
        return (f"Ordem: {self.ordem}")
    