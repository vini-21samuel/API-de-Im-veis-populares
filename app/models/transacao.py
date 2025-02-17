from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    comprador_id = Column(Integer, ForeignKey("users.id"))
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)
    
    imovel = relationship("Imovel", back_populates="transacoes")
    comprador = relationship("User", back_populates="transacoes")
