from django.db import models
from ..models import BaseModel
from ..validators import cpf


class aluno(BaseModel):
    nome = models.CharField(max_length=50,verbose_name="Nome",help_text="Digite o nome do aluno.")
    ano_nascimento = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Data de Nascimento",help_text="Digite a data de nascimento do aluno.")
    cpf = models.CharField(
        max_length=14,
        validators=[cpf],
        verbose_name="CPF",help_text="Digite o CPF do aluno"
    )

    def __str__(self):
        return (f'ID: {self.id} Nome: {self.nome} Ano De Nascimento: {self.ano_nascimento} CPF: {self.cpf}')