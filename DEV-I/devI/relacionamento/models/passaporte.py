import datetime
from datetime import date
from .base_model import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
from .pessoa import Pessoa

class Passaporte(BaseModel):
    numero = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(4)],verbose_name="Número do Passaporte", help_text="Número do passaporte da pessoa")

    emissao = models.DateField(verbose_name="Data de Emissão", help_text="Data de emissão do passaporte", validators=[MinValueValidator(date.today)])

    vencimento = models.DateField(verbose_name="Data de Vencimento", help_text="Data de vencimento do passaporte")

    # realize a associação entre as classes (bidirecionail) 1:1
    pessoa = models.OneToOneField(Pessoa, help_text="Selecione o titular do passaporte", on_delete=models.PROTECT)


    def clean(self):
        
        if self.emissao > self.vencimento:
            raise ValidationError({"emissao": "A data de emissão não pode ser posterior a data de vencimento.",
                                   "vencimento": "A data de vencimento não pode ser anterior a data de emissão."})
        
        if self.pessoa.data_nascimento > self.emissao:
            raise ValidationError({"emissao":"data de emissao não pode ser posterior ao nascimento do titular"})

    def __str__(self):
        return f"{self.numero}"