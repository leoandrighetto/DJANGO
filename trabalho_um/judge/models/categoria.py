from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator


class Categoria(BaseModel):
    nome = models.CharField(
        max_length=50, validators=[MinLengthValidator(5)], help_text="Nome da categoria"
    )
    slug = models.SlugField(
        max_length=50,
        validators=[MinLengthValidator(5)],
        unique=True,
        help_text="Slug da categoria",
    )
    descricao = models.TextField(help_text="Descrição da categoria"
    )

    def __str__(self):
        return f"Nome: {self.nome} Slug: {self.slug} Descrição: {self.descricao}"
