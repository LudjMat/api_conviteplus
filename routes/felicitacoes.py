# Rotas relacionadas a felicitacoes
from fastapi import APIRouter, HTTPException
from crud.felicitacoes import get_felicitacoes_convite, create_felicitacao, get_felicitacoes, get_felicitacao, delete_felicitacao
from schemas import FelicitacaoSchema

router = APIRouter()

@router.get("/listar-felicitacoes", response_model=list[FelicitacaoSchema])
def getFelicitacoes():
    return get_felicitacoes()

@router.get("/{convite_id}/felicitacoes", response_model=list[FelicitacaoSchema])
def getFelicitacoes_convite(convite_id: str):
    return get_felicitacoes(convite_id)

@router.post("/create-felicitacao")
def createFelicitacao(felicitacao: FelicitacaoSchema):
    return create_felicitacao(felicitacao)

@router.get("/felicitacao/{felicitacao_id}", response_model=FelicitacaoSchema)
def getFelicitacao(felicitacao_id: str):
    felicitacao = get_felicitacao(felicitacao_id)
    return felicitacao

@router.delete("/delete-felicitacao/{felicitacao_id}")
def deleteFelicitacao(felicitacao_id: str):
    return delete_felicitacao(felicitacao_id)
