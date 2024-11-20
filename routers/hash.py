import hashlib
from http import HTTPStatus
import os

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/hash', tags=['hash'])

sv_file = os.path.join("csv", "publicacoes.csv")


@router.get('/hash256/', status_code=HTTPStatus.OK)
def get_hash():
    sha256_hash = hashlib.sha3_256()

    with open(sv_file, 'rb') as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)

    return JSONResponse(content={"sha256": sha256_hash.hexdigest()})
