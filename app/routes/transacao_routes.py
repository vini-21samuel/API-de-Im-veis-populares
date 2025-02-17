from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.transacao_repository import create_transacao, list_transacoes
from app.schemas.transacao_schema import TransacaoCreate

router = APIRouter()

@router.post("/locacao")
@router.post("/venda")
def registrar_transacao(transacao: TransacaoCreate, db: Session = Depends(get_db)):
    return create_transacao(db, transacao)

@router.get("/listar")
def listar_transacoes(db: Session = Depends(get_db)):
    return list_transacoes(db)
