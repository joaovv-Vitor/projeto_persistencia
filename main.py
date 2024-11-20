from fastapi import FastAPI
from http import HTTPStatus
from routers.publicacoes import router as publicacoes_router

app = FastAPI()
app.include_router(publicacoes_router)

@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return{'message': 'olar mundo!!'}


