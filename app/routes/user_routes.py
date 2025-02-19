from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST

from app.schemas.user_schema import UserCreate, UserLogin  # O esquema para validação dos dados de entrada
from app.services.auth_service import hash_password, authenticate_user, create_access_token  # Funções de autenticação
from app.repositories.user_repository import create_user_repository, get_user_by_id_repository, recover_password_repository, get_user_by_email_repository
from app.core.database import get_db
from app.models.user import User

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.senha)
    user.senha = hashed_password

    new_user = User(**user.model_dump())
    new_user.is_admin = False
    response = create_user_repository(db, new_user)
    if response is None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Falha ao tentar regitrar, o email pode já está em uso.",
        )
    return response


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.senha)

    if not db_user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

    access_token = create_access_token({"sub": db_user.email})
    return {"access_token": access_token, "data": db_user}


@router.get("/info/{id}")
def get_user_info(id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id_repository(db, id)

    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return db_user


@router.patch("/recovery")
def recovery(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email_repository(db, user.email)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="Email não registrado, tente novamente.",
        )

    return recover_password_repository(db, user.email, user.senha)
