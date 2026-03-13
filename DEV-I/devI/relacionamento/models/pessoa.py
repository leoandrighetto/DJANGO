import datetime
from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from ..validators import validacao_cpf


class Pessoa(BaseModel):

    nome = models.CharField(
        max_length=100,
        help_text="Nome completo da pessoa",
        validators=[MinLengthValidator(5)],
    )
    data_nascimento = models.DateField(
        verbose_name="Idade da pessoa",
        help_text="Selecione a data de nascimento",
        validators=[],
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[validacao_cpf],
        help_text="CPF da pessoa",
        verbose_name="CPF",
    )

    def clean(self):
        hoje = datetime.date.today()
        if self.data_nascimento is not None and self.data_nascimento > hoje:
            raise ValidationError("A data de nascimento não pode ser no futuro.")

    def __str__(self):
        return self.nome
