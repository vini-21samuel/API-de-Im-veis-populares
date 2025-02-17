from sqlalchemy.orm import Session
from app.models.transacao import Transacao
from app.schemas.transacao_schema import TransacaoCreate

def create_transacao(db: Session, transacao: TransacaoCreate):
    db_transacao = Transacao(**transacao.dict())
    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)
    return db_transacao

def list_transacoes(db: Session):
    return db.query(Transacao).all()
