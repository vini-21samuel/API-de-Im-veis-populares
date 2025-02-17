from fastapi import FastAPI
from app.core.database import engine, Base
from app.routes import user_routes, imovel_routes, transacao_routes

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar aplicação FastAPI
app = FastAPI(title="API de Imóveis")

# Incluir rotas
app.include_router(user_routes.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(imovel_routes.router, prefix="/imoveis", tags=["Imóveis"])
app.include_router(transacao_routes.router, prefix="/transacoes", tags=["Transações"])

@app.get("/")
def read_root():
    return {"message": "Casa Certa"}