from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate  # O esquema para validação dos dados de entrada
from app.services.auth_service import hash_password, authenticate_user, create_access_token  # Funções de autenticação
from app.repositories.user_repository import create_user
from app.core.database import get_db
from app.models.user import User
from app.schemas import UserLogin 

router = APIRouter()

# Função para o registro do usuário
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.senha)  # Faz o hash da senha
    new_user = User(nome=user.nome, email=user.email, senha=hashed_password, telefone=user.telefone, tipo=user.tipo)
    return create_user(db, new_user)

# Função para o login do usuário
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Autenticar o usuário com email e senha
    db_user = authenticate_user(db, user.email, user.senha)
    
    if not db_user:
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    # Gerar o token de acesso
    access_token = create_access_token({"sub": db_user.email})
    return {"access_token": access_token}
