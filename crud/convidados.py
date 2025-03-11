# Funções CRUD para convidados
from database import supabase
from schemas import ConvidadoSchema, ConvidadoCreateSchema
import uuid
from datetime import datetime

def get_convidado(uuid: str):
    response = supabase.table("convidados").select("*").eq("id", uuid).single().execute()
    return response.data

def create_convidado(convidado: ConvidadoCreateSchema):
    convidado_data = convidado.dict()
    convidado_data["id"] = str(uuid.uuid4())
    #convidado_data["created_at"] = datetime.utcnow()
    response = supabase.table("convidados").insert(convidado_data).execute()
    return response.data

def get_convidados():
    response = supabase.table("convidados").select("*").execute()
    return response.data

def get_convidado_eventoID(uuid: str):
    evento = supabase.table("eventos").select("*").eq("id", uuid).maybe_single().execute()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento nao encontrado")
    convidado = supabase.table("convidados").select("*").eq("evento_id", uuid).maybe_single().execute()

    return convidado.data

def delete_convidado(uuid: str):
    convidado = get_convidado(uuid)
    if not convidado:
        raise HTTPException(status_code=404, detail="Convidado nao encontrado")
    response = supabase.table("convidados").delete().eq("id", uuid).execute()
    return {"message": "convidado deletado com sucesso"}