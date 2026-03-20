from datetime import datetime
from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from ..enumerations import Dificuldade, Idioma, LimiteTempo, LimiteMemoria, Nota


class Problema(BaseModel):

    cod = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(4)],
        help_text="Código",
    )
    titulo = models.CharField(
        max_length=200,
        unique=True,
        validators=[MinLengthValidator(5)],
        help_text="Título",
    )
    enunciado = models.TextField(
        max_length=5000,
        unique=True,
        validators=[MinLengthValidator(10)],
        help_text="Enunciado",
    )
    enunciado_entrada = models.TextField(
        max_length=2000,
        unique=True,
        validators=[MinLengthValidator(10)],
        help_text="Enunciado de entrada",
    )
    enunciado_saida = models.TextField(
        max_length=2000,
        unique=True,
        validators=[MinLengthValidator(10)],
        help_text="Enunciado de Saída",
    )
    dificuldade = models.CharField(choices=Dificuldade)
    idioma = models.CharField(choices=Idioma)
    fonte = models.CharField(
        max_length=150, validators=[MinLengthValidator(3)], help_text="Fonte"
    )
    limite_tempo=models.CharField(choices=LimiteTempo)
    limite_memoria=models.CharField(choices=LimiteMemoria)
    publico = models.BooleanField(default=True)
    nota = models.CharField(choices=Nota)
    criado = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        default=datetime.now,
        help_text="Data de criação",
    )
    atualizacao = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        default=datetime.now,
        help_text="Data de Atualização",
    )

    def __str__(self):
        return (f'Código: {self.cod}')