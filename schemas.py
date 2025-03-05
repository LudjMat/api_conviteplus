from pydantic import BaseModel
from datetime import date, time

class AniversarianteSchema(BaseModel):
    id: str
    nome: str
    

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
    aniversariante_id: str
    nome: str
    sobrenome: str
    telefone: int
    confirmado: str

class Confirmacao(BaseModel):
    convite_id: str
    nome: str
    sobrenome: str
    telefone: int
    confirmado: bool = True