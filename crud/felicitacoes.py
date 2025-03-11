# Funções CRUD para felicitacoes
from database import supabase
from schemas import FelicitacaoSchema
import uuid
from datetime import datetime

def get_felicitacoes_convite(convite_id: str):
    response = supabase.table("felicitacoes").select("*").eq("convite_id", convite_id).execute()
    return response.data

def create_felicitacao(felicitacao: FelicitacaoSchema):
    felicitacao_data = felicitacao.dict()
    felicitacao_data["id"] = str(uuid.uuid4())
    #felicitacao_data["created_at"] = datetime.utcnow()
    response = supabase.table("felicitacoes").insert(felicitacao_data).execute()
    return response.data

def get_felicitacoes():
    response = supabase.table("convites").select("*").execute()
    return response.data

def get_felicitacao(uuid: str):
    felicitacao = supabase.table("felicitacoes").select("*").eq("id", uuid).maybe_single().execute()
    if not felicitacao:
        raise HTTPException(status_code=404, detail="Felicitacao nao encontrada")
    return felicitacao.data

def delete_felicitacao(uuid: str):
    felicitacao = get_felicitacao(uuid)
    if not felicitacao:
        raise HTTPException(status_code=404, detail="Felicitacao nao encontrada")
    supabase.table("felicitacoes").delete().eq("id", uuid).execute()
    return {"message":"Felicitacao deetada com sucesso"}
