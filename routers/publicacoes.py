from fastapi import APIRouter
import pandas as pd
from starlette import status
from schemas import PublicacaoSchema


router = APIRouter(prefix='/publicacoes', tags=['publicaoes'])

@router.post('/publicacoes', status_code=status.HTTP_201_CREATED)
def create_publicacao(publicacao: PublicacaoSchema):

    nova_publi = pd.DataFrame([publicacao])
    nova_publi.to_csv('csv/publicacoes.csv', mode='a', index=False, header=False)
    
    return {"message": "Publicação criada com sucesso", "publicacao": publicacao}
