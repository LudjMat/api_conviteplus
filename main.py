from fastapi import FastAPI, HTTPException
from database import supabase
from routes import convites, felicitacoes, convidados, eventos, confirmacoes, usuarios, notificacoes
import uuid
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurações de CORS
origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
	"https://conviteplus.vercel.app",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir apenas esses domínios
    allow_credentials=True, # Permit ir cookies e headers de autenticação
    allow_methods=["*"],    # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],    # Permitir tbodos os header
)

@app.get("/")
async def root():
    return {"message": "Bem Vinda ao CONVITEplus"}

app.include_router(convidados.router, prefix="/convidados", tags=["Convidados"])
app.include_router(confirmacoes.router, prefix="/confirmacao", tags=["Confirmacoes"])
app.include_router(convites.router, prefix="/convite", tags=["Convites"])
app.include_router(eventos.router, prefix="/eventos", tags=["Eventos"])
app.include_router(felicitacoes.router, prefix="/felicitacoes", tags=["Felicitações"])
app.include_router(notificacoes.router, prefix="/notificacoes", tags=["Notificações"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])