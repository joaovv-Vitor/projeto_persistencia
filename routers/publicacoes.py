import pandas as pd
from fastapi import APIRouter, HTTPException
from starlette import status
import os


from schemas import PublicacaoSchema

router = APIRouter(prefix='/publicacoes', tags=['publicaoes'])

sv_file = os.path.join("csv", "publicacoes.csv")

def ler_csv():#função auxiliar p evitar fazer a conversao sempre
    if os.path.exists(sv_file) and os.path.getsize(sv_file) > 0:
        return pd.read_csv(sv_file)
    raise FileNotFoundError(f"O arquivo não existe ou está vazio")


@router.post('/nova_publicacao', status_code=status.HTTP_201_CREATED)
def create_publicacao(publicacao: PublicacaoSchema):
    
    df = ler_csv()#pegar a ultma version do csv

    data_criacao_formatada = publicacao.data_criacao.strftime('%d/%m/%Y %H:%M:%S')#formata a data no padrao br

    nova_publi = {
        "id_pub": publicacao.id_pub,
        "id_autor": publicacao.id_autor,
        "legenda": publicacao.legenda,
        "curtidas": publicacao.curtidas,
        "data_criacao": data_criacao_formatada,
        "caminho_imagem": publicacao.caminho_imagem
    }#cria um novo dic com as informaçoes passadas no parametro

    df = pd.concat([df, pd.DataFrame([nova_publi])], ignore_index=True)
    df.to_csv(sv_file, index=False)

    return {"mensagem": "Publicação criada com sucesso(:", "publicacao": nova_publi}


@router.get('/listar_publicacoes', status_code= status.HTTP_200_OK)
def listar_publicacoes():
    df= ler_csv()
    publicacoes_dic= df.to_dict(orient='records')#converte p dic fazendo associaçao de valor/coluna
    return{"publicações":publicacoes_dic}#retorna o json


@router.get('/pegar_publicacao/{publicacao_id}', status_code=status.HTTP_200_OK )
def get_publicacao(publicacao_id: int):
    df= ler_csv()
    publi= df.loc[df['id_pub']==publicacao_id] #busca a linha/publi onde bate os ids. se n achar, fica vazia
    if publi.empty:
        raise HTTPException(status_code=404, detail= 'Publicação não encontrada')#autoexplicativo
    publi_dic= publi.to_dict(orient='records')
    return {"publicação":publi_dic}


@router.delete('/deletar_publicacao/{publicacao_id}', status_code=status.HTTP_200_OK)
def deletar_publicacao(publicacao_id: int):
    df= ler_csv()
    if publicacao_id not in df['id_pub'].values:
        raise HTTPException(status_code=404, detail='Publicação não encontrada')
    
    df= df[df['id_pub'] != publicacao_id]

    df.to_csv(sv_file, index=False)

    return {"mensagem":f"Publicação {publicacao_id} deletada com sucesso<3"}