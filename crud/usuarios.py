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
    # 1️⃣ Criar o usuário no Supabase Auth (Apenas e-mail e senha)
    auth_response = supabase.auth.sign_up({
        "email": usuario.email,
        "password": usuario.senha
    })

    if auth_response.user is None:
        raise Exception(f"Erro ao cadastrar no Auth: {auth_response.error.message}")

    user_id = auth_response.user.id  # Pegar o ID do usuário

    # 2️⃣ Salvar os dados na tabela `usuarios`
    usuario_data = usuario.dict()
    usuario_data["id"] = user_id  # Garante que o ID seja o mesmo do Auth

    response = supabase.table("usuarios").insert(usuario_data).execute()

    return response.data[0]


def update_usuario(usuario_id: str, usuario: UsuarioUpdateSchema):
    usuario_data = usuario.dict(exclude_unset=True)

    # 1️⃣ Se telefone ou nome forem passados, atualiza no Supabase Auth
    auth_data = {}
    if "telefone" in usuario_data:
        auth_data["phone"] = usuario_data.pop("telefone")  # Remove para evitar duplicação
    if "nome" in usuario_data:
        auth_data["data"] = {"display_name": usuario_data.pop("nome")}

    if auth_data:
        update_response = supabase.auth.update_user(auth_data)
        if update_response.user is None:
            raise Exception(f"Erro ao atualizar usuário no Auth: {update_response.error.message}")

    # 2️⃣ Atualiza os dados na tabela `usuarios`
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