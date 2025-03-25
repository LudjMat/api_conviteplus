# Funções CRUD para presentes
from database import supabase
from fastapi import HTTPException
from schemas import PresenteSchema, PresenteUpdateSchema
import uuid
from datetime import datetime

def get_Presentes():
    response = supabase.table("presentes").select("*").execute()
    return response.data

def get_presente(uuid: str):
    try:
        # Busca o presente pelo UUID
        response = supabase.table("presentes").select("*").eq("id", uuid).maybe_single().execute()

        # Verifica se houve erro na resposta
        if response is None or response.data is None:
            print(f"Presente não encontrado para UUID: {uuid}")
            return None

        return response.data

    except Exception as e:
        print(f"Erro ao buscar presente: {e}")
        return None

def create_presente(presente: PresenteSchema):
    presente_data = presente.dict()
    presente_data["id"] = str(uuid.uuid4())
    #presente_data["created_at"] = datetime.utcnow()
    response = supabase.table("presentes").insert(presente_data).execute()
    return response.data

def update_presente(uuid: str, presente: PresenteUpdateSchema):
    presente_data = presente.dict(exclude_unset)
    response = supabase.table("presentes").update(presente_data).eq("id", uuid).execute()
    return response.data

def delete_presente(uuid: str):
    presente = get_presente(uuid)
    if not presente:
        return HTTPException(status_code=404, detail="Presente nao encontrado")
    response = supabase.table("presentes").delete().eq("id", uuid).execute()
    return {"message": "Presente deletado com sucesso"}
    
        
