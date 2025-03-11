from fastapi import APIRouter
from crud.notificacoes import get_notificacoes, send_notificacoes, send_notificacao, delete_notificacao, get_notificacao
from schemas import NotificacaoSchema, NotificacaoCreateSchema

router = APIRouter()

@router.get("/listar-notificacoes")
def listar_notiticacaoes():
    return get_notificacoes()

@router.get("/notificacao/{notificacao_id}")
def getNotificacao(notificacao_id: str):
    return get_notificacao(notificacao_id)

@router.post("/notificar", response_model=NotificacaoSchema)
def enviarNotificacao(notificacao: NotificacaoCreateSchema, email: str):
    return send_notificacao(notificacao, email)

@router.delete("/delete-notificacao/{notiticacao_id}")
def deleteNotificacao():
    return {"message": "Notifcacao deletada com sucesso"}
    
