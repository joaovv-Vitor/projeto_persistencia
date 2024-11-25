import csv
import os
from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from schemas import PublicacaoSchema

router = APIRouter(prefix='/publicacoes', tags=['publicacoes'])

sv_file = os.path.join('csv', 'publicacoes.csv')


@router.post('/nova_publicacao', status_code=status.HTTP_201_CREATED)
def create_publicacao(publicacao: PublicacaoSchema):
    publicacoes = carregar_publicacoes_csv()

    if any(int(pub["id_pub"]) == publicacao.id_pub for pub in publicacoes):
        raise HTTPException(status_code=400, detail="Publicação já existe")
    if publicacao.id_pub < 0:
        raise HTTPException(status_code=400, detail="ID inválido")

    nova_publi = {
        "id_pub": publicacao.id_pub,
        "id_autor": publicacao.id_autor,
        "legenda": publicacao.legenda,
        "curtidas": publicacao.curtidas,
        "data_criacao": publicacao.data_criacao.strftime('%d/%m/%Y %H:%M:%S'),
        "caminho_imagem": publicacao.caminho_imagem,
    }

    publicacoes.append(nova_publi)
    salvar_publicacoes_csv(publicacoes)

    return {"mensagem": "Publicação criada!", "publicacao": nova_publi}


@router.get('/listar_publicacoes', status_code=status.HTTP_200_OK)
def listar_publicacoes():
    publicacoes = carregar_publicacoes_csv()
    return {"publicações": publicacoes}


@router.get('/pegar_publicacao/{publicacao_id}', status_code=200)
def get_publicacao(publicacao_id: int):
    publicacoes = carregar_publicacoes_csv()

    for pub in publicacoes:
        if int(pub["id_pub"]) == publicacao_id:
            return {"publicação": pub}
    raise HTTPException(status_code=404, detail="Not found")


@router.get('/quantidade_de_publicacoes', status_code=status.HTTP_200_OK)
def quantidade_publicacoes():
    publicacoes = carregar_publicacoes_csv()
    return {"quantidade de publicações": len(publicacoes)}


@router.put('/atualizar_publicacao/{publicacao_id}', status_code=200)
def atualizar_publicacao(publicacao_id: int, publicacao: PublicacaoSchema):
    publicacoes = carregar_publicacoes_csv()
    for pub in publicacoes:
        if int(pub["id_pub"]) == publicacao_id:

            form_hr = publicacao.data_criacao.strftime('%d/%m/%Y %H:%M:%S')

            pub["id_pub"] = publicacao.id_pub
            pub["id_autor"] = publicacao.id_autor
            pub["legenda"] = publicacao.legenda
            pub["curtidas"] = publicacao.curtidas
            pub["data_criacao"] = form_hr
            pub["caminho_imagem"] = publicacao.caminho_imagem
            salvar_publicacoes_csv(publicacoes)
            return {"mensagem": "Publicação atualizada!", "publicacao": pub}
    raise HTTPException(status_code=404, detail="Not found")


@router.delete('/deletar_publicacao/{publicacao_id}', status_code=200)
def deletar_publicacao(publicacao_id: int):
    publicacoes = carregar_publicacoes_csv()

    publicacoes_filtradas = []
    for pub in publicacoes:
        if int(pub["id_pub"]) != publicacao_id:
            publicacoes_filtradas.append(pub)

    if len(publicacoes) == len(publicacoes_filtradas):
        raise HTTPException(status_code=404, detail="Error: not found")

    salvar_publicacoes_csv(publicacoes_filtradas)

    return {'mensagem': f'Publicação {publicacao_id} deletada com sucesso!'}


def carregar_publicacoes_csv() -> List[dict]:
    if os.path.exists(sv_file) and os.path.getsize(sv_file) > 0:
        with open(sv_file, mode='r', encoding='utf-8') as file:
            pubs_dic = csv.DictReader(file)
            return list(pubs_dic)
    raise HTTPException(status_code=400, detail='empty or does not exist')


def salvar_publicacoes_csv(publicacoes: List[dict]):
    if not publicacoes:
        raise ValueError("Lista de publicações está vazia.")

    with open(sv_file, mode='w', newline='', encoding='utf-8') as file:
        colunas = publicacoes[0].keys()
        writer = csv.DictWriter(file, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(publicacoes)
