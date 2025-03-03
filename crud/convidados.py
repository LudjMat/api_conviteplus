# Funções CRUD para convidados
from database import supabase
from schemas import ConvidadoSchema
import uuid
from datetime import datetime

def get_convidados(uuid: str):
    response = supabase.table("convidados").select("*").eq("id", uuid).single().execute()
    return response.data

def create_convidado(convidado: ConvidadoSchema):
    convidado_data = convidado.dict()
    convidado_data["id"] = str(uuid.uuid4())
    #convidado_data["created_at"] = datetime.utcnow()
    response = supabase.table("convidados").insert(convidado_data).execute()
    return response.data

 