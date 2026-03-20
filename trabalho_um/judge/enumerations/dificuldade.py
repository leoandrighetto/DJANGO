from django.utils.translation import gettext_lazy as _
from django.db import models


class Dificuldade(models.TextChoices):
    LVL1 = "1", _("Muito Fácil")
    LVL2 = "2", _("Fácil")
    LVL3 = "3", _("Básico")
    LVL4 = "4", _("intermediário")
    LVL5 = "5", _("Intermediário Alto")
    LVL6 = "6", _("Difícil")
    LVL7 = "7", _("Muito Difícil")
    LVL8 = "8", _("Avançado")
    LVL9 = "9", _("Muito Avançado")
    LVL10 = "10", _("Perito")
