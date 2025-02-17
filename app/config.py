from pydantic_settings import BaseSettings
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Classe de configurações
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://vini_samuel:210503@localhost/imoveisdb"
    JWT_SECRET: str = "secretoforte"  # A chave secreta para gerar tokens
    JWT_ALGORITHM: str = "HS256"     # Algoritmo utilizado para o JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60  # Tempo de expiração do token

    class Config:
        env_file = ".env"  # Arquivo de variáveis de ambiente

# Instancia a classe de configurações
settings = Settings()

# Função para criar o token de acesso
def create_access_token(data: dict, expires_delta: timedelta = None):
    # Definir o tempo de expiração
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # Criar o payload
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    # Gerar o token JWT usando as configurações
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt
