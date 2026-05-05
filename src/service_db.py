from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.models import Disciplina


def criar_disciplina_db(titulo, data_inicio, data_termino, numero_vagas, verao):
    db: Session = SessionLocal()

    try:
        nova = Disciplina(
            
            titulo=titulo,
            data_inicio=data_inicio,
            data_termino=data_termino,
            numero_vagas=numero_vagas,
            verao=verao
        )

        db.add(nova)
        db.commit()
        db.refresh(nova)

        return {
            "id": nova.id,
            "titulo": nova.titulo,
            "data_inicio": nova.data_inicio,
            "data_termino": nova.data_termino,
            "numero_vagas": nova.numero_vagas,
            "verao": nova.verao
        }

    finally:
        db.close()


def listar_disciplinas_db():
    db: Session = SessionLocal()

    try:
        disciplinas = db.query(Disciplina).all()

        return [
            {
                "id": d.id,
                "titulo": d.titulo,
                "data_inicio": d.data_inicio,
                "data_termino": d.data_termino,
                "numero_vagas": d.numero_vagas,
                "verao": d.verao
            }
            for d in disciplinas
        ]

    finally:
        db.close()


def atualizar_disciplina_db(id, novos_dados):
    db: Session = SessionLocal()

    try:
        disciplina = db.query(Disciplina).filter(Disciplina.id == id).first()

        if not disciplina:
            return None

        for chave, valor in novos_dados.items():
            setattr(disciplina, chave, valor)

        db.commit()
        db.refresh(disciplina)

        return {
            "id": disciplina.id,
            "titulo": disciplina.titulo,
            "data_inicio": disciplina.data_inicio,
            "data_termino": disciplina.data_termino,
            "numero_vagas": disciplina.numero_vagas,
            "verao": disciplina.verao
        }

    finally:
        db.close()


def deletar_disciplina_db(id):
    db: Session = SessionLocal()

    try:
        disciplina = db.query(Disciplina).filter(Disciplina.id == id).first()

        if not disciplina:
            return False

        db.delete(disciplina)
        db.commit()

        return True

    finally:
        db.close()