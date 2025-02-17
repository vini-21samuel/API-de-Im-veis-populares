from pydantic import BaseModel
from enum import Enum
from typing import Optional

class TipoImovel(str, Enum):
    VENDA = "venda"
    LOCACAO = "locacao"

class StatusImovel(str, Enum):
    DISPONIVEL = "disponivel"
    VENDIDO = "vendido"
    ALUGADO = "alugado"

class ImovelBase(BaseModel):
    titulo: str
    descricao: str
    preco: float
    tipo: TipoImovel
    status: Optional[StatusImovel] = StatusImovel.DISPONIVEL
    area: Optional[float]
    cidade: str
    estado: str
    endereco: str

class ImovelCreate(ImovelBase):
    proprietario_id: int

class ImovelResponse(ImovelBase):
    id: int
    proprietario_id: int

    class Config:
        from_attributes = True
