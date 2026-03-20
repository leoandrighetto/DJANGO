from django.db import models
from django.utils.translation import gettext_lazy as _


class LimiteMemoria(models.TextChoices):
    MB8 = "8 MB", _("8 MB")
    MB16 = "16 MB", _("16 MB")
    MB32 = "32 MB", _("32 MB")
    MB64 = "64 MB", _("64 MB")
    MB128 = "128 MB", _("128 MB")
    MD256 = "256 MB", _("256 MB")
