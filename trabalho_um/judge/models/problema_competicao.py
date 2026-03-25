from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from .problema import Problema
from .competicao import Competicao


class ProblemaCompeticao(BaseModel):
    label = models.CharField(
        max_length=5, validators=[MinLengthValidator(1)], help_text="Label do Problema"
    )
    pontos = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=100
    )
    ordem = models.IntegerField(validators=[MinValueValidator(1)])

    problema = models.ForeignKey(Problema, null=True,blank=True, on_delete=models.CASCADE)

    competicao = models.ForeignKey(Competicao, null=True,blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return f"Label: {self.label} Pontos: {self.pontos} Ordem: {self.ordem}"
