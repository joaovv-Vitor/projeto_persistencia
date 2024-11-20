
from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import zipfile
import os


router = APIRouter(prefix='/compactacao',tags=['compactacao'])

csv_file = os.path.join('csv', 'publicacoes.csv')
zip_file = os.path.join('csv', 'publicacoes.zip')

@router.get('/csv_to_zip/', status_code=HTTPStatus.OK)
def csv_to_zip():
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zip:
        zip.write(csv_file, arcname='publicacoes.csv')
    
    return JSONResponse(content={"message": "Arquivo CSV compactado com sucesso."})


