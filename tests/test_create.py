import json
from src.service import criar_disciplina


def test_criar_disciplina():
    # Limpa o JSON antes do teste
    with open("data/disciplinas.json", "w", encoding="utf-8") as arquivo:
        json.dump([], arquivo)

    disciplina = criar_disciplina(
        1,
        "Programação Orientada a Objetos",
        "2026-03-01",
        "2026-07-10",
        30,
        False
    )

    assert disciplina["id"] == 21
    assert disciplina["titulo"] == "Programação Orientada a Objetos"
    assert disciplina["data_inicio"] == "2026-03-01"
    assert disciplina["data_termino"] == "2026-07-10"
    assert disciplina["numero_vagas"] == 30
    assert disciplina["verao"] is False