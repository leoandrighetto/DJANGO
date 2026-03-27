from manage import *
import contextlib, io
from django.utils.dateparse import parse_date

stdout = io.StringIO()
from datetime import date

with contextlib.redirect_stdout(stdout):
    main()

from relacionamento.models import Pessoa, Passaporte, Artigo, Reporter

Passaporte.objects.all().delete()
Artigo.objects.all().delete()
Pessoa.objects.all().delete()

Lucas = Pessoa(
    nome="Lucas", data_nascimento=parse_date("2003-10-11"), cpf="03612078147"
)
Millena = Pessoa(
    nome="Millena", data_nascimento=parse_date("2002-10-11"), cpf="54124566589"
)
Mirella = Pessoa(
    nome="Mirella", data_nascimento=parse_date("1987-10-11"), cpf="44211546754"
)
Mayara = Pessoa(
    nome="Mayara", data_nascimento=parse_date("1989-10-11"), cpf="45412145478"
)

pessoas = [Lucas, Millena, Mayara, Mirella]

for pessoa in pessoas:

    try:
        pessoa.full_clean()
        pessoa.save()
    except Exception as e:
        print(str(e))


print("\nPessoas Cadastradas com Sucesso\n")

db_lucas = Pessoa.objects.get(nome="Lucas")
db_millena = Pessoa.objects.get(nome="Millena")
db_mirella = Pessoa.objects.get(nome="Mirella")
db_mayara = Pessoa.objects.get(nome="Mayara")

passaporte_1 = Passaporte(
    numero=1234,
    emissao=date.today(),
    vencimento=parse_date("2038-12-12"),
    pessoa=db_lucas,
)
passaporte_2 = Passaporte(
    numero=2345,
    emissao=date.today(),
    vencimento=parse_date("2038-12-12"),
    pessoa=db_millena,
)
passaporte_3 = Passaporte(
    numero=3456,
    emissao=date.today(),
    vencimento=parse_date("2038-12-12"),
    pessoa=db_mirella,
)
passaporte_4 = Passaporte(
    numero=4567,
    emissao=date.today(),
    vencimento=parse_date("2038-12-12"),
    pessoa=db_mayara,
)

passaportes = [passaporte_1, passaporte_2, passaporte_3, passaporte_4]

for passaporte in passaportes:

    try:
        passaporte.full_clean()
        passaporte.save()

    except Exception as e:
        print(str(e))


print("\nPassaportes Cadastrados com Sucesso\n")


reporter_1 = Reporter(
    nome="Diego",
    data_nascimento=parse_date("2003-10-11"),
    cpf="01264325879",
    email="Diego@gmail.com",
)
reporter_2 = Reporter(
    nome="Roger",
    data_nascimento=parse_date("2003-10-11"),
    cpf="65632154856",
    email="Roger@gmail.com",
)
reporter_3 = Reporter(
    nome="Tomas",
    data_nascimento=parse_date("2003-10-11"),
    cpf="54896532648",
    email="Tomas@gmail.com",
)
reporter_4 = Reporter(
    nome="Maicon",
    data_nascimento=parse_date("2003-10-11"),
    cpf="54565632565",
    email="Maicon@gmail.com",
)

reporteres = [reporter_1, reporter_2, reporter_3, reporter_4]

for reporter in reporteres:
    try:
        reporter.full_clean()
        reporter.save()
    except Exception as e:
        print(str(e))


print("\nReporteres cadastrados con sucesso\n")

db_diego = Reporter.objects.get(nome="Diego")
db_roger = Reporter.objects.get(nome="Roger")
db_tomas = Reporter.objects.get(nome="Tomas")
db_maicon = Reporter.objects.get(nome="Maicon")


artigos = [
    Artigo(autor=db_diego, titulo="Artigo do Diego", data_publicacao=date.today()),
    Artigo(autor=db_roger, titulo="Artigo do Roger", data_publicacao=date.today()),
    Artigo(autor=db_tomas, titulo="Artigo do Tomas", data_publicacao=date.today()),
    Artigo(autor=db_maicon, titulo="Artigo do Maicon", data_publicacao=date.today()),
]


for artigo in artigos:

    try:
        artigo.full_clean()
        artigo.save()

    except Exception as e:
        print(str(e))

print("\nArtigos Cadastrados com Sucesso\n")
