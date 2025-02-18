from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.config import settings
from sqlalchemy.orm import Session
from app.models.user import User  # Corrigindo a importação
from app.repositories.user_repository import get_user_by_email  # Mantendo a importação correta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def authenticate_user(db: Session, email: str, senha: str):
    # Buscar o usuário no banco de dados pelo email
    user = db.query(User).filter(User.email == email).first()
    
    # Verificar se o usuário foi encontrado e se a senha é válida
    if user and verify_password(senha, user.senha):
        return user
    return None
