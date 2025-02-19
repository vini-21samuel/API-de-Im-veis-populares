from sqlalchemy import Boolean
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    telefone = Column(String, nullable=True)
    is_admin = Column(Boolean, nullable=False)

    transacoes = relationship("Transacao", back_populates="user")
