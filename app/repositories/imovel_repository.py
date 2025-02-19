from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.models.imovel import Imovel
from app.schemas.imovel_schema import ImovelUpdate


def create_imovel_repository(db: Session, imovel: Imovel):
    db.add(imovel)
    db.commit()
    db.refresh(imovel)

    return {
        "status": "success",
        "imovel": imovel
    }


def get_imoveis_repository(db: Session):
    imoveis = db.query(Imovel).all()

    return {
        "status": "success",
        "results": len(imoveis),
        "imoveis": imoveis
    }


def update_imovel_repository(db: Session, id: int, imovel_update: ImovelUpdate):
    db_imovel = db.query(Imovel).filter(Imovel.id == id).first()
    if not db_imovel:
        return None

    update_data = imovel_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_imovel, key, value)

    db.commit()
    db.refresh(db_imovel)
    return {
        "status": "success",
        "imovel": db_imovel
    }


def delete_imovel_repository(db: Session, id: int):
    imovel = db.query(Imovel).filter(Imovel.id == id).first()
    if not imovel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Imóvel não encontrado")

    db.delete(imovel)
    db.commit()
    return {
        "status": "success",
        "detail": "Imóvel excluído com sucesso"
    }


def get_imoveis_by_cep_repository(db: Session, cep: str):
    imoveis = db.query(Imovel).filter(Imovel.cep == cep).all()
    return {
        "status": "success",
        "results": len(imoveis),
        "imoveis": imoveis
    }


def get_imovel_by_id_repository(db: Session, id: int):
    imovel = db.query(Imovel).filter(Imovel.id == id).first()
    if not imovel:
        return None

    return {
        "status": "success",
        "imovel": imovel
    }
