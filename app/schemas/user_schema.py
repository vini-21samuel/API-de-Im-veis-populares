from pydantic import BaseModel

# Esquema base para o usuário (dados comuns em várias operações)
class UserBase(BaseModel):
    nome: str
    email: str

# Esquema para criação de usuário
class UserCreate(UserBase):
    senha: str  # Senha será recebida em texto simples (será hashada ao criar o usuário)
    telefone: str  # Adicionado campo telefone

# Esquema para resposta do usuário
class UserResponse(UserBase):
    id: int
    telefone: str  # Adicionado campo telefone

    class Config:
        from_attributes = True  # Atualizado para Pydantic V2

# Novo esquema para login, apenas com email e senha
class UserLogin(BaseModel):
    email: str
    senha: str
