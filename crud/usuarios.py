#get_usuarios, create_usuario, get_usuario_ID, get_usuario_email
from database import supabase
import uuid
from fastapi import HTTPException
from schemas import UsuariosSchema, UsuarioCreateSchema, UsuarioUpdateSchema

def get_usuarios():
    response = supabase.table("usuarios").select("*").execute()
    return response.data

def get_usuario_ID(uuid: str):
    response = supabase.table("usuarios").select("*").eq("id", uuid).execute()
    if not response:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    return response.data

def get_usuario_email(email: str):
    response = supabase.table("usuarios").select("*").eq("email", email).maybe_single().execute()
    if not response:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
   
    return response.data

def create_usuario(usuario: UsuariosSchema):
    usuario_data = usuario.dict()
    response = supabase.table("usuarios").insert(usuario_data).execute()
    return response.data[0]

def update_usuario(usuario_id: str, usuario: UsuarioUpdateSchema):
    usuario_data = usuario.dict(exclude_unset=True)
    response = supabase.table("usuarios").update(usuario_data).eq("id", usuario_id).execute()
    return response.data[0]
    

def delete_usuario(uuid: str):
    usuario = get_usuario_ID(uuid)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    
    response = supabase.table("usuarios").delete().eq("id", uuid).execute()
    
    if not response.data:  # Se não houver dados na resposta, significa que o usuário já foi removido ou não existia
        raise HTTPException(status_code=400, detail="Falha ao deletar usuário ou usuário inexistente")
    
    return {"message": "Usuário Deletado com sucesso"}