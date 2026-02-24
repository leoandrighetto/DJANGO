from typing import ClassVar
from datetime import datetime
from datetime import date


class Curso:

    cursos: ClassVar[list] = []

    codigos_cursos: ClassVar[int] = 0

    def __init__(self, nome, grau, sigla, carga_horaria, descricao):

        Curso.codigos_cursos += 1
        self.__cod = Curso.codigos_cursos
        self.nome = nome
        self.grau = grau
        self.sigla = sigla
        self.descricao = descricao
        self.carga_horaria = carga_horaria

        self.disciplinas_cursos = []

        Curso.cursos.append(self)

    @property
    def cod(self):
        return self.__cod

    @property
    def nome(self):
        return self.__nome

    @property
    def grau(self):
        return self.__grau

    @property
    def sigla(self):
        return self.__sigla

    @property
    def descricao(self):
        return self.__descricao

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @nome.setter
    def nome(self, valor: str):

        if not isinstance(valor, str) or len(valor) < 10 or len(valor) > 100:
            raise ValueError(
                "O nome do curso deve conter somente letras, de 10 a 100 caracteres."
            )

        self.__nome = valor

    @grau.setter
    def grau(self, valor: str):

        if not isinstance(valor, str) or len(valor) < 5 or len(valor) > 30:
            raise ValueError(
                "O grau do curso deve conter somente letras, de 5 a 30 caracteres."
            )

        self.__grau = valor

    @sigla.setter
    def sigla(self, valor: str):

        if not isinstance(valor, str) or len(valor) != 3:
            raise ValueError(
                "A sigla do curso deve conter somente letras, com 3 caracteres."
            )

        self.__sigla = valor

    @descricao.setter
    def descricao(self, valor: str):
        if valor is not None:
            if not isinstance(valor, str) or len(valor) > 500:
                raise ValueError(
                    "A descrição deve conter somente letras de até 500 caracteres."
                )
        self.__descricao = valor

    @carga_horaria.setter
    def carga_horaria(self, valor: int):

        if not isinstance(valor, int) or valor < 600:
            raise ValueError(
                "A carga horária deve conter apenas números, com valor mínimo de 600."
            )
        self.__carga_horaria = valor

    def __str__(self):
        return (
            f"Código: {self.cod}\n"
            f"Nome: {self.nome}\n"
            f"Grau: {self.grau}\n"
            f"Sigla: {self.sigla}\n"
            f"{'Descrição: ' + self.descricao + '\n' if self.descricao else ''}"
            f"Carga Horária Total: {self.carga_horaria}\n\n"
        )

    @staticmethod
    def listar_cursos():
        print(f"\n LISTA DE CURSOS:\n\n")
        for curso in Curso.cursos:
            print(curso)

    def adicionar_disciplina(self, disciplina):
        if not isinstance(disciplina, Disciplina):
            raise ValueError("Disciplina deve ser um objeto da classe de disciplinas.")

        self.disciplinas_cursos.append(disciplina)

    def listar_disciplinas_do_curso(self):
        print(f"\n LISTA DE DISCIPLINAS DO CURSO {self.nome}:\n")
        for disciplina in self.disciplinas_cursos:
            print(f"{disciplina.nome}")


class Disciplina:

    codigos_disciplinas: ClassVar[int] = 0
    disciplinas_atuais: ClassVar[list] = []

    def __init__(
        self,
        nome,
        curso,
        sigla,
        ementa,
        carga_horaria,
        data_inicio,
        data_fim,
        referencias,
    ):

        if not isinstance(curso, Curso):
            raise TypeError("O curso informado deve estar associado a um curso válido")

        self.nome = nome
        self.curso = curso
        self.sigla = sigla
        self.ementa = ementa
        self.carga_horaria = carga_horaria
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.referencias = referencias

        Disciplina.disciplinas_atuais.append(self)

        curso.adicionar_disciplina(self)

    @property
    def nome(self):
        return self.__nome

    @property
    def sigla(self):
        return self.__sigla

    @property
    def ementa(self):
        return self.__ementa

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @property
    def data_inicio(self):
        return self.__data_inicio

    @property
    def data_fim(self):
        return self.__data_fim

    @property
    def referencias(self):
        return self.__referencias

    @property
    def funcao(self):
        return self.__nova

    @property
    def funcao(self):
        return self.__nova

    @nome.setter
    def nome(self, valor: str):

        if not isinstance(valor, str) or len(valor) < 5 or len(valor) > 50:
            raise ValueError(
                "O nome da disciplina deve conter somente letras, de 5 a 50 caracteres."
            )

        self.__nome = valor

    @sigla.setter
    def sigla(self, valor: str):

        if valor:

            if not isinstance(valor, str) or len(valor) < 3 or len(valor) > 10:
                raise ValueError(
                    "A sigla da disciplina deve conter somente letras, com 3 caracteres."
                )

            self.__sigla = valor

        else:
            self.__sigla = None

    @ementa.setter
    def ementa(self, valor: str):

        if not isinstance(valor, str) or len(valor) < 30 or len(valor) > 300:
            raise ValueError(
                "A ementa da disciplina deve conter somente letras, entre 30 e 300 caracteres."
            )

        self.__ementa = valor

    @carga_horaria.setter
    def carga_horaria(self, valor: int):

        if not isinstance(valor, int) or valor < 20:
            raise ValueError(
                "A carga horária da disciplina deve conter somente números, com valor mínimo de 20 (horas)."
            )
        self.__carga_horaria = valor

    @data_inicio.setter
    def data_inicio(self, valor: date):

        if not valor:
            self.__data_inicio = date.today()

        else:
            try:
                data = datetime.strptime(valor, "%d/%m/%Y").date()
                self.__data_inicio = data
            except ValueError:
                raise ValueError("O formato da data de início deve ser DD/MM/AA.")

    @data_fim.setter
    def data_fim(self, valor: date):

        if not valor:
            raise ValueError("A data final deve ser informada.")
        else:
            try:
                data = datetime.strptime(valor, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError(
                    "Data inválida. O formato da data de início deve ser DD/MM/AA."
                )

            if data < self.__data_inicio:
                raise ValueError(
                    "A data final deve ser no mínimo igual a data de início."
                )

            self.__data_fim = data

    @referencias.setter
    def referencias(self, valor: str):

        if not isinstance(valor, str) or len(valor) < 50 or len(valor) > 500:
            raise ValueError(
                "A referência deve conter somente letras, entre 50 e 500 caracteres."
            )

        self.__referencias = valor

    def __str__(self):

        return (
            f"\nDisciplina: {self.nome}\n"
            f"Curso: {self.curso.nome}\n"
            f"{'Sigla: ' + self.sigla + '\n' if self.sigla else ''}"
            f"Ementa: {self.ementa}\n"
            f"Carga Horária: {self.carga_horaria}\n"
            f"Data de Início: {self.data_inicio}\n"
            f"Data Final: {self.data_fim}\n"
            f"Referências: {self.referencias}\n"
        )

    @staticmethod
    def listarDisciplinas():

        return {disciplina for disciplina in Disciplina.disciplinas_atuais}


curso1 = Curso(
    "Ciências da Computação",
    "Superior",
    "CIC",
    3000,
    "Estudos intensivos sobre computação.",
)

curso2 = Curso(
    "Confeitaria Gourmet",
    "Superior",
    "CON",
    600,
    "Aprender a fazer um bolo de cenoura bom.",
)

print(curso1)

print(curso2)


disciplina1 = Disciplina(
    nome="Lógica de Computador",
    curso=curso1,
    sigla="PER",
    ementa="Super ementa bem trabalhada essa...Super ementaSuper ementaSuper ementaSuper ementa",
    carga_horaria=600,
    data_inicio="20/02/2026",
    data_fim="22/02/2027",
    referencias="Referências incríveis de youtubers tipo Mano Deyvin... referencias referencias referencias referencias",
)

disciplina2 = Disciplina(
    nome="Matemática de Granulados",
    curso=curso2,
    sigla="MDG",
    ementa="Super ementa Super ementaSuper ementaSuper ementaSuper ementaSuper ementa",
    carga_horaria=600,
    data_inicio="20/02/2026",
    data_fim="22/02/2027",
    referencias="referencias referencias referencias referencias referencias referencias referencias",
)


print(disciplina1)
print(disciplina2)
curso1.listar_disciplinas_do_curso()
curso2.listar_disciplinas_do_curso()
