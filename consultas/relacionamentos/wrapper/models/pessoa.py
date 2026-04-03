from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from wrapper.models import BaseModel
from wrapper.enumerations import Sexo
from wrapper.models import Time, Esporte, Cidade
from aula.managers import PessoaManager


class Pessoa(BaseModel):
    nome = models.CharField(max_length=40,
                            validators=[MinLengthValidator(3)],
                            help_text='Nome da Pessoa')
    sexo = models.CharField(max_length=1,
                            validators=[MinLengthValidator(1)],
                            choices=Sexo,
                            help_text='Selecione o sexo da pessoa')

    idade = models.IntegerField(validators=[MinValueValidator(0),
                                            MaxValueValidator(200)],
                                help_text="Insira a idade da pessoa")

    renda = models.DecimalField(decimal_places=2, max_digits=10,
                                validators=[MinValueValidator(0),],
                                help_text="Insira a renda da pessoa")

    time_torce = models.ForeignKey(Time, on_delete=models.RESTRICT,
                                   help_text="Selecione o time que torce")

    esporte_favorito = models.ForeignKey(Esporte, on_delete=models.RESTRICT,
                                         help_text="Selecione o esporte favorito")

    cidade = models.ForeignKey(Cidade, on_delete=models.RESTRICT,
                               help_text="Selecione a cidade que mora")

    objects = PessoaManager()                               

    def __str__(self):
        return self.nome