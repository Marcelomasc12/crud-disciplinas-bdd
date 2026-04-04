import json
import os

CAMINHO_ARQUIVO = "data/disciplinas.json"


def ler_disciplinas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_disciplinas(disciplinas):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(disciplinas, arquivo, indent=4, ensure_ascii=False)