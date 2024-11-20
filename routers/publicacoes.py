import pandas as pd
from fastapi import APIRouter
from starlette import status
import os


from schemas import PublicacaoSchema

router = APIRouter(prefix='/publicacoes', tags=['publicaoes'])

sv_file = os.path.join("csv", "publicacoes.csv")

@router.post('/publicacoes', status_code=status.HTTP_201_CREATED)
def create_publicacao(publicacao: PublicacaoSchema):

    nova_publi = pd.DataFrame([publicacao])
    nova_publi.to_csv(sv_file, mode='a', index=False, header=False)

    return {"message": "Publicação criada com sucesso", "publicacao": publicacao}

# @router.get('/listar_publicacoes', status_code= status.HTTP_200_OK)
def listar_publicacoes():
    if os.path.exists(sv_file) and os.path.getsize(sv_file)>0:#checagem p ver se o arquivo existe e se nao está vazio
        df= pd.read_csv(sv_file)#p ler o csv
        publicacoes_dic= df.to_dict(orient='records')#converte p dic fazendo associaçao de valor/coluna
        return{"publicações":publicacoes_dic}#retorna o json
    raise FileNotFoundError(f"O arquivo não existe ou está vazio.")