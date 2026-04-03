from django.db.models import QuerySet
from .base_manager import BaseManager
from decimal import Decimal

class PessoaManager(BaseManager):

    def find_by_renda(self, renda: Decimal) -> QuerySet["Pessoa"]:
        if isinstance (renda, Decimal) and renda > 0:
            consulta = self.filter(renda__gte=renda).order_by("nome")
            return consulta
        else:
            raise TypeError("a renda deve ser um número decimal maior que 0.")

    
    """

    >>> from decimal import Decimal
    >>> from wrapper.models import pessoa

    >>> p = Pessoa.objects.find_by_renda(Decimal("10000.00"))

    >>> for i in p:
    ...     print(f"{i.nome} - {i.renda}")
    ... 
    Eduardo - 14414.89
    Thales - 11618.22
    Raul - 11205.28
    Maria Sophia - 14171.38
    ...
    ...




    """