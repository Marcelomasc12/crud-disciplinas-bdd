from typing import List

from fastapi import FastAPI, HTTPException

from src.service_db import (
    criar_disciplina_db,
    listar_disciplinas_db,
    atualizar_disciplina_db,
    deletar_disciplina_db,
)

from src.schemas import (
    DisciplinaCreate,
    DisciplinaResponse,
    DisciplinaUpdate,
)

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}


@app.post("/disciplinas", response_model=DisciplinaResponse)
def criar_disciplina(disciplina: DisciplinaCreate):
    return criar_disciplina_db(
        titulo=disciplina.titulo,
        data_inicio=disciplina.data_inicio,
        data_termino=disciplina.data_termino,
        numero_vagas=disciplina.numero_vagas,
        verao=disciplina.verao,
    )


@app.get("/disciplinas", response_model=List[DisciplinaResponse])
def listar():
    return listar_disciplinas_db()


@app.put("/disciplinas/{id}", response_model=DisciplinaResponse)
def atualizar(id: int, novos_dados: DisciplinaUpdate):
    disciplina = atualizar_disciplina_db(id, novos_dados.dict())

    if disciplina is None:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")

    return disciplina


@app.delete("/disciplinas/{id}")
def deletar(id: int):
    deletado = deletar_disciplina_db(id)

    if not deletado:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")

    return {"mensagem": "Disciplina deletada com sucesso"}