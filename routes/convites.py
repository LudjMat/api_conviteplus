# Rotas relacionadas a convites
from fastapi import APIRouter, HTTPException
from crud.convites import get_convite, create_convite, update_convite, delete_convite
from schemas import ConviteSchema

router = APIRouter()

@router.get("/{uuid}")
def getConvite(uuid: str):
    convite = get_convite(uuid)
    if convite:
        return convite
    raise HTTPException(status_code=404, detail="Convite não encontrado")

@router.post("/")
def createConvite(convite: ConviteSchema):
    return create_convite(convite)

@router.put("/update-convite/{convite_id}")
def updateConvite():
    return {"message": "Convite atualizado com sucesso"}

@router.delete("/delete-convite/{convite_id}")
def deleteConvite():
    return {"message": "Convite Deletado com sucesso"}