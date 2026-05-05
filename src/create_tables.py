from src.database import Base, engine
from src.models import Disciplina

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")