# Funções CRUD para confirmacao
from database import supabase
from schemas import Confirmacao
import uuid


def get_confirmacoes():
    response = supabase.table("confirmacoes").select("*").execute()
    return response.data

def criar_confirmacao(confirmacao: Confirmacao):
    data = confirmacao.dict()
    response = supabase.table("confirmacoes").insert(data).execute()

    if response.data:
        return response.data
    else:
        return {"error": "Erro ao confirmar!"}

def get_confirmacoes_conviteID(convite_id: str):
    response = supabase.table("confirmacoes").select("*").eq("convite_id", convite_id).execute()
    
    if response.data:
        return response.data
    else: return {"erro": "Nenhuma confirmacao encontrada"}

def get_num_confirmacoes_conviteID(convite_id: str):
    response = supabase.table("confirmacoes").select("id", count="exact").eq("convite_id", convite_id).execute()
    return response.count