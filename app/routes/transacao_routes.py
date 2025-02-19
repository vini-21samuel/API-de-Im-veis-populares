from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from app.core.database import get_db
from app.repositories.transacao_repository import create_transacao_repository, list_transacoes_repository
from app.schemas.transacao_schema import TransacaoBase

router = APIRouter()


@router.post("/create")
def registrar_transacao(transacao: TransacaoBase, db: Session = Depends(get_db)):
    transacao_created = create_transacao_repository(db, transacao)

    if transacao_created is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="Erro na requisição, verifique os dados informados")

    return transacao_created


@router.get("/list")
def listar_transacoes(db: Session = Depends(get_db)):
    return list_transacoes_repository(db)
