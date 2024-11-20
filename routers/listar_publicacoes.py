import pandas as pd 
from fastapi import APIRouter
#from schemas import PublicacaoSchema
from starlette import status
import os

router = APIRouter(prefix='/publicacoes', tags=['publicacoes'])#quero deixar a rota como
#/publicacoes/listar_publicacoes/

csv_caminho= os.path.join('csv', 'publicacoes.csv')#acessar arq com as pub

@router.get('/listar_publicacoes/', status_code=status.HTTP_200_OK)
def listar_publicacoes():
    df= pd.read_csv(csv_caminho) #leitura do csv guardando em um dataf

    publicacoesdic= df.to_dict(orient='records')#agora pega o df e converte em dic
    #o records é p associar o valor da coluna com o nome, tipo id=1

    return {"publicacoes": publicacoesdic}