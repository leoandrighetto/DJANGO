from datetime import datetime
from .base_model import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from .problema import Problema


class Teste(BaseModel):
    nome = models.CharField(
        max_length=80, validators=[MinLengthValidator(5)], help_text="Nome do Teste"
    )
    dados_entrada = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5000)],
        help_text="Dados de Entrada",
    )
    dados_saida = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5000)],
        help_text="Dados de Saída",
    )
    criado = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=datetime.now
    )

    atualizado = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=datetime.now
    )

    problema = models.ForeignKey(Problema, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nome: {self.nome} Dados de Entrada: {self.dados_entrada} Dados de Saída: {self.dados_saida} Criado: {self.criado} Atualizado: {self.atualizado}"
