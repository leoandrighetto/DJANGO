from django.db import models

class Profissao(models.TextChoices):
    #CONSTANTE = "NOME NO BD", "NOME PARA USUARIO"
    ANALISTA = "Analista", "Analista de Sistemas"
    DESEMPREGADO = "Desempregado", "Desempregado"
    ESTUDANTE = "Estudante", "Estudante"
    PROFESSOR = "Professor", "Professor"
    PROGRAMADOR = "Programador", "Programador"

