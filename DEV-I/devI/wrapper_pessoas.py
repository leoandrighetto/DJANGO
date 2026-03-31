from manage import *
from decimal import Decimal
import contextlib, io


saida = io.StringIO()


with contextlib.redirect_stdout(saida):
    main()


from relacionamento.models import Esporte, Time, Cidade, Pessoaa
from relacionamento.models import Sexo

processados = 0
erros = 0

with open("pessoas.csv", "r", encoding="utf-8") as a:

    try:
        a.readline()  # lê a primeira linha e não armazena

        for linha in a:

            dados = linha.split(",")
            nome = dados[0]
            sexo = dados[1]
            idade = int(dados[2])
            cidade = dados[3]
            estado = dados[4]
            time_que_torce = dados[5]
            renda = Decimal(dados[6])
            esporte_favorito = dados[6]

            if sexo.upper() == "MASCULINO":
                sexo = Sexo.MASCULINO

            elif sexo.upper() == "FEMININO":
                sexo = Sexo.MASCULINO

            else:
                raise ValueError

            try:
                endereco = Cidade.objects.filter(nome=cidade, estado=estado)
                if len(endereco) == 0:
                    nova_cidade = Cidade(nome=cidade, estado=estado)

                    try:

                        nova_cidade.full_clean()
                        nova_cidade.save()

                    except Exception as e:
                        print(str(e))

                # um elemento encontrado no banco
                elif len(endereco) == 1:
                    nova_cidade = endereco[0]

                # mais de um elemento
                else:
                    raise ValueError("Cidade em duplicação")

            except Exception as e:
                print(str(e))

            try:

                times = Time.objects.filter(name=time_que_torce)

                try:
                    if len(times) == 0:
                        novo_time = Time(name=time_que_torce)
                        novo_time.full_clean()
                        novo_time.save()

                    elif len(times) == 1:
                        novo_time = times[0]

                    else:
                        raise ValueError("Times duplicados no banco")

                except Exception as e:
                    print(str(e))

            except Exception as e:
                print(str(e))

            try:
                esportes = Esporte.objects.filter(name=esporte_favorito)
                try:
                    if len(esportes) == 0:

                        novo_esporte = Esporte(name=esporte_favorito)
                        novo_esporte.full_clean()
                        novo_esporte.save()

                    elif len(esportes) == 1:
                        novo_esporte = esportes[0]

                    else:
                        raise ValueError("Esportes duplicados no banco")

                except Exception as e:
                    print(str(e))

            except Exception as e:
                print(str(e))

            try:
                nova_pessoa = Pessoaa(
                    nome=nome,
                    sexo=sexo,
                    idade=idade,
                    renda=renda,
                    time_torce=novo_time,
                    esporte_favorito=novo_esporte,
                    cidade=nova_cidade,
                )

                nova_pessoa.full_clean()
                nova_pessoa.save()
                processados += 1

                print("SALVOU A PESSOA BEM DIREITINHO, MANO! Parabénsh.")

            except Exception as e:
                erros += 1
                print(str(e))

    except Exception as e:
        print(str(e))

print("CABÔ... PROCESSAMENTO CONCLUÍDO.")
print(
    f"Total de processos: {processados + erros}"
    f"Processados corretamente: {processados}"
    f"Processados com erro: {erros}"
)
