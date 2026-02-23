import { useEffect, useState } from "react";

export default function Formulario() {
  const [codigo, setCodigo] = useState(0);
  const [nome, setNome] = useState("");
  const [grau, setGrau] = useState("");
  const [sigla, setSigla] = useState("");
  const [descricao, setDescricao] = useState("");
  const [carga_horaria, setCargaHoraria] = useState(0);

  const [cursos, setCursos] = useState([]);
  const [disciplina, setDisciplina] = useState([]);

  function cadastrarCurso() {
    let novoCodigo = codigo + 1;
    let novo_curso = {
      codigo: novoCodigo,
      nome,
      grau,
      sigla,
      descricao,
      carga_horaria,
    };

    let novo_cursos = [...cursos, novo_curso];
    setCursos(novo_cursos);

    setCodigo(novoCodigo);
  }

  return (
    <>
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
          value={nome}
          onChange={(e) => setNome(e.target.value)}
          type="text"
          minLength={10}
          maxLength={100}
        />

        <input
          placeholder="Digite o grau do curso"
          value={grau}
          onChange={(e) => setGrau(e.target.value)}
          type="text"
          minLength={5}
          maxLength={30}
        />

        <input
          placeholder="Digite a sigla do curso"
          value={sigla}
          onChange={(e) => setSigla(e.target.value)}
          type="text"
          minLength={3}
          maxLength={3}
        />

        <input
          placeholder="Digite uma descrição para o curso"
          value={descricao}
          onChange={(e) => setDescricao(e.target.value)}
          type="text"
          maxLength={500}
        />

        <input
          placeholder="Digite a carga horária total do curso"
          value={carga_horaria}
          onChange={(e) => setCargaHoraria(e.target.value)}
          type="number"
          min={600}
        />

        <button onClick={() => cadastrarCurso()}>Cadastrar Curso</button>

        <div>
          {cursos.map((c, i) => (
            
              <div key={i}>{c.nome}</div>
            
          ))}
        </div>
      </div>
    </>
  );
}
