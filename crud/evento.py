# Funções CRUD para evento
import uuid
from schemas import EventoSchema, EventoCreate, EventoUpdate
from database import supabase
from datetime import datetime
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


def get_eventos():
    response = supabase.table("eventos").select("*").execute()
    return response.data


def get_evento(uuid: str):
    response = supabase.table("eventos").select("*").eq("id", uuid).maybe_single().execute()
    
    if not response:
        raise HTTPException(status_code=404, detail="Evento nao encontrado")
  
    return response.data

def get_evento_bilhete(bilhete: str):
    response = supabase.table("eventos").select("*").eq("bilhete", bilhete).single().execute()
    if not response.data:
        return None
  
    return response.data

def create_evento(evento_data: EventoCreate):
    dados_dict = evento_data.dict()
        # Converte o modelo Pydantic para um dicionário serializável
    dados_dict = jsonable_encoder(evento_data)
    response = supabase.table("eventos").insert(dados_dict).execute()
   
    if not response.data:
        raise HTTPException(status_code=500, detial="Erro ao criar o evento")
            
    return response.data[0]


def update_evento(uuid: str, novos_dados: EventoUpdate):
    evento = get_evento(uuid)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento nao encontrado")
    dados_dict = novos_dados.dict(exclude_unset=True)

    response = supabase.table("eventos").update(dados_dict).eq("id", uuid).execute()

    if not response.data:
        raise HTTPException(status_code=500, detail="Erro ao atualizar o evento")

    return response.data[0]


def delete_evento(uuid: str):
    evento = get_evento(uuid)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento nao encontrada")
    response = supabase.table("eventos").delete().eq("id", uuid).execute()

 
    if not response.data:
        raise HTTPException(status_code=500, detail="Erro ao deletar evento")
    
    return {"message": "Evento deletado com sucesso"}