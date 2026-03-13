from .pessoa import Pessoa
from django.db import models
from django.core.validators import MinLengthValidator

class Reporter(Pessoa):
    email = models.EmailField(max_length=100,validators=[MinLengthValidator(5)], help_text="Email institucional", verbose_name="Email")

