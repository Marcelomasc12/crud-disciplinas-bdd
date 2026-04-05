import json
from src.service import deletar_disciplina, listar_disciplinas


def test_deletar_disciplina():
    disciplinas_teste = [
        {
            "id": 1,
            "titulo": "Engenharia de Software",
            "data_inicio": "2026-03-01",
            "data_termino": "2026-07-10",
            "numero_vagas": 35,
            "verao": False
        }
    ]

    # Coloca uma disciplina no JSON antes do teste
    with open("data/disciplinas.json", "w", encoding="utf-8") as arquivo:
        json.dump(disciplinas_teste, arquivo, ensure_ascii=False, indent=4)

    resultado = deletar_disciplina(1)
    disciplinas = listar_disciplinas()

    assert resultado is True
    assert len(disciplinas) == 0