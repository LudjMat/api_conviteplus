# Funções CRUD para felicitacoes
from database import supabase
from schemas import FelicitacaoSchema
import uuid
from datetime import datetime

def get_felicitacoes(convite_id: str):
    response = supabase.table("felicitacoes").select("*").eq("convite_id", convite_id).execute()
    return response.data

def create_felicitacao(felicitacao: FelicitacaoSchema):
    felicitacao_data = felicitacao.dict()
    felicitacao_data["id"] = str(uuid.uuid4())
    #felicitacao_data["created_at"] = datetime.utcnow()
    response = supabase.table("felicitacoes").insert(felicitacao_data).execute()
    return response.data
