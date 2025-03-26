from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime

# Schema para leitura/retorno de dados
class EventoSchema(BaseModel):
    id: str
    nome: str
    descricao: str
    data: date
    horario: time
    local: str
    dress_code: str
    tipo: str
    usuario_id: str

# Schema para criação de aniversariante (todos os campos são obrigatórios)
class EventoCreate(BaseModel):
    nome: str
    descricao: str
    data: date
    horario: time
    local: str
    dress_code: str
    tipo: str
    usuario_id: str

# Schema para atualização de aniversariante (todos os campos são opcionais)
class EventoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    data: Optional[date] = None
    horario: Optional[time] = None
    local: Optional[str] = None
    dress_code: Optional[str] = None
    tipo: Optional[str] = None

class ConviteSchema(BaseModel):
    id: str
    aniversariante_id: str
    localizacao: str
    code_dress: str
    horario: str
    data: str
    #
    class Config:
        json_encoders = {
            date: lambda v: v.strftime("%Y-%m-%d"),  # Converte date para string
            time: lambda v: v.strftime("%H:%M:%S"),  # Converte time para string
        }

class ConviteUpdateSchema(BaseModel):
    localizacao: str
    code_dress: str
    horario: str
    data: str

class FelicitacaoSchema(BaseModel):
    #id: str
    convite_id: str
    nome: str
    telefone: int
    mensagem: str
    

class ConfirmacaoSchema(BaseModel):
    id: str
    convite_id: str
    nome: str
    sobrenome: str
    telefone: int
    
class ConvidadoSchema(BaseModel):
    id: str
    nome: str
    sobrenome: str
    telefone: Optional[int]
    email: Optional[str]
    status: Optional[str]
    confirmado: Optional[bool]
    evento_id: Optional[str]

class ConvidadoCreateSchema(BaseModel):
    nome: Optional[str]
    sobrenome: Optional[str]
    telefone: Optional[int]
    email: Optional[str]
    status: Optional[str]
    confirmado: Optional[bool]=False
    evento_id: Optional[str]

class Confirmacao(BaseModel):
    convite_id: str
    nome: str
    sobrenome: str
    telefone: int
    status: bool = True

class UsuariosSchema(BaseModel):
    id: str
    nome: Optional[str]
    email: Optional[str]
    telefone: Optional[int]
    senha: Optional[str]

class UsuarioCreateSchema(BaseModel):
    nome: str
    email: str
    telefone: int
    senha: str

class UsuarioUpdateSchema(BaseModel):
    nome: Optional[str]=None
    email: Optional[str]=None
    telefone: Optional[int]=None
    senha: Optional[str]=None

class NotificacaoSchema(BaseModel):
    usuario_id: Optional[str] = None
    evento_id: Optional[str] = None
    tipo: Optional[str]=None
    mensagem: Optional[str]=None
    status: Optional[bool]=None
    data_envio: Optional[datetime]=None
    data_leitura: Optional[datetime]=None

class NotificacaoCreateSchema(BaseModel):
    usuario_id: Optional[str] = None
    evento_id: Optional[str] = None
    tipo: Optional[str]=None
    mensagem: Optional[str]=None
    status: Optional[bool]=None
    data_envio: Optional[datetime]=None
    data_leitura: Optional[datetime]=None
    
    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}

class PresenteSchema(BaseModel):
    id: str #= str(uuid.uuid4())  # Gera um UUID único automaticamente
    nome_destinatario: str
    telefone_destinatario: str
    mensagem: str
    imagem_url: str | None = None  # Opcional
    nome_remetente: str
    telefone_remetente: str | None = None  # Opcional
    data_envio: datetime = datetime.utcnow()

    class Config:
        orm_mode = True  # Para funcionar com ORMs como SQLAlchemy
        json_encoders = {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
        }
        
class PresenteUpdateSchema(BaseModel):
    mensagem: str | None = None
    imagem_url: str | None = None
