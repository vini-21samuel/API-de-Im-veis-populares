import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jose import jwt
from pydantic_settings import BaseSettings

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITH = os.getenv("JWT_ALGORITH")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# Classe de configurações
class Settings(BaseSettings):
    POSTGRES_PORT: int = POSTGRES_PORT
    POSTGRES_PASSWORD: str = POSTGRES_PASSWORD
    POSTGRES_USER: str = POSTGRES_USER
    POSTGRES_DB: str = POSTGRES_DB
    POSTGRES_HOST: str = POSTGRES_HOST
    POSTGRES_HOSTNAME: str = POSTGRES_HOST
    DATABASE_URL: str = DATABASE_URL

    JWT_SECRET: str = JWT_SECRET
    JWT_ALGORITHM: str = JWT_ALGORITH
    ACCESS_TOKEN_EXPIRE_MINUTES: int = ACCESS_TOKEN_EXPIRE_MINUTES

    class Config:
        env_file = "./.env"  # Arquivo de variáveis de ambiente

# Instancia a classe de configurações
settings = Settings()

# Função para criar o token de acesso
def create_access_token(data: dict, expires_delta: timedelta = None):
    # Definir o tempo de expiração
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # Criar o payload
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    # Gerar o token JWT usando as configurações
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
