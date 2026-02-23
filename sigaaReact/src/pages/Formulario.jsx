import { useEffect, useState } from "react";

export default function Formulario() {
  const [cursos, setCursos] = useState([]);
  const [codigoCurso, setCodigoCurso] = useState(0);
  const [nomeCurso, setNomeCurso] = useState("");
  const [grauCurso, setGrauCurso] = useState("");
  const [siglaCurso, setSiglaCurso] = useState("");
  const [descricaoCurso, setDescricaoCurso] = useState("");
  const [carga_horariaCurso, setCargaHorariaCurso] = useState(0);
  const [disciplinasDosCursos, setDisciplinasDosCursos] = useState([]);

  const [disciplinas, setDisciplinas] = useState([]);
  const [codigoDisciplina, setCodigoDisciplina] = useState("");
  const [nomeCursoDaDisciplina, setNomeCursoDaDisciplina] = useState("");
  const [nomeDisciplina, setNomeDisciplina] = useState("");
  const [siglaDisciplina, setSiglaDisciplina] = useState("");
  const [ementa, setEmenta] = useState("");
  const [cargaHorariaDisciplina, setCargaHorariaDisciplina] = useState(null);
  const hoje = new Date().toISOString().split("T")[0];

  const [dataInicio, setDataInicio] = useState(hoje);
  const [dataFim, setDataFim] = useState("");
  const [referencias, setReferencias] = useState("");

  function cadastrarCurso() {
    let novoCodigo = codigoCurso + 1;
    let novo_curso = {
      codigoCurso: novoCodigo,
      nomeCurso,
      grauCurso,
      siglaCurso,
      descricaoCurso,
      carga_horariaCurso,
    };

    let novo_cursos = [...cursos, novo_curso];
    setCursos(novo_cursos);

    setCodigoCurso(novoCodigo);

    let novo_disciplinas_curso = [...disciplinasDosCursos, { [nomeCurso]: [] }];

    setDisciplinasDosCursos(novo_disciplinas_curso);
  }

  console.log(disciplinasDosCursos);
  function cadastrarDisciplina() {
    let novoCodigoDisciplina = codigoDisciplina + 1;
    let nova_disciplina = {
      codigo: novoCodigoDisciplina,
      nomeDisciplina,
      siglaDisciplina,
      ementa,
      cargaHorariaDisciplina,
      dataInicio,
      dataFim,
      referencias,
    };

    let novo_disciplinas = [...disciplinas, nova_disciplina];
    setDisciplinas(novo_disciplinas);

    setCodigoDisciplina(novoCodigoDisciplina);

    setDisciplinasDosCursos((prev) =>
      prev.map((obj) => {
        const [nome, disc] = Object.entries(obj)[0];

        if (nome === nomeCursoDaDisciplina) {
          return { [nome]: [...disc, nomeDisciplina] };
        }

        return obj;
      }),
    );
  }

  return (
    <>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          marginLeft: "10em",
          gap: "5em",
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            width: "300px",
            gap: "10px",
          }}
        >
          <p>Cadastro de curso:</p>
          <input
            placeholder="Digite o nome do curso"
            value={nomeCurso}
            onChange={(e) => setNomeCurso(e.target.value)}
            type="text"
            minLength={10}
            maxLength={100}
          />

          <input
            placeholder="Digite o grau do curso"
            value={grauCurso}
            onChange={(e) => setGrauCurso(e.target.value)}
            type="text"
            minLength={5}
            maxLength={30}
          />

          <input
            placeholder="Digite a sigla do curso"
            value={siglaCurso}
            onChange={(e) => setSiglaCurso(e.target.value)}
            type="text"
            minLength={3}
            maxLength={3}
          />

          <input
            placeholder="Digite uma descrição para o curso"
            value={descricaoCurso}
            onChange={(e) => setDescricaoCurso(e.target.value)}
            type="text"
            maxLength={500}
          />

          <input
            placeholder="Digite a carga horária total do curso"
            value={carga_horariaCurso}
            onChange={(e) => setCargaHorariaCurso(e.target.value)}
            type="number"
            min={600}
          />

          <button onClick={() => cadastrarCurso()}>Cadastrar Curso</button>

          <div>
            {cursos.map((c, i) => (
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  whiteSpace: "pre-line",
                }}
                key={i}
              >
                {"Nome: " +
                  c.nomeCurso +
                  "\n" +
                  "Grau: " +
                  c.grauCurso +
                  "\n" +
                  "Sigla: " +
                  c.siglaCurso +
                  "\n" +
                  "Descrição: " +
                  c.descricaoCurso +
                  "\n" +
                  "Carga Horária Total: " +
                  c.carga_horariaCurso +
                  "\n\n"}
              </div>
            ))}
          </div>
        </div>

        <div
          style={{
            display: "flex",
            flexDirection: "column",
            width: "300px",
            gap: "10px",
          }}
        >
          <p>Cadastro de Disciplinas:</p>

          <input
            placeholder="Digite o curso da disciplina"
            value={nomeCursoDaDisciplina}
            onChange={(e) => setNomeCursoDaDisciplina(e.target.value)}
            type="text"
          />

          <input
            placeholder="Digite o nome da disciplina"
            value={nomeDisciplina}
            onChange={(e) => setNomeDisciplina(e.target.value)}
            type="text"
            minLength={5}
            maxLength={50}
          />

          <input
            placeholder="Digite a sigla da disciplina"
            value={siglaDisciplina}
            onChange={(e) => setSiglaDisciplina(e.target.value)}
            type="text"
            minLength={3}
            maxLength={3}
          />

          <input
            placeholder="Digite uma ementa para a disciplina"
            value={ementa}
            onChange={(e) => setEmenta(e.target.value)}
            minLength={30}
            maxLength={300}
            type="text"
          />

          <input
            placeholder="Digite a carga horária total da disciplina"
            value={cargaHorariaDisciplina}
            onChange={(e) => setCargaHorariaDisciplina(e.target.value)}
            type="number"
            min={20}
          />

          <input
            placeholder="Digite a data de início da disciplina"
            value={dataInicio}
            onChange={(e) => setDataInicio(e.target.value)}
            type="date"
            min={600}
          />

          <input
            placeholder="Digite a data de fim da disciplina"
            value={dataFim}
            onChange={(e) => setDataFim(e.target.value)}
            type="date"
            min={hoje}
          />

          <input
            placeholder="Digite a referência da disciplina"
            value={referencias}
            onChange={(e) => setReferencias(e.target.value)}
            type="text"
            minLength={50}
            maxLength={500}
          />

          <button onClick={() => cadastrarDisciplina()}>
            Cadastrar Disciplina
          </button>

          <div>
            {disciplinas.map((c, i) => (
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  whiteSpace: "pre-line",
                }}
                key={i}
              >
                {"Nome: " +
                  c.nomeDisciplina +
                  "\n" +
                  "Sigla: " +
                  c.siglaDisciplina +
                  "\n" +
                  "Ementa: " +
                  c.ementa +
                  "\n" +
                  "Carga Horária: " +
                  c.cargaHorariaDisciplina +
                  "\n" +
                  "Data de Início: " +
                  c.dataInicio +
                  "\n" +
                  "Data de término: " +
                  c.dataFim +
                  "\n" +
                  "Referência: " +
                  c.referencias +
                  "\n\n"}
              </div>
            ))}
          </div>

        </div>
        
      </div>
    </>
  );
}
