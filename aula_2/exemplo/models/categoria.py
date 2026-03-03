from django.db import models
from ..models import BaseModel


class Categoria(BaseModel):
    nome = models.CharField(max_length=20)
    area = models.CharField(max_length=20, null=True, blank=True, verbose_name="Área do conhecimento",
                            help_text="Informe a área do conhecimento segundo o padrão CAPES")
    instituicao = models.CharField(max_length=10, default='ifrs',verbose_name="Instituição",help_text="Máximo de 10 caracteres")

    def __str__(self):
        return f'{self.id}: {self.nome} ({self.area}/{self.instituicao})'
