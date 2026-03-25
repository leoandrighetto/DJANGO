from datetime import date
from django.db import models
from .base_model import BaseModel
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from ..validators.validadores_de_data import data_minima
from ..enumerations import Genero, Idioma
from django.contrib.auth.models import User


class Perfil(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    data_nascimento = models.DateField(
        auto_now=False,
        auto_now_add=False,
        validators=[data_minima],
        help_text="Data de Nascimento",
    )
    pais = models.CharField(
        max_length=100, validators=[MinLengthValidator(3)], help_text="País de origem"
    )
    genero = models.CharField(choices=Genero)
    pagina_pessoal = models.URLField(
        max_length=150,
        validators=[MinLengthValidator(15)],
        null=True,
        blank=True,
        help_text="URL do perfil",
    )
    biografia = models.TextField(null=True, blank=True, help_text="Biografia")
    idioma = models.CharField(choices=Idioma, help_text="Idioma")
    premium = models.BooleanField(default=False, help_text="Perfil Premium")
    membro_desde = models.DateField(
        auto_now=False,
        auto_now_add=False,
        default=date.today,
        help_text="Tempo como membro",
    )
    instituicao = models.CharField(
        max_length=120, validators=[MinLengthValidator(3)], help_text="Instituição"
    )
    posicao_ranking = models.IntegerField(
        validators=[MinValueValidator(1)], help_text="Posição no Ranking"
    )
    resolvidos = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Quantidade de Problemas Resolvidos",
    )
    submetidos = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Quantidade de Problemas Submetidos",
    )
    
    treinador = models.BooleanField(default=False, help_text="Perfil com Treinador")

    def __str__(self):
        return (f"Nome: {self.user}")