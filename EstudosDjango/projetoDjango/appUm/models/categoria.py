from django.db import models
from ..models import BaseModel


class categoria(BaseModel):
    nome = models.CharField(max_length=50)
    area = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Área do conhecimento",
        help_text="Digite a área do conhecimento segundo o padrão CAPES",
    )
    instituicao = models.CharField(
        max_length=5,
        default="IFRS",
        verbose_name="Instutuição de ensino",
        help_text="Digite a sigla da instituição de ensino (no máximo 5 caracteres)",
    )

    def __str__(self):
        return (
            f"\nID: {self.id}\n"
            f"Nome: {self.nome}\n"
            f"Área: {self.area}\n"
            f"Instituição: {self.instituicao}\n"
        )
