from src.storage import ler_disciplinas, salvar_disciplinas
from src.disciplina import Disciplina


def criar_disciplina(id, titulo, data_inicio, data_termino, numero_vagas, verao):
    disciplinas = ler_disciplinas()

    nova_disciplina = Disciplina(
        id, titulo, data_inicio, data_termino, numero_vagas, verao
    )

    disciplinas.append(nova_disciplina.to_dict())
    salvar_disciplinas(disciplinas)

    return nova_disciplina.to_dict()


def listar_disciplinas():
    return ler_disciplinas()


def atualizar_disciplina(id, novos_dados):
    disciplinas = ler_disciplinas()

    for disciplina in disciplinas:
        if disciplina["id"] == id:
            disciplina.update(novos_dados)
            salvar_disciplinas(disciplinas)
            return disciplina

    return None


def deletar_disciplina(id):
    disciplinas = ler_disciplinas()

    novas_disciplinas = [
        disciplina for disciplina in disciplinas if disciplina["id"] != id
    ]

    if len(novas_disciplinas) == len(disciplinas):
        return False

    salvar_disciplinas(novas_disciplinas)
    return True