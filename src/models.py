from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base


class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    data_inicio = Column(String, nullable=False)
    data_termino = Column(String, nullable=False)
    numero_vagas = Column(Integer, nullable=False)
    verao = Column(Boolean, nullable=False)