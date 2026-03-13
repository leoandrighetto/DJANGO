from datetime import date

from django.core.exceptions import ValidationError
from .base_model import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from .reporter import Reporter
from django.contrib import admin


class Artigo(BaseModel):
    titulo = models.CharField(
        max_length=255,
        help_text="Título do artigo",
        validators=[MinLengthValidator(5)],
        verbose_name="Título",
    )
    data_publicacao = models.DateField(
        verbose_name="Data de Publicação",
        help_text="Data de publicação do artigo",
        validators=[MinValueValidator(date.today)],
    )

    # tipo de field que permite a relação entre as classes (1:N ou N:1) - ForeignKey
    autor = models.ForeignKey(
        Reporter,
        verbose_name="Reporter Autor",
        help_text="Selecione o autor do artigo",
        on_delete=models.PROTECT,
    )

    def clean(self):
        data_publicacao = self.data_publicacao
        data_publicacao.replace(year=data_publicacao.year - 18)

        if data_publicacao < self.autor.data_nascimento:
            raise ValidationError(
                {
                    "publicacao": "Autor não possui idade mínima para publicar o artigo (18 anos)."
                }
            )

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_publicacao", "autor")