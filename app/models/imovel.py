# app/models/imovel.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    area = Column(Float, nullable=False)
    cep = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    endereco = Column(String, nullable=True)

    proprietario_id = Column(Integer, ForeignKey("users.id"))
    proprietario = relationship("User", back_populates="imoveis")
    transacoes = relationship("Transacao", back_populates="imovel")
