from tabnanny import verbose
from wsgiref.validate import validator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.core.validators import MinLengthValidator
from django.db import models
from ..validators import *

from categoria.enumerations import Nivel
from ..validators.palavras_proibidas import PalavrasProibidas


class Problema(models.Model):
    codigo = models.IntegerField(unique=True,validators=[MinValueValidator(1000),PalavrasProibidas(lista_proibida=['teste','admin'],mensage='o campo contem palavras que foram proibidas')],
                                                         help_text='Código do problema',)

    titulo = models.CharField(max_length = 100,
                              validators=[MinValueValidator(3)],
                              help_text='Titulo do problema',
                              verbose_name='Titulo')


    nivel = models.IntegerField(choices=Nivel, default=Nivel.UM,
                                verbose_name='Nivel',
                                help_text='Escolha o nivel do problema')

    descricao = models.TextField(max_length=2000, validators=[MinLengthValidator(20)],
                                 verbose_name ='descricao',
                                 help_text='Insira a descricao do problema para o usuario')

    exemplo_entrada = models.TextField(max_length=2000,
                                       verbose_name ='exemplo de entrada',
                                       help_text='Entrada esperada para a solucao do problema')

    exemplo_saida = models.TextField(max_length=2000,
                                     validators=[MinLengthValidator(1)],
                                     verbose_name ='exemplo saida',
                                     help_text='Saida esperada para a solucao do problema')

    testes_entrada = models.TextField(max_length=2000,
                                       verbose_name='teste de entrada',
                                       help_text='teste esperado para a solucao do problema')

    testes_saida = models.TextField(max_length=2000,
                                     validators=[MinLengthValidator(1)],
                                     verbose_name='teste saida',
                                     help_text='teste esperado para a solucao do problema')

    pontuacao = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(10.0)],
                                  verbose_name='pontuacao',
                                  help_text='Insira a pontuacao a ser creditada para o usuario')

    tempo_execucao = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(30)],
                                         verbose_name='tempo execucao',
                                         help_text='Insira o tempo maximo de execucao')

    memoria_maxima = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(256), memory_validator],
                                                             verbose_name='memoria maxima',
                                                             help_text='Insira a quantidade em MB de memoria maxima a ser utilizada')
    resolvidos = models.IntegerField(validators=[MinValueValidator(0)],
                                     verbose_name='resolvidos',
                                     help_text='quantidade de usuarios que resolveram o problema')
