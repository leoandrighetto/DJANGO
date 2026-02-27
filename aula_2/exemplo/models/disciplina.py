from django.db import models
from ..models.base_model import BaseModel


class Disciplina(BaseModel):
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=4, null=True, blank=True)
    instituicao = models.CharField(max_length=15, default="IFRS",)

    def __str__(self):
        return f'{self.id}: {self.nome} ({self.sigla}/{self.instituicao})'