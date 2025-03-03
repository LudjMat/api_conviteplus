# Rotas relacionadas a felicitacoes
from fastapi import APIRouter, HTTPException
from crud.felicitacoes import get_felicitacoes, create_felicitacao
from schemas import FelicitacaoSchema

router = APIRouter()

@router.get("/{convite_id}/felicitacoes")
async def get_felicitacoes_route(convite_id: str):
    return get_felicitacoes(convite_id)

@router.post("/felicitacao")
async def create_felicitacao_route(felicitacao: FelicitacaoSchema):
    return create_felicitacao(felicitacao)
