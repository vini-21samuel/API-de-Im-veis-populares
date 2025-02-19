from pydantic import BaseModel
from datetime import datetime


class TransacaoBase(BaseModel):
    imovel_id: int
    user_id: int
