from pydantic import BaseModel
from datetime import datetime

class PublicacaoSchema(BaseModel):
    id_pub: int
    id_autor: int
    legenda: str
    curtidas: int
    data_criacao: datetime
