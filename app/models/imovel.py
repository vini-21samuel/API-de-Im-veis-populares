from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)
    tipo_negocio = Column(String, nullable=False)
    status = Column(String, nullable=False)
    area = Column(Float, nullable=False)
    cep = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    endereco = Column(String, nullable=True)

    transacoes = relationship("Transacao", back_populates="imovel")
