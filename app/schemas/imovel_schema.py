from pydantic import BaseModel
from enum import Enum
from typing import Optional

class TipoImovel(str, Enum):
    CASA = "casa"
    APT = "apartamento"
    KITNET = "kitnet"
    DUPLEX = "duplex"

class TipoNegocio(str, Enum):
    VENDA = "venda"
    ALUGUEL = "aluguel"

class StatusImovel(str, Enum):
    DISPONIVEL = "disponivel"
    VENDIDO = "vendido"
    ALUGADO = "alugado"

class ImovelBase(BaseModel):
    titulo: str
    descricao: str
    preco: float
    tipo: TipoImovel
    tipo_negocio: TipoNegocio
    status: StatusImovel
    area: float
    cidade: str
    cep: str
    estado: str
    endereco: str

class ImovelResponse(ImovelBase):
    id: int

class ImovelUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    tipo: Optional[str] = None
    tipo_negocio: Optional[str] = None
    status: Optional[StatusImovel] = None
    area: Optional[float] = None
    cidade: Optional[str] = None
    cep: Optional[str] = None
    estado: Optional[str] = None
    endereco: Optional[str] = None