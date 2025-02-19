from pydantic import BaseModel

class UserBase(BaseModel):
    nome: str
    email: str
    is_admin: bool = False

class UserCreate(UserBase):
    senha: str
    telefone: str

class UserResponse(UserBase):
    id: int
    telefone: str

class UserLogin(BaseModel):
    email: str
    senha: str
