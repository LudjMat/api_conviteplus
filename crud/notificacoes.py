from database import supabase
from crud.usuarios import get_usuario_email
from schemas import NotificacaoCreateSchema
from datetime import datetime
from fastapi import HTTPException
def get_notificacoes():
    response = supabase.table("notificacoes").select("*").execute()
    if not response:
        raise HTTPException(status_code=404, detail="Nenhuma notificacao encontrada")

    return  response.data

def get_notificacao(uuid: str):
    notificacao = supabase.table("notificacoes").select("*").eq("id", uuid).maybe_single().execute()
    if not notificacao:
        raise HTTPException(status_code=404, detail="Notificacao nao encontrada")
    return notificacao.data

def send_notificacoes(notificacao: NotificacaoCreateSchema, usuario_id: str):
    #nova_notificacao = notificacao.dict(exclude_unset)
    #response = supabase.table("notificacoes").insert(nova_notii)

    return {"message": "Notificacoes enviadas"}

def send_notificacao(notificacao: NotificacaoCreateSchema, email: str):
    usuario = get_usuario_email(email)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    nova_notificacao = notificacao.dict(exclude_unset=True)
    nova_notificacao["usuario_id"] = usuario["id"]

    # Converter datetime para string ISO 8601
    if "data_envio" in nova_notificacao and isinstance(nova_notificacao["data_envio"], datetime):
        nova_notificacao["data_envio"] = nova_notificacao["data_envio"].isoformat()
    
    if "data_leitura" in nova_notificacao and isinstance(nova_notificacao["data_leitura"], datetime):
        nova_notificacao["data_leitura"] = nova_notificacao["data_leitura"].isoformat()

    supabase.table("notificacoes").insert(nova_notificacao).execute()

    return {"message": "Notificação enviada com sucesso!"}

def delete_notificacao(uuid: str):
    notificacao = get_notificacao(uuid)
    if not notificacao:
        raise HTTPException(status_code=404, detail="Notificacao nao encontrada")
    supabase.table("notificacoes").delete().eq("id", uuid).execute()

    return {"message": "Notificacao deletada com sucesso"}