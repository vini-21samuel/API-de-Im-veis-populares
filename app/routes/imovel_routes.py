from fastapi import APIRouter, Depends

from app.core.database import get_db
from app.repositories.imovel_repository import *
from app.schemas.imovel_schema import ImovelBase, ImovelUpdate

router = APIRouter()

@router.post("/create")
def add_imovel(imovel: ImovelBase, db: Session = Depends(get_db)):
    new_imovel = Imovel(**imovel.model_dump())
    return create_imovel_repository(db, new_imovel)


@router.get("/list")
def list_imoveis(db: Session = Depends(get_db)):
    return get_imoveis_repository(db)


@router.patch("/update/{id}")
def update_imovel(id: int, imovel: ImovelUpdate, db: Session = Depends(get_db)):
    return update_imovel_repository(db, id, imovel)


@router.delete("/delete")
def delete_imovel(id: int, db: Session = Depends(get_db)):
    return delete_imovel_repository(db, id)


@router.get("/cep/{cep}")
def get_imoveis_by_cep(cep: str, db: Session = Depends(get_db)):
    return get_imoveis_by_cep_repository(db, cep)


@router.get("/{id}")
def get_imovel_by_id(id: int, db: Session = Depends(get_db)):
    reponse = get_imovel_by_id_repository(db, id)
    if reponse is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Imóvel não encontrado")

    return reponse
