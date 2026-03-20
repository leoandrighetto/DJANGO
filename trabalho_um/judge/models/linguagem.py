from .base_model import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator


class Linguagem(BaseModel):

    name = models.CharField(
        max_length=50, validators=[MinLengthValidator(3)], help_text="Nome da linguagem"
    )
    slug = models.SlugField(
        max_length=50, validators=[MinLengthValidator(3)], help_text="Slug da Linguagem"
    )
    compilador = models.CharField(
        max_length=80, validators=[MinLengthValidator(5)], help_text="Compilador"
    )
    versao = models.CharField(
        max_length=50, validators=[MinLengthValidator(3)], help_text="Versão"
    )
    multiplicador_tempo = models.FloatField(
        validators=[MinValueValidator(1.0)], help_text="Multiplicador do tempo"
    )
    multiplicador_memoria = models.FloatField(
        validators=[MinValueValidator(1.0)], help_text="Multiplicador da Memória"
    )
    ativo = models.BooleanField(default=True, help_text="Ativo")

    def __str__(self):
        return f"Nome: {self.name} Slug: {self.slug} Compilador: {self.compilador} Versão: {self.versao} Multiplicador de Tempo: {self.multiplicador_tempo} Multiplicador de Memória: {self.multiplicador_memoria} Ativo: {self.ativo}"
