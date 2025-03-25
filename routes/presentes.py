# Rotas relacionadas a presentes
from fastapi import APIRouter, HTTPException
from crud.presentes import get_presente, create_presente, update_presente, delete_presente, get_Presentes
from schemas import PresenteSchema

router = APIRouter()

@router.get("/lista", response_model=list[PresenteSchema])
def ListarPresentes():
    return get_Presentes()

@router.get("/{uuid}")
def getPresente(uuid: str):
    presente = get_presente(uuid)
    if presente:
        return presente
    raise HTTPException(status_code=404, detail="Presente não encontrado")

@router.post("/")
def createPresente(presente: PresenteSchema):
    return create_presente(presente)

@router.put("/update-presente/{presente_id}")
def updatePresente():
    return {"message": "Presente atualizado com sucesso"}

@router.delete("/delete-presente/{presente_id}")
def deletePresente():
    return {"message": "Presente Deletado com sucesso"}