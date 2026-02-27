from django.db import models
from ..models import BaseModel


class Categoria(BaseModel):
    nome = models.CharField(max_length=20)
    area = models.CharField(max_length=20, null=True, blank=True)
    instituicao = models.CharField(max_length=10,default='ifrs')

    def __str__(self):
        return f'{self.id}: {self.nome} ({self.area}/{self.instituicao})'
