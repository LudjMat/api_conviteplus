# Rotas relacionadas a convidados
from fastapi import APIRouter, HTTPException
from crud.convidados import get_convidado, get_convidados, create_convidado, get_convidado_eventoID, delete_convidado
from schemas import ConvidadoSchema, ConvidadoCreateSchema

router = APIRouter()
#
@router.get("/convidado/{uuid}")
async def getConvidado(uuid: str):
    convidado = get_convidados(uuid)
    if convidado:
        return convidado
    raise HTTPException(status_code=404, detail="convidado não encontrado")

@router.post("/create-convidado")
async def createConvidado(convidado: ConvidadoCreateSchema):
    return create_convidado(convidado)

@router.get("/listar-convidados", response_model=list[ConvidadoSchema])
def getConvidados():
    return get_convidados()

@router.get("/convidado-evento/{evento_id}", response_model=ConvidadoSchema)
def getConvidadoEventoID(evento_id: str):
    return get_convidado_eventoID(evento_id)

@router.delete("/delete-convidado")
def deleteConvidado(convidado_id: str):
    return delete_convidado(convidado_id)
