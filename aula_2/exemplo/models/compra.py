from django.db import models
from ..models import BaseModel
from django.core.validators import MinLengthValidator

class Compra(BaseModel):
    data = models.DateField(auto_now=False, auto_now_add=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    valor = models.DecimalField(max_digits = 7 , decimal_places = 2)
    quantidade = models.IntegerField()
    peso = models.FloatField()
    descricao = models.TextField()
    cliente = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
