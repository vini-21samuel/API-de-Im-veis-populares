from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.imovel_schema import ImovelCreate, ImovelResponse
from app.repositories.imovel_repository import create_imovel, get_imoveis
from app.core.database import get_db

router = APIRouter()

@router.post("/imoveis", response_model=ImovelResponse)
def add_imovel(imovel: ImovelCreate, db: Session = Depends(get_db)):
    return create_imovel(db, imovel)

@router.get("/imoveis", response_model=list[ImovelResponse])
def list_imoveis(db: Session = Depends(get_db)):
    return get_imoveis(db)
