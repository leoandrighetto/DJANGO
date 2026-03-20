from django.db import models


class Idioma(models.TextChoices):
    PT_BR = "Português do Brasil"
    EN_US = "Inglês dos EUA"
    ES_ES = "Espanhol da Espanha"
