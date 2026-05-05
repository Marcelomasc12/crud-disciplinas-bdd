from pydantic import BaseModel, validator
from datetime import datetime


class DisciplinaBase(BaseModel):
    titulo: str
    data_inicio: str
    data_termino: str
    numero_vagas: int
    verao: bool

    @validator("data_termino")
    def validar_datas(cls, v, values):
        data_inicio = values.get("data_inicio")

        if data_inicio:
            inicio = datetime.fromisoformat(data_inicio)
            termino = datetime.fromisoformat(v)

            if termino <= inicio:
                raise ValueError("data_termino deve ser maior que data_inicio")

        return v


class DisciplinaCreate(DisciplinaBase):
    pass


class DisciplinaUpdate(DisciplinaBase):
    pass


class DisciplinaResponse(DisciplinaBase):
    id: int

    class Config:
        from_attributes = True