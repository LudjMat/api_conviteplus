# Rotas relacionadas a convites
from fastapi import APIRouter, HTTPException
from crud.convites import get_convite, create_convite
from schemas import ConviteSchema

router = APIRouter()

@router.get("/{uuid}")
async def get_convite_route(uuid: str):
    convite = get_convite(uuid)
    if convite:
        return convite
    raise HTTPException(status_code=404, detail="Convite não encontrado")

@router.post("/")
async def create_convite_route(convite: ConviteSchema):
    return create_convite(convite)
