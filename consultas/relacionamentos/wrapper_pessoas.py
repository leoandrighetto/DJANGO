from decimal import Decimal

from rest_framework.exceptions import ValidationError

from manage import *
import contextlib, io

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()

from wrapper.models import Esporte, Time, Cidade, Pessoa
from wrapper.enumerations import Sexo

processados = 0
erros = 0

with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    try:
        # lê a primeira linha e não armazena
        arquivo.readline()

        # faz a leitura do restante do arquivo
        for linha in arquivo:
            dados = linha.split(',')
            nome = dados[0]
            sexo = dados[1]
            idade = int(dados[2])
            cidade = dados[3]
            estado = dados[4]
            time = dados[5]
            renda = Decimal(dados[6])
            esporte = dados[7]

            if sexo.upper() == "MASCULINO":
                sexo = Sexo.MASCULINO
            elif sexo.upper() == "FEMININO":
                sexo = Sexo.FEMININO
            else:
                raise ValueError("Sexo não cadastrado no enum")


            # consulta e cadastro da cidade
            try:
                endereco = Cidade.objects.filter(nome=cidade, estado=estado)

                # cidade não está cadastrada
                if len(endereco) == 0:
                    try:
                        cidade_cadastrada = Cidade(nome=cidade, estado=estado)
                        cidade_cadastrada.full_clean()
                        cidade_cadastrada.save()
                    except ValidationError as e:
                        print(e)
                # cidade cadastrada
                elif len(endereco) == 1:
                    cidade_cadastrada = endereco[0]
                # mais de uma cidade cadastrada
                else:
                    raise ValueError("Cidade em duplicidade")
            except Exception as e:
                print(e)


            # consulta e cadastro do time
            try:
                clube = Time.objects.filter(nome=time)

                # time não cadastrado
                if len(clube) == 0:
                    clube = Time(nome=time)
                    clube.full_clean()
                    clube.save()
                # time já está cadastrado
                elif len(clube) == 1:
                    clube = clube[0]
                else:
                    raise ValueError("Clube cadastrado em duplicidade")
            except Exception as e:
                print(e)

            # consulta e cadastro para o esporte favorito
            try:
                esporte_favorito = Esporte.objects.filter(nome=esporte)
                if len(esporte_favorito) == 0:
                    esporte_favorito = Esporte(nome=esporte)
                    esporte_favorito.full_clean()
                    esporte_favorito.save()
                elif len(esporte_favorito) == 1:
                    esporte_favorito = esporte_favorito[0]
                else:
                    raise ValueError("Esporte cadastrado em duplicidade")
            except Exception as e:
                print(e)

            try:
                nova_pessoa = Pessoa(
                    nome=nome,
                    sexo=sexo,
                    idade=idade,
                    renda=renda,
                    time_torce=clube,
                    esporte_favorito=esporte_favorito,
                    cidade=cidade_cadastrada,
                )
                nova_pessoa.full_clean()
                nova_pessoa.save()
                print(f"Registro processado: {linha}")
                processados += 1
            except Exception as e:
                print(f"Problema ao salvar: {linha}")
                print(e)
                erros += 1
    except Exception as e:
        print(f"Problema ao salvar: {linha}")
        print(e)
        erros += 1

print("Processamento concluído")
print(f"Total: {processados+erros}")
print(f"Processados Corretamente: {processados}")
print(f"erros: {erros}")

