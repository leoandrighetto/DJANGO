from django.db import models


class StatusSubmission(models.TextChoices):
    NOT_ANSWERED = "Não Respondida"
    IN_QUEUE = "Em fila de Execução"
    RUNNING = "Execução"
    ACCEPTED = "Aceito"
    WRONG_ANSWER = "resposta Errada"
    TIME_LIMIT_EXCEEDED = "Tempo Limite Excedido"
    MEMORY_LIMIT_EXCEEDED = "Limite de memória Excedido"
    RUNTIME_ERROR = "Erro de Runtime"
    COMPILATION_ERROR = "Erro de Compilação"
    PRESENTATION_ERROR = " Erro de Apresentação"
    INTERNAL_ERROR = "Erro Interno"
