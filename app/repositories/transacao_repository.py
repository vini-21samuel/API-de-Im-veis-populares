from typing import Any

from sqlalchemy.orm import Session

from app.models.imovel import Imovel
from app.models.transacao import Transacao
from app.schemas.transacao_schema import TransacaoBase


def create_transacao_repository(db: Session, transacao: TransacaoBase):
    imovel_id = transacao.imovel_id

    if imovel_id is None:
        return None

    imovel = db.query(Imovel).get(imovel_id)
    if not imovel:
        return None

    imovel_preco = imovel.preco
    tipo = imovel.tipo_negocio

    if not imovel_preco:
        return None

    db_transacao = Transacao(**transacao.model_dump())
    db_transacao.valor = imovel_preco
    db_transacao.tipo_transacao = tipo

    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)

    return {
        "status": "success",
        "data": db_transacao
    }


def list_transacoes_repository(db: Session):
    transacoes = db.query(Transacao).all()

    return {
        "status": "success",
        "results": len(transacoes),
        "data": transacoes
    }
