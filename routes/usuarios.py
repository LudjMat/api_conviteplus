# Rotas relacionadas a felicitacoes
from fastapi import APIRouter, HTTPException
from crud.usuarios import get_usuarios, create_usuario, get_usuario_ID, get_usuario_email, update_usuario, delete_usuario
from schemas import UsuariosSchema, UsuarioCreateSchema, UsuarioUpdateSchema

router = APIRouter()

@router.get("/lista-usuarios", response_model=list[UsuariosSchema])
def getUsuarios():
    return get_usuarios()

@router.get("/usuario/{usuario_id}", response_model=UsuariosSchema)
def get_usuarioID(usuario_id: str):
    return get_usuario_ID(usuario_id)

@router.get("/usuario/email/{usuario_email}", response_model=UsuariosSchema)
def get_usuarioEmail(usuario_email: str):

    usuario = get_usuario_email(usuario_email)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    return usuario

@router.post("/usuario/create", response_model=UsuariosSchema)
def createUsuario(usuario: UsuarioCreateSchema):
    return create_usuario(usuario)

@router.put("/usuario/update/{usuario_id}", response_model=UsuariosSchema)
def updateUsuario(usuario_id: str, usuario: UsuarioUpdateSchema):
    return update_usuario(usuario_id, usuario)

@router.delete("/usuario/delete/{usuario_id}")
def deleteUsuario(usuario_id: str):
    return delete_usuario(usuario_id)