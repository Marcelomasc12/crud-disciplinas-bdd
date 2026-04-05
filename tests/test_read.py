import json
from src.service import listar_disciplinas


def test_listar_disciplinas():
    disciplinas_teste = [
        {
            "id": 1,
            "titulo": "Banco de Dados",
            "data_inicio": "2026-03-01",
            "data_termino": "2026-07-10",
            "numero_vagas": 40,
            "verao": False
        }
    ]

    # Coloca uma disciplina no JSON antes do teste
    with open("data/disciplinas.json", "w", encoding="utf-8") as arquivo:
        json.dump(disciplinas_teste, arquivo, ensure_ascii=False, indent=4)

    disciplinas = listar_disciplinas()

    assert len(disciplinas) == 1
    assert disciplinas[0]["id"] == 1
    assert disciplinas[0]["titulo"] == "Banco de Dados"
    assert disciplinas[0]["numero_vagas"] == 40