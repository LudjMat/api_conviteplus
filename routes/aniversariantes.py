# Rotas relacionadas a aniversariantes
from fastapi import APIRouter, HTTPException
from crud.convites import get_convite, create_convite
from schemas import ConviteSchema
from database import supabase

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


@router.get("/aniversariante/{aniversariante_id}")
def get_aniversariante(aniversariante_id: str):
    #print(f"🔍 Buscando aniversariante com ID: {aniversariante_id}")  # Debug
    aniversariante_response = (
        supabase.table("aniversariantes")
        .select("*")  # Pegamos tudo para verificar
        .eq("id", aniversariante_id)
        .maybe_single()
        .execute()
    )

    if aniversariante_response and aniversariante_response.data:
        return {"status": "success", "data": aniversariante_response.data}
    else:
        return {"status": "error", "message": f"Aniversariante {aniversariante_id} não encontrado"}