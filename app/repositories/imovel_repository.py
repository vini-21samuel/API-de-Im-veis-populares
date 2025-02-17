from sqlalchemy.orm import Session
from app.models.imovel import Imovel

def create_imovel(db: Session, imovel: Imovel):
    db.add(imovel)
    db.commit()
    db.refresh(imovel)
    return imovel

def get_imoveis(db: Session):
    return db.query(Imovel).all()

def update_imovel(db: Session, imovel: Imovel):
    db.commit()
    return imovel

def delete_imovel(db: Session, imovel: Imovel):
    db.delete(imovel)
    db.commit()
