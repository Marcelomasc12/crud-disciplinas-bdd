import json
from src.service import atualizar_disciplina


def test_atualizar_disciplina():
    disciplinas_teste = [
        {
            "id": 1,
            "titulo": "Redes",
            "data_inicio": "2026-03-01",
            "data_termino": "2026-07-10",
            "numero_vagas": 25,
            "verao": False
        }
    ]

    # Coloca uma disciplina no JSON antes do teste
    with open("data/disciplinas.json", "w", encoding="utf-8") as arquivo:
        json.dump(disciplinas_teste, arquivo, ensure_ascii=False, indent=4)

    disciplina_atualizada = atualizar_disciplina(1, {"numero_vagas": 50})

    assert disciplina_atualizada is not None
    assert disciplina_atualizada["numero_vagas"] == 50