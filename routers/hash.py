import hashlib
from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/hash', tags=['hash'])


@router.get("/hash256/", status_code=HTTPStatus.OK)
def get_hash():
    sha256_hash = hashlib.sha3_256()

    with open('csv/publicacoes.csv', 'rb') as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)

    return JSONResponse(content={"sha256": sha256_hash.hexdigest()})
