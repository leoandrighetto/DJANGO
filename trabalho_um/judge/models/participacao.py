from django.db import models
from .base_model import BaseModel
from django.core.validators import MinValueValidator
from .perfil import Perfil
from .competicao import Competicao


class Participacao(BaseModel):
    registro = models.DateTimeField(
        auto_now=False, auto_now_add=False, help_text="Registro"
    )
    oficial = models.BooleanField(default=True, help_text="Oficial")
    total_pontos = models.IntegerField(
        validators=[MinValueValidator(0)], help_text="Total de Pontos"
    )

    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    competicao = models.ForeignKey(Competicao,on_delete=models.CASCADE)

    def __str__(self):
        return f"Registro: {self.registro} Oficial: {self.oficial} Total de Pontos: {self.total_pontos}"
