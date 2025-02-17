from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)  # Hash da senha
    telefone = Column(String, nullable=True)
    tipo = Column(String, nullable=False)   # "admin" ou "user"

    imoveis = relationship("Imovel", back_populates="proprietario")
    transacoes = relationship("Transacao", back_populates="comprador")
