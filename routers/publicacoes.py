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


@router.post('/publicacoes', status_code=status.HTTP_201_CREATED)
def create_publicacao(publicacao: PublicacaoSchema):

    nova_publi = pd.DataFrame([publicacao])
    nova_publi.to_csv(sv_file, mode='a', index=False, header=False)

    return {"message": "Publicação criada com sucesso", "publicacao": publicacao}


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