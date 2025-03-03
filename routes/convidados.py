# Rotas relacionadas a convidados
from fastapi import APIRouter, HTTPException
from crud.convidados import get_convidados, create_convidado
from schemas import ConvidadoSchema

router = APIRouter()
#
@router.get("/{uuid}")
async def get_convidado_route(uuid: str):
    convidado = get_convidados(uuid)
    if convidado:
        return convidado
    raise HTTPException(status_code=404, detail="convidado não encontrado")

@router.post("/")
async def create_convidado_route(convidado: ConvidadoSchema):
    return create_convidado(convidado)
