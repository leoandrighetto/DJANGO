from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from ..enumerations import StatusSubmission


class Submissao(BaseModel):
    linguagem = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)],
        help_text="Linguagem do Código",
    )
    codigo_fonte = models.CharField(
        max_length=1000, validators=[MinLengthValidator(1)], help_text="Código Fonte"
    )
    status = models.CharField(
        choices=StatusSubmission, help_text="Status Atual"
    )

    def __str__(self):
        return f"Linguagem: {self.linguagem} Código Fonte: {self.codigo_fonte} Status {self.status}"
