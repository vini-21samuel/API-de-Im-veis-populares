import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.routes import user_routes, imovel_routes, transacao_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Imóveis")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(imovel_routes.router, prefix="/imoveis", tags=["Imóveis"])
app.include_router(transacao_routes.router, prefix="/transacoes", tags=["Transações"])


@app.get("/")
def read_root():
    return {"message": "Casa Certa"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
