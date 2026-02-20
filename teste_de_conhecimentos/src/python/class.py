class Curso:

    lista_cursos = []
    id = 0

    def __init__(self, cod: int, nome: str, grau:str, sigla:str, descricao:str, carga_horaria:int):

        self.__cod = cod
        self.__nome = nome        
        self.__grau = grau
        self.__sigla = sigla
        self.__descricao = descricao | None
        self.__carga_horaria = carga_horaria

        Curso.lista_cursos.append(self)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def setter_nome(self, novo_nome):

        if isinstance(novo_nome, str):
            if len(novo_nome) > 10 and len(novo_nome) < 100:
                self.__nome = novo_nome
            else:
                raise TypeError("O nome deve ter entre 10 e 100 caracteres")
        else:
            raise TypeError("O nome deve ser uma String")
        
    @property
    def grau(self):
        return self.__grau
    
    @grau.setter
    def setter_grau(self, novo_grau):

        if isinstance(novo_grau, str):
            if len(novo_grau) > 5 and len(novo_grau) < 30:
                self.__grau = novo_grau
            else:
                raise TypeError("O grau deve ter entre 5 e 30 caracteres")
        else:
            raise TypeError("O grau deve ser uma String")
        
    @property
    def sigla(self):
        return self.__sigla
    
    @sigla.setter
    def setter_sigla(self, nova_sigla):

        if isinstance(nova_sigla, str):
            if len(nova_sigla) == 3:
                self.__sigla = nova_sigla
            else:
                raise TypeError("A sigla deve ter 3 caracteres")
        else:
            raise TypeError("A sigla deve ser uma String")
        
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def setter_descricao(self, nova_descricao):

        if isinstance(nova_descricao, str):
            if len(nova_descricao) > 10 and len(nova_descricao) < 100:
                self.__nome = nova_descricao
            else:
                raise TypeError("O nome deve ter entre 10 e 100 caracteres")
        else:
            raise TypeError("O nome deve ser uma String")
        
    

    def __str__(self):
        return (f'INFORMAÇÕES SOBRE O CURSO: \n\n'
                f'Código: {self.cod}\n'
                f'Nome: {self.nome}\n'
                f'Grau: {self.grau}\n'
                f'Sigla: {self.sigla}\n'
                f'Descricao: {self.descricao}\n'
                f'Carga Horária: {self.carga_horaria}\n')
    
    def listar_cursos(cls):

        print("\nLISTA DE CURSOS DISPONÍVEIS\n\n")
        for curso in cls.lista_cursos:
            print(curso)



class Disciplina:

    def __init__(self, cod: int, nome: str, grau:str, sigla:str, ementa:str, carga_horaria:int, data_inicio: str, data_fim: str, referencias: str):
        pass