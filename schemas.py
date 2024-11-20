from datetime import datetime

from pydantic import BaseModel


class PublicacaoSchema(BaseModel):
    id_pub: int
    id_autor: int
    legenda: str
    curtidas: int
    data_criacao: datetime
    caminho_imagem: str
