from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    tipo_transacao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.now())
    
    imovel = relationship("Imovel", back_populates="transacoes")
    user = relationship("User", back_populates="transacoes")
