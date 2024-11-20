from http import HTTPStatus

from fastapi import FastAPI

from routers.publicacoes import router as publicacoes_router
from routers.hash import router as hash_router

app = FastAPI()
app.include_router(publicacoes_router)
app.include_router(hash_router)




@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'olar mundo!!'}
