from datetime import datetime
from django.db import models
from .base_model import BaseModel
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator


class Competicao(BaseModel):

    nome = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
        help_text="Nome da competição",
    )
    slug = models.SlugField(
        max_length=50,
        validators=[MinLengthValidator(3)],
        unique=True,
        help_text="Slug da Competição",
    )
    descricao = models.TextField(
        validators=[MinLengthValidator(5), MaxLengthValidator(1000)],
        help_text="Descrição da Competição",
    )
    url = models.URLField(
        max_length=500, null=True, blank=True, help_text="URL da competição"
    )
    inicio = models.DateTimeField(
        auto_now=False, auto_now_add=False, help_text="Data de início"
    )
    termino = models.DateTimeField(
        auto_now=False, auto_now_add=False, help_text="Data de Término"
    )
    freeze = models.DateTimeField(
        auto_now=False, auto_now_add=False, help_text="Data do Freeze"
    )
    publico = models.BooleanField(default=True)
    criado = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        default=datetime.now,
        help_text="Data de início",
    )
    atualizado=models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        default=datetime.now,
        help_text="Data de atualização",
    )
    penalidade=models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return (f"Nome {self.nome}")
