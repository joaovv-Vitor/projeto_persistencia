from fastapi import FastAPI
from schemas import PublicacaoSchema
from starlette import status
import pandas as pd

app = FastAPI()

@app.post('/publicacao/', status_code=status.HTTP_201_CREATED)
def create_publicacao(publicacao: PublicacaoSchema):

    nova_publi = pd.DataFrame([publicacao])
    nova_publi.to_csv('csv/publicacoes.csv', mode='a', index=False, header=False)
    
    return {"message": "Publicação criada com sucesso", "publicacao": publicacao}
