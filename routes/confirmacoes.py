# Rotas relacionadas as confirmacoe
from fastapi import APIRouter, HTTPException
from crud.confirmacao import criar_confirmacao, get_confirmacoes, get_confirmacoes_conviteID, get_num_confirmacoes_conviteID
from schemas import Confirmacao
from database import supabase
from typing import List

router = APIRouter()

@router.post("/confirmar")
def confirmar_presenca(confirmacao : Confirmacao ):
    response = criar_confirmacao(confirmacao)
    return response

@router.get("/confirmacoes", response_model=List[Confirmacao])
def listar_confirmacoes ():
    response = get_confirmacoes()
    if response:
        return response
    else:
        return {"error": "Erro ao listar"}

@router.get("/confirmacoes/{convite_id}", response_model=List[Confirmacao])
def listar_confirmacoes_convite(convite_id: str):
    return get_confirmacoes_conviteID(convite_id)

@router.get("/confirmacoes/num/{convite_id}")
def buscar_num_confirmacoes(convite_id: str):
    return {"numConfirmacao": get_num_confirmacoes_conviteID(convite_id)}