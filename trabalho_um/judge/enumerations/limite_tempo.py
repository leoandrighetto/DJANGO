from django.db import models
from django.utils.translation import gettext_lazy as _


class LimiteTempo(models.TextChoices):

    S1 = '1000', _("1 segundo")
    S2 = '2000', _("2 segundos")
    S3 = '3000', _("3 segundos")
    S4 = '4000', _("4 segundos")
    S5 = '5000', _("5 segundos")
    S6 = '6000', _("6 segundos")
    S7 = '7000', _("7 segundos")
    S8 = '8000', _("8 segundos")
    S9 = '9000', _("9 segundos")
    S10 = '10000', _("10 segundo")
