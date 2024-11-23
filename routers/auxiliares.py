import csv
import os
from typing import List

sv_file = 'csv/publicacoes_csv'


def carregar_publicacoes_csv() -> List[dict]:
    if os.path.exists(sv_file) and os.path.getsize(sv_file) > 0:
        with open(sv_file, mode='r', encoding='utf-8') as file:
            pubs_dic = csv.DictReader(file)
            return list(pubs_dic)
    return []


# Salvar publicações de uma lista de volta no CSV
def salvar_publicacoes_csv(publicacoes: List[dict]):
    if not publicacoes:
        raise ValueError("Lista de publicações está vazia.")

    with open(sv_file, mode='w', newline='', encoding='utf-8') as file:
        colunas = publicacoes[0].keys()
        writer = csv.DictWriter(file, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(publicacoes)
