from logging.config import valid_ident
from xml.dom import ValidationErr
from django.core.exceptions import ValidationError


from django.utils.deconstruct import deconstructible
#permite que os objetos dessa classe sejam serializados e deserializados
@deconstructible
class PalavrasProibidas:
    # como isntanciar os objetos dessa classe
    def __init__(self, lista_proibida:list, mensagem:str):
        if not isinstance(lista_proibida, list):
            raise TypeError('A variavel lista_proibida deve ser do tipo list.')
        elif len(lista_proibida) == 0:
            raise ValueError('A variavel lista_proibida nao deve ser vazia')
        elif not isinstance(mensagem, str):
            raise TypeError('A variavel mensagem deve ser do tipo str.')
        elif mensagem.strip() == '':
            raise ValueError('A variavel mensagem nao deve ser vazia')
        self.lista_proibida = lista_proibida
        self.mensagem = mensagem

    # o que sera executado quando for invocado
    def __call__(self,valor_campo):
        for palavra in self.lista_proibida:
            if palavra.lower() == valor_campo.lower():
                raise ValidationError(
                    self.mensagem,
                    params={'value': valor_campo},
                )

    # como determinar se o objeto é igual a outro
    def __eq__(self, outro):
        if isinstance(outro, PalavrasProibidas):
            if len(self.lista_proibida) == len(outro.lista_proibida):
                for palavra in self.lista_proibida:
                    if palavra.lower() not in outro.lista_proibida:
                        return True
        return False