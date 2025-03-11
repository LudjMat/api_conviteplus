# Rotas relacionadas a aniversariantes
from fastapi import APIRouter, HTTPException
from crud.evento import update_evento, get_evento, delete_evento, create_evento, get_evento_bilhete, get_eventos
from schemas import EventoUpdate, EventoSchema, EventoCreate
from database import supabase

router = APIRouter()

@router.get("/listar-eventos", response_model=list[EventoSchema])
def getEventos():
    return get_eventos()


@router.post("/evento", response_model=EventoSchema)
def criar_evento(evento: EventoCreate):
    return create_evento(evento)

@router.get("/evento/{evento_id}", response_model=EventoSchema)
def buscar_evento(evento_id: str):
    evento = get_evento(evento_id)

    if not evento:
        raise HTTPException(status_code=404, detail="Aniversariante nao encotrado")
    return evento

"""@router.get("/evento/bilhete/{bilhete}", response_model=EventoSchema)
def buscar_evento_bilhete(bilhete: str):
    return get_evento_bilhete(bilhete)*/"""


@router.put("/update/{evento_id}", response_model=EventoSchema)
def atualizar_evento(evento_id: str, novos_dados: EventoUpdate):
    return update_evento(evento_id, novos_dados)


@router.delete("/delete/{evento_id}")
def deletar_evento(evento_id: str):
    return delete_evento(evento_id)

