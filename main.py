from fastapi import FastAPI
from schemas import PublicacaoSchema
from starlette import status
import csv

app = FastAPI()

@app.post('/publicacao/', status_code=status.HTTP_201_CREATED)
def create_publicacao(publicacao: PublicacaoSchema):
    with open('csv\publicacoes.csv', 'a') as publi_csv:
        nova_publi = csv.writer(publi_csv)
        nova_publi.writerow(publicacao)

