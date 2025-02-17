from pydantic import BaseModel
from datetime import datetime

class TransacaoBase(BaseModel):
    imovel_id: int
    comprador_id: int
    valor: float

class TransacaoCreate(TransacaoBase):
    pass

class TransacaoResponse(TransacaoBase):
    id: int
    data: datetime

    class Config:
        from_attributes = True
